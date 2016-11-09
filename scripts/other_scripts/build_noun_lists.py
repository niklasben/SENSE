# -*- coding: utf-8 -*-
"""Docstring."""

import os
import fnmatch
import json
from pattern.de import parse, split, pprint, tag, parsetree, singularize
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
    list330 = []
    list710NE = []
    list710NN = []
    list710 = []

    # Defining dictionary variables
    dict330NE = {}
    dict330NN = {}
    dict330 = {}
    dict330WithoutCommons = {}
    dict710NE = {}
    dict710NN = {}
    dict710 = {}
    dict710WithoutCommons = {}

    for dirpath, dirs, files in os.walk('../../collecting/temp/'):
        for filename in fnmatch.filter(files, '*.txt'):
            with open('../../collecting/temp/' + dirpath + '/' + filename,
                      'r') as openfile:

                parsefile = openfile.read()
                # parsefile = parse(parsefile)

                ddcFromFilepath = dirpath[-3:]

                for word, postag in tag(parsefile, tagset='STTS'):
                    word = word.decode('utf-8')

                    if ddcFromFilepath == '330':
                        if postag == 'NN':

                            singularForm = singularize(word)

                            if word == singularForm:
                                pass
                            else:
                                word = singularForm

                            list330NN.append(word)
                            list330.append(word)

                            if word not in dict330NN.keys():
                                dict330NN[word] = 1
                            elif word in dict330NN.keys():
                                dict330NN[word] += 1
                            else:
                                pass

                        elif postag == 'NE':

                            singularForm = singularize(word)

                            if word == singularForm:
                                pass
                            else:
                                word = singularForm

                            list330NE.append(word)
                            list330.append(word)

                            if word not in dict330NE.keys():
                                dict330NE[word] = 1
                            elif word in dict330NE.keys():
                                dict330NE[word] += 1
                            else:
                                pass
                        else:
                            pass

                    elif ddcFromFilepath == '710':
                        if postag == 'NN':

                            singularForm = singularize(word)

                            if word == singularForm:
                                pass
                            else:
                                word = singularForm

                            list710NN.append(word)
                            list710.append(word)

                            if word not in dict710NN.keys():
                                dict710NN[word] = 1
                            elif word in dict710NN.keys():
                                dict710NN[word] += 1
                            else:
                                pass

                        elif postag == 'NE':

                            singularForm = singularize(word)

                            if word == singularForm:
                                pass
                            else:
                                word = singularForm

                            list710NE.append(word)
                            list710.append(word)

                            if word not in dict710NE.keys():
                                dict710NE[word] = 1
                            elif word in dict710NE.keys():
                                dict710NE[word] += 1
                            else:
                                pass
                        else:
                            pass

                    else:
                        pass

    # Building list with words common in both DDCs
    listCommonWords = list(set(list330).intersection(list710))

    # Building new lists without the common words
    list330WithoutCommons = []
    list710WithoutCommons = []

    for i in list330:
        if i not in listCommonWords:
            list330WithoutCommons.append(i)

    for i in list710:
        if i not in listCommonWords:
            list710WithoutCommons.append(i)

    # Building new dictionaries without the common words
    for i in list330WithoutCommons:
        if i not in dict330WithoutCommons.keys():
            dict330WithoutCommons[i] = 1
        elif i in dict330WithoutCommons.keys():
            dict330WithoutCommons[i] += 1
        else:
            pass

    for i in list710WithoutCommons:
        if i not in dict710WithoutCommons.keys():
            dict710WithoutCommons[i] = 1
        elif i in dict710WithoutCommons.keys():
            dict710WithoutCommons[i] += 1
        else:
            pass

    # Merge NE and NN dictionaries into one dictionary
    dict330.update(dict330NE)
    dict330.update(dict330NN)
    dict710.update(dict710NE)
    dict710.update(dict710NN)

    # Dump dictionaries into JSON files
    with open('../../collecting/dict330NE.txt', 'w') as exportfile330NE:
        json.dump(dict330NE, exportfile330NE, sort_keys=True, indent=4,
                  separators=(',', ': '))

    with open('../../collecting/dict330NN.txt', 'w') as exportfile330NN:
        json.dump(dict330NN, exportfile330NN, sort_keys=True, indent=4,
                  separators=(',', ': '))

    with open('../../collecting/dict330WithoutCommons.txt', 'w') as\
            exportfile330WithoutCommons:
        json.dump(dict330WithoutCommons, exportfile330WithoutCommons,
                  sort_keys=True, indent=4, separators=(',', ': '))

    with open('../../collecting/dict330All.txt', 'w') as exportfile330All:
        json.dump(dict330, exportfile330All, sort_keys=True, indent=4,
                  separators=(',', ': '))

    with open('../../collecting/dict710NE.txt', 'w') as exportfile710NE:
        json.dump(dict710NE, exportfile710NE, sort_keys=True, indent=4,
                  separators=(',', ': '))

    with open('../../collecting/dict710NN.txt', 'w') as exportfile710NN:
        json.dump(dict710NN, exportfile710NN, sort_keys=True, indent=4,
                  separators=(',', ': '))

    with open('../../collecting/dict710WithoutCommons.txt', 'w') as\
            exportfile710WithoutCommons:
        json.dump(dict710WithoutCommons, exportfile710WithoutCommons,
                  sort_keys=True, indent=4, separators=(',', ': '))

    with open('../../collecting/dict710All.txt', 'w') as exportfile710All:
        json.dump(dict710, exportfile710All, sort_keys=True, indent=4,
                  separators=(',', ': '))

# Call function buildWordList
buildWordList()
