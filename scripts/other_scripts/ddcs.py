# -*- coding: utf-8 -*-
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

openfile = open('ddc_all.txt', 'r')
writefile = open('ddc_count.txt', 'w')

ddcs = {}

for line in openfile:
    line = line.strip()

    if line not in ddcs.keys():
        ddcs[line] = 1
    else:
        ddcs[line] += 1

for key, value in sorted(ddcs.iteritems()):
    writefile.write(key + '\t' + str(value) + '\n')
