===============================
asyncio-utils
===============================


.. image:: https://img.shields.io/pypi/v/asyncio_utils.svg
        :target: https://pypi.python.org/pypi/asyncio_utils

.. image:: https://img.shields.io/travis/m-housh/asyncio-utils.svg
        :target: https://travis-ci.org/m-housh/asyncio-utils

.. image:: https://coveralls.io/repos/github/m-housh/asyncio-utils/badge.svg?branch=master
    :target: https://coveralls.io/github/m-housh/asyncio-utils?branch=master


Asyncio utilities for python >= 3.6

A small package of utilities that mimics some builtin methods, but in an 
asynchronous fashion.


* Free software: MIT license


Features
--------

* Asyncio utilities

Install
-------

To install::

    pip install asyncio-utils

Usage
------

Almost everything is used with the ``await`` keyword before unless marked
otherwise.  However most of the method inputs can be ``awaitable`` (but not
actually awaited yet) and they will still work, unless marked otherwise.

To run any of the examples::

    import asyncio
    loop = asyncio.get_event_loop()


aiter
--------------

Wraps/ensures an ``AsyncIterator``.  

If the input is ``Awaitable``, then we will ``await`` the result, and check
if it returns and ``AsyncIterator``.

If the input is an ``async generator`` that was not called, then we will
call it and yield it's values.

Else if the input is an ``iterator`` we iterate it and yield the values.


Examples::

    >>> async def main():
        async for v in aiter2(range(1, 5)):  # normal iterator
            print(v)

    >>> loop.run_until_complete(main())
    1
    2
    3
    4

    >>> async def main():
            async for v in aiter2(arange(1, 5)):  # not awaited
                print(v)

    >>> loop.run_until_complete(main())
    1
    2
    3
    4

    >>> async def main():
            async for v in aiter2(await arange(1, 5)):  # awaited works
                print(v)

    >>> loop.run_until_complete(main())
    1
    2
    3
    4

    >>> async def agen():
            yield 1
            yield 2
            yield 3
            yield 4

    >>> async def main():
            async for v in aiter2(agen):  # oops forgot to call it
                print(v)

    >>> loop.run_until_complete(main())
    1
    2
    3
    4



anext
-----------------

Mimics the builtin ``next`` method.  This method will not accept an 
``awaitable``.  The input must be an ``AsyncIterator`` or you will get a 
``TypeError``.

Example::  

    >>> async def main():
        myrange = await arange(1, 5)
        for n in range(1, 5):
            print(n, n == await anext(myrange))
        try:
            n = await anext(myrange)
            print("This should not be shown")
        except StopAsyncIteration:
            print('Sorry no more values!')

    >>> loop.run_until_complete(main())
    1 True
    2 True
    3 True
    4 True
    Sorry no more values!


Example of using a default value if a ``StopAsyncIteration`` has occured::

    >>> async def main():
        myrange = await arange(1)
        print(await anext(myrange))
        print(await anext(myrange, 'Sorry no more values!'))
        # or as kwarg
        print(await anext(myrange, default='Still no more values!'))

    >>> loop.run_until_complete(main())
    1
    Sorry no more values!
    Still no more values!


Example failure because a non ``AsyncIterator`` passed in::  

    >>> async def main():
            val = await anext(arange(1, 5))
            print(val)  # never get here

    >>> loop.run_until_complete(main())
    Traceback (most recent call last):
    ...
    TypeError: Not an AsyncIterator: <coroutine object arange at 0x1068170f8>


amap
--------------

``AsyncGenerator`` that mimics the builtin ``map`` method.

.. note::
    You do not use ``await`` on ``AsyncGenerator``'s

Example::  

    >>> async def main():
            async for val in amap('${}'.format, arange(1, 5)):
                print(val)

    >>> loop.run_until_complete(main())
    $1
    $2
    $3
    $4

