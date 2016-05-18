# -*- coding: utf-8 -*-
"""
Created on Mon May 09 08:48:44 2016

@author: Niklas
"""

import re
import os
import fnmatch


with open('ddc_all.txt', 'w') as writefile:
    for dirpath, dirs, files in os.walk('TUB'):
        for filename in fnmatch.filter(files, '*.xml'):
            with open('TUB/'+filename, 'r') as openfile:
                line = openfile.read()
                m = re.search('<dc:subject>ddc:(.*)</dc:subject>', line)
                if m:
                    found = m.group(1)
                    if len(found) == 1:
                        found = '00' + found
                        print found
                    elif len(found) == 2:
                        found = '0' + found
                        print found
                    else:
                        pass
                    writefile.write(found + '\n')
