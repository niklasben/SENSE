# -*- coding: utf
"""Docstring."""

import re
import os
import fnmatch
from pattern.de import parse, split, pprint, tag
from pprint import pprint


def buildWordList():
    """Docstring."""

    list330NE = []
    list330NN = []
    list710NE = []
    list710NN = []

    dict330NE = {}
    dict330NN = {}
    dict710NE = {}
    dict710NN = {}

    for dirpath, dirs, files in os.walk('../../collecting/temp/'):
        for filename in fnmatch.filter(files, '*.txt'):
            with open('../../collecting/temp/' + dirpath + '/' + filename,
                      'r') as openfile:

                parsefile = openfile.read()
                # parsefile = parse(parsefile)

                ddcFromFilepath = dirpath[-3:]

                for word, postag in tag(parsefile, tagset="STTS"):
                    if ddcFromFilepath == '330':
                        print ddcFromFilepath + '\t' + word
                    # if postag == 'NN':
                    #     if word not in dictNN.keys():
                    #         dictNN[word] = 1
                    #     elif word in dictNN.keys():
                    #         dictNN[word] += 1
                    #     else:
                    #         pass
                    # elif postag == 'NE':
                    #     if word not in dictNE.keys():
                    #         dictNE[word] = 1
                    #     elif word in dictNE.keys():
                    #         dictNE[word] += 1
                    #     else:
                    #         pass
                    # else:
                    #     pass










                # ddcFromFilepath = dirpath[-3:]
                # if ddcFromFilepath == '330':
                #     pass
                # elif ddcFromFilepath == '710':
                #     pass
                # else:
                #     print 'Irgendeine DDC die nicht da sein dürfte'


buildWordList()
