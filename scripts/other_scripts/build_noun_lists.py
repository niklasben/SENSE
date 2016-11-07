# -*- coding: utf-8 -*-
"""Docstring."""

import re
import os
import fnmatch
import json
from pattern.de import parse, split, pprint, tag
import sys


# Set default encoding to UTF-8
reload(sys)
sys.setdefaultencoding('utf-8')


def buildWordList():
    """
    Function to build lists and dictionaries.

    Function exports txt-files incl. dictionaries and lists from both DDC for
    the words that are tagged as NE and NN.
    """

    # Defining list variables
    list330NE = []
    list330NN = []
    list710NE = []
    list710NN = []

    # Defining dictionary variables
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
                    word = word.decode('utf-8')
                    if ddcFromFilepath == '330':
                        # print ddcFromFilepath + '\t' + word
                        if postag == 'NN':
                            list330NN.append(word)
                            if word not in dict330NN.keys():
                                dict330NN[word] = 1
                            elif word in dict330NN.keys():
                                dict330NN[word] += 1
                            else:
                                pass
                        elif postag == 'NE':
                            list330NE.append(word)
                            if word not in dict330NE.keys():
                                dict330NE[word] = 1
                            elif word in dict330NE.keys():
                                dict330NE[word] += 1
                            else:
                                pass
                        else:
                            pass
                    elif ddcFromFilepath == '710':
                        # print ddcFromFilepath + '\t' + word
                        if postag == 'NN':
                            list710NN.append(word)
                            if word not in dict710NN.keys():
                                dict710NN[word] = 1
                            elif word in dict710NN.keys():
                                dict710NN[word] += 1
                            else:
                                pass
                        elif postag == 'NE':
                            list710NE.append(word)
                            if word not in dict710NE.keys():
                                dict710NE[word] = 1
                            elif word in dict710NE.keys():
                                dict710NE[word] += 1
                            else:
                                pass
                        else:
                            pass

    with open('../../collecting/dict330NE.txt', 'w') as exportfile330NE:
        json.dump(dict330NE, exportfile330NE, sort_keys=True, indent=4,
                  separators=(',', ': '))

    with open('../../collecting/dict330NN.txt', 'w') as exportfile330NN:
        json.dump(dict330NN, exportfile330NN, sort_keys=True, indent=4,
                  separators=(',', ': '))

    with open('../../collecting/dict710NE.txt', 'w') as exportfile710NE:
        json.dump(dict710NE, exportfile710NE, sort_keys=True, indent=4,
                  separators=(',', ': '))

    with open('../../collecting/dict710NN.txt', 'w') as exportfile710NN:
        json.dump(dict710NN, exportfile710NN, sort_keys=True, indent=4,
                  separators=(',', ': '))


buildWordList()  # Call function buildWordList
