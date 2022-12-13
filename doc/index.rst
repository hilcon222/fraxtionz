.. Fraxtionz documentation master file, created by
   sphinx-quickstart on Sat Aug  6 12:14:40 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

warning the navigation bar is useless and not working, but not removable.


Welcome to Fraxtionz's documentation!
=====================================

"Why Fraxtionz?"

Fraxtionz is an useful library to manage rational numbers with more precision. It is very useful because it correctly computes periodic numbers, when Python aproximates them.

>>> 1/3
0.3333333333333333

That isn't correct. The correct result would be 0.3 periodic, not 0.3333333333333333 with exactly 16 decimal digits.
Well, Fraxtionz permits you to avoid this problem. Floating-point numbers are in most cases unexact. However, the numerator and a denominator of a fractions are natural numbers, if the fractions are rational.
Therefore, because an int can be much more precise, the fraction will be exact!!!

>>> from fraxtionz import Rational
>>> f = Rational(1, 3)
>>> f + f + f == Rational(1)
True
>>> Rational(3, 3).floatdump()
1.0

Documentation of the Fraxtionz module
=====================================

.. automodule:: fraxtionz
   :members:
   :undoc-members:
   :show-inheritance:
