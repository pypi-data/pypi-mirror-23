
.. code-block:: python
   :emphasize-lines: 26,29

=======================
Forbes Quote of the Day
=======================

As many of you seen Forbes Quote of the day when you open Forbes website.
This package provides a way to get quote and its author.

------------
Installation
------------

Install it by pip::
    
    pip install forbesqotd

-----
Usage
-----

Package has two methods which returns quote and its author::

    from forbesqotd import forbes
    app = forbes()
    quote = forbes.get_quote()
    author = forbes.get_by()

