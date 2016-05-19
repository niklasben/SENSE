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

import os
import fnmatch


deu = {}
eng = {}

for dirpath, dirs, files in os.walk('../DDCs/deu/'):
    for filename in fnmatch.filter(files, 'deu_*.xml'):
        if dirpath[-3:] not in deu.keys():
            deu[dirpath[-3:]] = 1
        else:
            deu[dirpath[-3:]] += 1

with open('deu_temp.txt', 'w') as file_deu_temp:
    for k, v in deu.items():
        file_deu_temp.write(k + '\t' + str(v) + '\n')

with open('deu_temp.txt', 'r') as file_deu_temp,\
 open('deu_ddc.txt', 'w') as file_deu:
    lines = file_deu_temp.read().splitlines()
    lines.sort(key=lambda line: int(line.split()[1]), reverse=True)
    for line in lines:
        file_deu.write(line + '\n')


for dirpath, dirs, files in os.walk('../DDCs/eng/'):
    for filename in fnmatch.filter(files, 'eng_*.xml'):
        if dirpath[-3:] not in eng.keys():
            eng[dirpath[-3:]] = 1
        else:
            eng[dirpath[-3:]] += 1

with open('eng_temp.txt', 'w') as file_eng_temp:
    for k, v in eng.items():
        file_eng_temp.write(k + '\t' + str(v) + '\n')

with open('eng_temp.txt', 'r') as file_eng_temp,\
 open('eng_ddc.txt', 'w') as file_eng:
    lines = file_eng_temp.read().splitlines()
    lines.sort(key=lambda line: int(line.split()[1]), reverse=True)
    for line in lines:
        file_eng.write(line + '\n')


os.remove('deu_temp.txt')
os.remove('eng_temp.txt')
