Tornado-Whois
===============

Asynchronous Whois client for tornado framework

Installation
~~~~~~~~~~~~

::

    pip install tornado-whois

Example
~~~~~~~

::

    from tornado import ioloop
    from tornadowhois import AsyncWhoisClient
    from tornado.platform.caresresolver import CaresResolver

    async def main():
        whois = AsyncWhoisClient(CaresResolver())
        is_available = await whois.check_domain("tornadoweb.org")
        if is_available:
            print("tornadoweb.org is available")

        read_result = await whois.whois_query("tornadoweb.org")
        print(read_result)

    ioloop.IOLoop.current().spawn_callback(main)
