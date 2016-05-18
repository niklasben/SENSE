# -*- coding: utf-8 -*-
"""
Created on Mon May 09 08:48:44 2016

@author: Niklas
"""

import operator


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
