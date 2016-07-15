================
argparse-oappend
================

Provides ``oappend`` action for `argparse`_ that works almost like `append`_,
but skips the default list if the user gives any value for the option.

See `issue 16399`_ for a discussion.

.. _argparse: https://docs.python.org/3/library/argparse.html
.. _append: https://docs.python.org/3/library/argparse.html#action
.. _issue 16399: https://bugs.python.org/issue16399

Example
=======

You may import ``OverrideAppendAction`` and register it with a parser or use the
provided parser:

.. code:: python

    from oappend import OverrideAppendArgumentParser

    parser = OverrideAppendArgumentParser()
    parser.add_argument('-n', action='oappend', type=int, default=[1, 2])
    args = parser.parse_args(['-n3', '-n4'])  # Namespace(n=[3, 4])

With the standard ``append`` action the option would be set to
``[1, 2, 3, 4]``, combining your default with user choices.

Installation
============

.. code:: bash

    pip3 install argparse-oappend
