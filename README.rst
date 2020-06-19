python-jyutping
===============

Python tool to convert Chinese characters to Jyutping.

Install
-------

.. code:: bash

    $ pip install jyutping

Usage
-----

.. code:: python

    >>> import jyutping

    >>> jyutping.get('广东话')  # Python 3
    >>> jyutping.get(u'广东话')  # Python 2
    ['gwong2', 'dung1', 'waa6']

    >>> unk_char = '<UNK>'  # label for unknown characters, default '<UNK>'
    >>> external_dictionary = {
        '燒': 'siu1',
        '臘': 'laap6'
    }
    >>> jyutping.get(
        '广东话',
        external_dictionary=external_dictionary,
        unk_char=unk_char
        )
    ['siu1', 'laap6']
    
Addtional resources
-----------------
1. https://jyut.net/query
2. https://ctext.org/dictionary.pl?if=gb&char=%E3%96%AD


Dependencies
------------
requests, beautifulSoup4