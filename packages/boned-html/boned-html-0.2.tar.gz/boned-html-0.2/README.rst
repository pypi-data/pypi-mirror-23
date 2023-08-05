|logo| boned-html
##################

|pypi| |travis| |coveralls|

Boned html is a small python library.

It helps you extract text from an html (in the form of a lxml tree),
process this text, to classify it,
reinject text in the html with specific css classes.

The typical use is for anotating an html with classes.
For example you are categorizing text,
and you want the user to visualize those categories on the original html.

The text will be extracted in a smart way:
it won't stop at semantic tags (`<i>`, `<em>`, etc.)
but at other tags (`<h1>`, `<p>`, etc.).

As you reinject the text, semantic tags will be added back to text,
and general html layout will be respected.

.. |logo| image:: ./images/boned-html-64.png

.. |pypi| image:: http://img.shields.io/pypi/v/boned-html.svg?style=flat
    :target: https://pypi.python.org/pypi/boned-html
.. |travis| image:: http://img.shields.io/travis/jurismarches/boned-html/master.svg?style=flat
    :target: https://travis-ci.org/jurismarches/boned-html
.. |coveralls| image:: http://img.shields.io/coveralls/jurismarches/boned-html/master.svg?style=flat
    :target: https://coveralls.io/r/jurismarches/boned-html

Installation
============

::

  pip install boned-html

Usage
=====

The fonctionalities are provided by the class `boned_html.Chunker`__ with methods:

* `chunk_tree` to get text chunks from an lxml tree.
* `unchunk` to put back chunks together providing css classes for pieces of text.

.. __: ./boned_html/chunker.py



A quick example: imagine we have a function to detect a tel number value in a sentence::

   >>> import re
   >>> from itertools import cycle
   >>> def get_tel(text):
   ...    splits = re.split(r"(\+?(?:\d\s*){8,13})", text)
   ...    return list(zip(splits, cycle([None, "tel"])))
   >>> get_tel("call +33 00 00 00 00")
   [('call ', None), ('+33 00 00 00 00', 'tel'), ('', None)]

And an html::

   >>> html = '''
   ... <html>
   ...   <head><title>call +33 00 00 00 00</title></head>
   ...   <body>
   ...     <p>To get an operator <em>call</em></p>
   ...     <p><b>call</b> <em>(country) +33</em> 00 00 00 00</p>
   ...   </body>
   ... </html>
   ... '''

We chunk::

   >>> import lxml.html
   >>> from boned_html import HtmlBoner
   >>> tree = lxml.html.fromstring(html)
   >>> boned = HtmlBoner(tree)

We evaluate each text and assign "tel" class to it if there is a telephone::

   >>> for i, text in enumerate(boned):
   ...     if text is not None:
   ...         boned.set_classes(i, get_tel(text))

We now rebuild the tree::

   >>> boned.tree
   <Element html ...>
   >>> print(boned)
   <html>
     <head><title>call +33 00 00 00 00</title></head>
     <body>
       <p>To get an operator <em>call</em></p>
       <p><b>call</b> <em>(country) </em><span class="tel" id="chunk-6-1"><em>+33</em> 00 00 00 00</span></p>
     </body>
   </html>

We have a specific span around our number,
also opening and closure of `em` tag was handled,
and phone number in `head/title` remains the same.
