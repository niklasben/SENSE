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

import errno
import fnmatch
import os
import re
import mmap
import shutil

for dirpath, dirs, files in os.walk('../DDCs/deu'):
    for filename in fnmatch.filter(files, '*.xml'):

        foldername = '../temp/temp_' + dirpath[-3:] + '/'
        newfilename = filename[11:-4] + '.txt'

        with open(dirpath + '/' + filename, 'r') as openfile:
            s = mmap.mmap(openfile.fileno(), 0, access=mmap.ACCESS_READ)
            if s.find('<dc:description xml:lang="deu">') != -1:
                line = openfile.read()
                start = line.index('<dc:description xml:lang="deu">') + len('<dc:description xml:lang="deu">')
                end = line.index('</dc:description>', start)

                foldername = '../temp/temp_' + dirpath[-3:] + '/'

                if not os.path.exists(os.path.dirname(foldername)):
                    try:
                        os.makedirs(os.path.dirname(foldername))
                    except OSError as exc:  # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise

            newfilename = filename[11:-4] + '.txt'
            with open(foldername + newfilename, 'w') as newfile:
                newfile.write(line[start:end])


for dirpath, dirs, files in os.walk('../temp'):
    with open('../temp/test_' + dirpath[-3:] + '.txt', 'w') as writefile:
        for filename in fnmatch.filter(files, '*.txt'):
            with open(dirpath + '/' + filename, 'r') as openfile:
                line = openfile.read()
            writefile.write(line + '\n\n')


# shutil.rmtree('../temp')
