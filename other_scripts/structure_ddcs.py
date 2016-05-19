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
import shutil


for dirpath, dirs, files in os.walk('../TUB'):
    for filename in fnmatch.filter(files, '*.xml'):
        with open('../TUB/'+filename, 'r') as openfile:
            content = openfile.read()
            ddc_r = re.search('<dc:subject>ddc:(.*)</dc:subject>', content)
            if ddc_r:
                ddc = ddc_r.group(1)
                if len(ddc) == 1:
                    ddc = '00' + ddc
                elif len(ddc) == 2:
                    ddc = '0' + ddc
                else:
                    pass

                foldername = '../DDCs/' + ddc + '/'

                if not os.path.exists(os.path.dirname(foldername)):
                    try:
                        os.makedirs(os.path.dirname(foldername))
                    except OSError as exc:  # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise

            lang_r = re.search('<dc:language>(.*)</dc:language>', content)
            if lang_r:
                lang = lang_r.group(1)
                if lang == 'deutsch':
                    lang = 'deu'
                elif lang == 'english' or 'englisch':
                    lang = 'eng'
                else:
                    pass

                newfilename = lang + '_' + filename
                with open(foldername + newfilename, 'w') as newfile:
                    newfile.write(content)

shutil.rmtree('../TUB')
