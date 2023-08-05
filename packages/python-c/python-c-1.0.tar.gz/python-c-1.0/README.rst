python-c
====

A lazy alternative to python -c.

Usage
====

If you have a file named foo.py with::

    def quite():
       return 5
    def loud():
        print 'hello'
    def double(arg):
       return arg*2

Instead of::

  $ python -c "import foo; foo.loud();"
  hello

You can lazily write::

    $ python-c foo 'loud()'
    hello

You can load multiple file::

  $ python-c foo,foo2 'loud()'
  hello

or directories::

  $ python-c ./,./dir1 'loud()'
  hello

In cases where it works, you can maximize your laziness and omit the first argument, the current directory is then loaded::

    $ python-c 'loud()'
    hello

Printing
====

Printing is handled for you::

    $ python-c foo quite()
    5

The result of the call (if any) is printed, even though the function does not call 'print'.

More examples
====

You can pass arguments to your functions::

    $ python-c foo 'double(2)'
    4

You can execute arbitrary code in your single line::

    $ python-c foo '"hot" if double(2) == 4 else "cold"'
    hot

This includes printing::

    $ python-c foo.py 'print "double {} is {}".format(2, double(2))'
    double 2 is 4

Motivation
====
I wrote this tool because I am so lazy that both 'python -c' and https://github.com/vascop/runp still felt like too much typing.
