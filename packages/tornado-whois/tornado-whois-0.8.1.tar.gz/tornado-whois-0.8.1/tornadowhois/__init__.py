import socket
import re
import logging

from tornado import iostream

logger = logging.getLogger(__name__)

class AsyncWhoisClient(object):

    default_server = "whois.verisign-grs.com"
    servers = {
        "com": {"message":"No match for", "server":"whois.verisign-grs.com"},
        "net": {"message":"No match for", "server":"whois.verisign-grs.com"},
        "org": {"message":"NOT FOUND", "server":"whois.pir.org"},
        "io": {"message":"NOT FOUND", "server":"whois.nic.io"},
    }
    timeout_sec = 5
    whois_port = 43
    resolver = None

    def __init__(self, resolver=None):
        if not resolver:
            logging.warn("Async resolver was not set")
        self.resolver = resolver

    async def lookup(self, address):
        results = []
        await self.find_records(address, self.default_server, results)
        return(results)

    async def find_records(self, name, server, results):
        record = await self.whois_query(name)
        results.append((server, record,))

        next_server = self._read_next_server_name(record)
        prev_server = None

        while next_server and next_server != prev_server:
            record = await self.whois_query(name, next_server)
            results.append((next_server, record,))
            prev_server = next_server
            next_server = self._read_next_server_name(record)
        return(record)


    def get_domain_information(self, domain):
        for extension in list(self.servers.keys()):
            if domain.endswith(".%s" % extension):
                return self.servers.get(extension)
        return self.servers.get("com")

    async def whois_query(self, domain):
        server = self.get_domain_information(domain)['server']
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        stream = iostream.IOStream(sock)
        logging.debug("Requesting {} whois for {}".format(server, domain))
        if self.resolver and not self.is_valid_ip(server):
            server = await self._get_ip_by_name(server)
        await stream.connect((server, self.whois_port))
        domain = '%s%s' % (domain, "\r\n")
        await stream.write(domain.encode())
        data = await stream.read_until_close()
        return data

    async def check_domain(self, domain):
        information = self.get_domain_information(domain)
        result = await self.whois_query(domain)
        if information["message"] in str(result):
            return True
        return False

    async def _get_ip_by_name(self, address):
        data = await self.resolver.resolve(address, None, socket.AF_INET)
        # [(2, ('<ip_address>', None))]
        for v in data:
            num, adr = v
            return(adr[0])
        return(None)

    def _read_next_server_name(self, data):
        lines = str(data).split("\n")
        for line in lines:
            match = re.match(re.compile(
                r"^(whois|whois\s+server):\s+([A-z0-9\-\.]{0,255})", re.IGNORECASE), line.strip())
            if match:
                return match.group(2)
        return None

    def is_valid_ip(self, ip):
        if not ip or '\x00' in ip:
            # getaddrinfo resolves empty strings to localhost, and truncates
            # on zero bytes.
            return False
        try:
            res = socket.getaddrinfo(ip, 0, socket.AF_UNSPEC,
                        socket.SOCK_STREAM, 0, socket.AI_NUMERICHOST)
            return bool(res)
        except socket.gaierror as e:
            if e.args[0] == socket.EAI_NONAME:
                return False
            raise
        return True
