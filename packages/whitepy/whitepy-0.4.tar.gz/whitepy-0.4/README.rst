whitepy
=======

|Build Status|

Whitespace interpreter written in Python3 for my final Open University
project (TM470)

Install and Usage
~~~~~~~~~~~~~~~~~

Once installed, run ``whitepycli`` with a whitespace source file as an
argument.

Using pip
'''''''''

.. code:: shell

    $ pip install whitepy
    $ whitepycli --help
    Usage: whitepycli [OPTIONS] FILENAME

      Whitespace Interpreter

    Options:
      --debug / --no-debug  Enable Debug
      --help                Show this message and exit.
      
    $ whitepycli sample_ws/helloworld.ws 
    Hello, World!

From Github
'''''''''''

.. code:: shell

    $ git clone https://github.com/yasn77/whitepy && cd whitepy
    $ pip install -r requirements.txt
    $ ./whitepycli --help
    Usage: whitepycli [OPTIONS] FILENAME

      Whitespace Interpreter

    Options:
      --debug / --no-debug  Enable Debug
      --help                Show this message and exit.
      
    $ ./whitepycli sample_ws/helloworld.ws 
    Hello, World!

What is Whitespace?
~~~~~~~~~~~~~~~~~~~

Whitespace programming language was originally created by Edwin Brady
and Chris Morris at the University of Durham[1], then gained wider
exposure when it was reviewed[2] April 1st 2003 on
`Slashdot <https://slashdot.org>`__ website.

Originally developed as a bit of fun, Whitespace is an attempt to have a
programming language that uses characters that are usually ignored by
other programming languages, namely ``space`` (ASCII 32),
``tab``\ (ASCII 9) and ``linefeed``\ (ASCII 10). The by-product being
that you could implement Whitespace code in other text (making it
possible to write a polygot computer program).

How to write Whitespace?
~~~~~~~~~~~~~~~~~~~~~~~~

Whitespace is an imperative stack based language, with 5 basic commands
known as *Instruction Imperative Parameter* (IMP):

+--------------------+----------------------+
| IMP                | Meaning              |
+====================+======================+
| ``[Space]``        | Stack Manipulation   |
+--------------------+----------------------+
| ``[Tab][Space]``   | Arithmetic           |
+--------------------+----------------------+
| ``[Tab][Tab]``     | Heap access          |
+--------------------+----------------------+
| ``[LF]``           | Flow Control         |
+--------------------+----------------------+
| ``[Tab][LF]``      | I/O                  |
+--------------------+----------------------+

The full list of IMP with commands can be found in the Whitespace
tutorial[3]. The original tutorial is no longer available, but can be
accessed using `Internet Archive: Wayback
machine <http://archive.org/web/>`__.

One of the biggest difficulties in writing Whitespace is that the source
code isn't immediately visible in most editors. To get around this, many
editors have the ability to represent Whitespace characters as some
other character. For example, in ``vim`` you can use
``:set listchars=...`` and ``:set list``.

whitepy Implementation
~~~~~~~~~~~~~~~~~~~~~~

Lexer (```lexer.py`` <whitepy/lexer.py>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The whitepy lexerical analysis relies on
```lexerconstants.py`` <whitepy/lexerconstants.py>`__, which contains
valid IMP that can be used and their valid arguments also other
definitions, such as integer representation. These are taken from the
`original whitespace
tutorial <https://web.archive.org/web/20030414001723/http://compsoc.dur.ac.uk:80/whitespace/tutorial.php>`__.

The lexer takes the whitespace code as an input
(``lexer.Lexer(line=lines)``) and when the method
``lexer.get_all_tokens()`` is called, a list of tokens and arguments is
created from the whitespace source file. These tokens are stored in the
lexer object and can be retrieved by calling ``lexer.tokens``.

Tokenisation process is handled by
```ws_token.py`` <whitepy/ws_token.py>`__.

Tokeniser (```ws_token.py`` <whitepy/ws_token.py>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The engine that drives the Tokeniser is Pythons ``re`` library,
specifically ``re.Scanner``. This is a powerful library that can easily
allow splitting of text in to the required tokens. Documentation for
``re.Scanner`` is not extensive and can be found under section
``6.2.5.9`` of `Python ``re``
documentation <https://docs.python.org/3.2/library/re.html#writing-a-tokenizer>`__,
however I found some really helpful documentation and examples
`here <http://lucumr.pocoo.org/2015/11/18/pythons-hidden-re-gems/>`__.

Parser (```parser.py`` <whitepy/parser.py>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once lexical analysis is complete, it is now possible to parse the list
of tokens and execute accordingly. At the heart of the parser is a token
to method map (``parser.method_map``), this is a ``dict`` structure that
maps tokens to internal methods. I believe this approach helps me to
extend the interpreter with possibly my own token implementations and
reduces the size of the ``parser.parse()`` method. This is because it
reduces the amount of logic required in ``parser.parse()`` and instead
the method simply looks up keys in a ``dict``.

Helpful links
~~~~~~~~~~~~~

The following is a list of sites/references I have used to help me
develop ``whitepy``:

+--------------------------------------+--------------------------------------+
| Title                                | Link                                 |
+======================================+======================================+
| Writing Compilers and Interpreters:  | https://www.amazon.co.uk/Writing-Com |
| A Software Engineering Approach by   | pilers-Interpreters-Software-Enginee |
| Ronald Mak                           | ring-ebook/dp/B004S82O40)            |
+--------------------------------------+--------------------------------------+
| Whitspace Language Tutorial          | https://h0tsh0tt.wordpress.com/2016/ |
|                                      | 07/03/whitespace-language-tutorial/  |
+--------------------------------------+--------------------------------------+
| Whitespace (Wikipedia)               | https://en.wikipedia.org/wiki/Whites |
|                                      | pace\_(programming\_language)        |
+--------------------------------------+--------------------------------------+
| Interpreter Collection for the       | https://github.com/hostilefork/white |
| Whitespace Language                  | spacers/                             |
+--------------------------------------+--------------------------------------+
| Online Whitespace Compiler, virtual  | https://github.com/vii5ard/whitespac |
| machine and IDE                      | e                                    |
+--------------------------------------+--------------------------------------+
| Let's build a simple interpreter     | https://ruslanspivak.com/lsbasi-part |
|                                      | 1/                                   |
+--------------------------------------+--------------------------------------+
| Python ``re`` module used for        | http://lucumr.pocoo.org/2015/11/18/p |
| tokenising                           | ythons-hidden-re-gems/               |
+--------------------------------------+--------------------------------------+
| Let's build a compiler               | http://compilers.iecc.com/crenshaw/  |
+--------------------------------------+--------------------------------------+
| Notes on how Parsers and Compilers   | http://parsingintro.sourceforge.net/ |
| work                                 |                                      |
+--------------------------------------+--------------------------------------+

References
~~~~~~~~~~

[1]
https://web.archive.org/web/20030412201917/http://compsoc.dur.ac.uk:80/whitespace/

[2]
https://developers.slashdot.org/story/03/04/01/0332202/New-Whitespace-Only-Programming-Language

[3]
https://web.archive.org/web/20030414001723/http://compsoc.dur.ac.uk:80/whitespace/tutorial.php

.. |Build Status| image:: https://travis-ci.org/yasn77/whitepy.svg?branch=master
   :target: https://travis-ci.org/yasn77/whitepy
