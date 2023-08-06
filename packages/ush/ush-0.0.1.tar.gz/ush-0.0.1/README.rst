.. vim: ft=doctest
ush - unix shell DSL for python
===============================

This library implements an idiomatic unix shell DSL for python. Its main goal is
to transform python into a perfect replacement for /bin/bash for writing complex
shell scripts.

Examples:

>>> import ush
>>> sh = ush.Shell()
