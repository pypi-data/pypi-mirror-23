aioodbc
=======
.. image:: https://travis-ci.org/aio-libs/aioodbc.svg?branch=master
    :target: https://travis-ci.org/aio-libs/aioodbc
.. image:: https://coveralls.io/repos/aio-libs/aioodbc/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/aio-libs/aioodbc?branch=master

**aioodbc** is Python 3.5+ module that makes possible accessing ODBC_ databases
with asyncio_. It is rely on awesome pyodbc_ library, preserve same look and
feel. *aioodbc* was written `async/await` syntax (PEP492_) thus not compatible
with Python older then 3.5.  Internally *aioodbc* employ threads to avoid
blocking the event loop, btw threads_ are not that bad as you think, other
drivers like motor_ use same approach.

**aioodbc** fully compatible and tested with uvloop_. Take a look on a test
suite, all tests are executed with both: default and uvloop_.

Supported Databases
-------------------

**aioodbc** should work with all databases supported by pyodbc_. But for now
library have been tested with: **SQLite**, **MySQL** and **PostgreSQL**. Feel
free to add other databases to the test suite by submitting PR.


Community
---------
Mailing List: https://groups.google.com/forum/#!forum/aio-libs

Chat room: https://gitter.im/aio-libs/Lobby


Basic Example
-------------

**aioodbc** based on pyodbc_ , and provides same api, you just need
to use  ``yield from conn.f()`` or ``await conn.f()`` instead of just
call ``conn.f()`` for every method.

Properties are unchanged, so ``conn.prop`` is correct as well as
``conn.prop = val``.


.. code:: python

    import asyncio
    import aioodbc


    loop = asyncio.get_event_loop()


    async def test_example():
        dsn = 'Driver=SQLite;Database=sqlite.db'
        conn = await aioodbc.connect(dsn=dsn, loop=loop)

        cur = await conn.cursor()
        await cur.execute("SELECT 42;")
        r = await cur.fetchall()
        print(r)
        await cur.close()
        await conn.close()

    loop.run_until_complete(test_example())


Connection Pool
---------------
Connection pooling ported from aiopg_ and rely on PEP492_ features:

.. code:: python

    import asyncio
    import aioodbc


    loop = asyncio.get_event_loop()


    async def test_pool():
        dsn = 'Driver=SQLite;Database=sqlite.db'
        pool = await aioodbc.create_pool(dsn=dsn, loop=loop)

        async with pool.acquire() as conn:
            cur = await conn.cursor()
            await cur.execute("SELECT 42;")
            r = await cur.fetchall()
            print(r)
            await cur.close()
            await conn.close()
        pool.close()
        await pool.wait_closed()

    loop.run_until_complete(test_example())


Context Managers
----------------
`Pool`, `Connection` and `Cursor` objects support context manager
protocol:

.. code:: python

    import asyncio
    import aioodbc


    loop = asyncio.get_event_loop()


    async def test_example():
        dsn = 'Driver=SQLite;Database=sqlite.db'

        async with aioodbc.create_pool(dsn=dsn, loop=loop) as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cur:
                    await cur.execute('SELECT 42;')
                    val = await cur.fetchone()
                    print(val)

    loop.run_until_complete(test_example())


Installation
------------

In Linux environment pyodbc_ (hence *aioodbc*) requires unixODBC_ library.
You can install it using package manager from your OS distribution, for example::

      $ sudo apt-get install unixodbc
      $ sudo apt-get install unixodbc-dev

then::

   pip install aioodbc


Run tests
---------

For testing purposes you need to install docker_ and development
requirements::

    $ pip install -r requirements-dev.txt

In order to simplify development all tests and environment created inside
separate docker image, you do not need to install any database of system level
libraries, everything happens automatically inside container.

Then just execute::

    $ make docker_build
    $ make docker_test

Test will automatically pull images and build containers with
required databases.

*NOTE:* Running tests requires Python 3.6 or higher.


Other SQL Drivers
-----------------

* aiopg_ - asyncio client for PostgreSQL
* aiomysql_ - asyncio client form MySQL


Requirements
------------

* Python_ 3.5+
* pyodbc_
* uvloop_ (optional)


.. _Python: https://www.python.org
.. _asyncio: http://docs.python.org/3.4/library/asyncio.html
.. _pyodbc: https://github.com/mkleehammer/pyodbc
.. _uvloop: https://github.com/MagicStack/uvloop
.. _ODBC: https://en.wikipedia.org/wiki/Open_Database_Connectivity
.. _aiopg: https://github.com/aio-libs/aiopg
.. _aiomysql: https://github.com/aio-libs/aiomysql
.. _PEP492: https://www.python.org/dev/peps/pep-0492/
.. _unixODBC: http://www.unixodbc.org/
.. _threads: http://techspot.zzzeek.org/2015/02/15/asynchronous-python-and-databases/
.. _docker: https://docs.docker.com/engine/installation/
.. _motor: https://emptysqua.re/blog/motor-0-7-beta/
