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

    from tornado import ioloop, gen
    from tornadowhois import AsyncWhoisClient


    async def main():
        data = await AsyncWhoisClient().lookup("example.com")
        print(data)

    ioloop.IOLoop.current().spawn_callback(main)


Example with non-blocking resolver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    from tornado import ioloop, gen
    from tornado.platform.caresresolver import CaresResolver
    from tornadowhois import AsyncWhoisClient

    resolver = CaresResolver()

    async def main():
        data = await AsyncWhoisClient(resolver).lookup("example.com")
        print(data)

    ioloop.IOLoop.current().spawn_callback(main)
