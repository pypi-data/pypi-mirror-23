===============================
Pykemon
===============================

A python wrapper for `PokeAPI <http://pokeapi.co>`_

This is remade from (the original Pykemon)[https://github.com/PokeAPI/pykemon] due to it not being compatible with Python 3.0 or higher, it still works the same though.

This api wrapper is currently for the V1 API, soon I'll update it to V2

* Free software: BSD license
* Documentation: http://pykemon.rtfd.org.


Installation
------------

Nice and simple:

.. code-block:: bash

    $ pip install pykemon2.0


Usage
-----

Even simpler:

.. code-block:: python

    >>> import pykemon
    >>> client = pykemon.V1Client()
    >>> p = client.get_pokemon(uid=1)
    [<Pokemon - Bulbasaur>]


Features
--------

* Generate Python objects from PokeAPI resources.

* Human-friendly API