This also works if the function passed in is a coroutine::

    >>> async def formatter(val):
            return f'${val}'

    >>> async def main():
            async for val in amap(formatter, arange(1, 5)):
                print(val)

    >>> loop.run_until_complete(main())
    $1
    $2
    $3
    $4

afilter
---------------

An ``async generator`` that mimics the builtin ``filter`` method.

Example::

    >>> async def main():
            myfilter = await afilter(lambda x: x == 2, arange(1, 5))
            print(await anext(myfilter, 'Oops no more twos'))
            print(await anext(myfilter, 'Oops no more twos'))

    >>> loop.run_until_complete(main())
    2
    Oops no more twos


arange
---------------------

Mimics the builtin ``range`` method.  Returning an ``AsyncIterator``.

Example::  

    >>> async def main():
            myrange = await arange(1, 5)
            async for n in myrange:
                print(n)

    >>> loop.run_until_complete(main())
    1
    2
    3
    4


alist
------------------

Transform an ``AsyncIterator`` to a list. This would be equivalent to::  

    [v async for v in async_iterator]

However we ensure that the ``async_iterator`` is actually an ``AsyncIterator``.

Example::  

    >>> async def main():
            print(await alist(arange(1, 5)))
            # or
            print(await alist(await arange(1, 5)))

    >>> loop.run_until_complete(main())
    [1, 2, 3, 4]
    [1, 2, 3, 4]


atuple
-----------------

Transform an ``AsyncIterator`` to a ``tuple``. This would be equivalent to::  

    tuple([v async for v in async_iterator])

However we ensure that the ``async_iterator`` is actually an ``AsyncIterator``.

Example::  

    >>> async def main():
            print(await atuple(arange(1, 5)))
            # or
            print(await atuple(await arange(1, 5)))

    >>> loop.run_until_complete(main())
    (1, 2, 3, 4)
    (1, 2, 3, 4)


aset
-------------

Transform an ``AsyncIterator`` to a ``set``. This would be equivalent to::  

    {v async for v in async_iterator}

However we ensure that the ``async_iterator`` is actually an ``AsyncIterator``.

Example::  

    >>> async def main():
            print(await aset(arange(1, 5)))
            # or
            print(await aset(await arange(1, 5)))

    >>> loop.run_until_complete(main())
    {1, 2, 3, 4}
    {1, 2, 3, 4}


adict
-----------

Transform an ``AsyncIterator`` to a ``dict``. This would be equivalent to::  

    {k: v async for (k, v) in async_iterator}

However we ensure that the ``async_iterator`` is actually an ``AsyncIterator``.

Example::  

    >>> async def k_v_gen():
            async for n in await arange(1, 5):
                yield (n, n * 2)

    >>> async def main():
            print(await adict(k_v_gen()))

    >>> loop.run_until_complete(main())
    {1: 2, 2: 4, 3: 6, 4: 8}


transform_factory
-----------------

This can be used to transform an ``AsyncIterator`` into any callable.  This is
the base for ``alist``, ``aset``, ``atuple``, and ``adict``.  While not tested,
in theory, you should be able to transform it into the output of any 
``callable`` that takes a standard iterator.


Example of how the ``alist`` method is declared in the code::  

    >>> import functools
    >>> alist = functools.partial(transform_factory, _type=list)
    >>> alist.__doc__ = """Async list documentation."""

    >>> async def main():
            print(await alist(arange(1, 5)))

    >>> loop.run_until_complete(main())
    [1, 2, 3, 4]


make_async
-----------------

Make's any callable awaitable.  Can be used as a decorator.

Example::

    >>> class AClass(object):

            def __init__(self):
                self.a = 'a'

    >>> async_aclass = make(async_aclass)

    # or as a decorator
    >>> @make_async
        def sync_a():
            return 'a'

    >>> async def main():
            async_a = await async_aclass()
            print(async_a.a == 'a')

            print(await sync_a())
            
