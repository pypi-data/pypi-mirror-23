Fwipy - Python Wrapper for Content Player Socket Operations
===========================================================

.. code-block:: python

    >>> from fwipy import Player

    >>> player = Player(host='127.0.0.1',
                port=10561,
                username='admin',
                password='fourwinds')

    >>> player.set_variable('foo', 'bar')


