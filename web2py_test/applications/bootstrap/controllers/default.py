# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# -------------------------------------------------------------------------
from pattern.de import parse, split, pprint, tag, parsetree, singularize
from pprint import pprint
from itertools import izip
import os
import json
import math
import sys


# Set default encoding to UTF-8
reload(sys)
sys.setdefaultencoding('utf-8')

# Set global variable for the path of this module
moduledir = os.path.dirname(os.path.abspath('__file__'))


def loadDDCDicts():
    """Function to build Dictionaries for DDCs from Files."""
    # Defining variable for path to JSON-files
    filepath = os.path.join(request.folder, 'static/json/')

    # DDC 330 with all words
    with open(filepath + 'dict330All.json', 'r') as readDict330All:
        dict330All = json.load(readDict330All)

    # DDC 330 without common used words of all DDCs
    with open(filepath + 'dict330WithoutCommons.json', 'r') as readDict330WC:
        dict330WC = json.load(readDict330WC)

    # DDC 330 only NE tagged words
    with open(filepath + 'dict330NE.json', 'r') as readDict330NE:
        dict330NE = json.load(readDict330NE)

    # DDC 330 only NN tagged words
    with open(filepath + 'dict330NN.json', 'r') as readDict330NN:
        dict330NN = json.load(readDict330NN)

    # DDC 710 with all words
    with open(filepath + 'dict710All.json', 'r') as readDict710All:
        dict710All = json.load(readDict710All)

    # DDC 710 without common used words of all DDCs
    with open(filepath + 'dict710WithoutCommons.json', 'r') as readDict710WC:
        dict710WC = json.load(readDict710WC)

    # DDC 710 only NE tagged words
    with open(filepath + 'dict710NE.json', 'r') as readDict710NE:
        dict710NE = json.load(readDict710NE)

    # DDC 710 only NN tagged words
    with open(filepath + 'dict710NN.json', 'r') as readDict710NN:
        dict710NN = json.load(readDict710NN)

    return dict330All, dict330WC, dict330NE, dict330NN, dict710All, dict710WC,\
        dict710NE, dict710NN


def defineSubmissionForm():
    """Function to build the Submission Form."""
    form = SQLFORM(db.dbInput)
    form.element(_type='submit')['_class'] = 'btn btn-default btn-sm'
    form.element('input[type=submit]',
                 replace=lambda button: CAT(button,
                                            INPUT(_class='btn btn-warning\
                                                          btn-sm',
                                                  _type='reset',
                                                  _value=T('Reset'))
                                            )
                 )
    if form.process().accepted:
        response.flash = T('form accepted')
    elif form.errors:
        response.flash = T('form has errors')
    else:
        response.flash = T('please fill out the form')

    returnSubmissionForm = dict(form=form)
    return returnSubmissionForm


def getLastEntryInputDB():
    """Function to get the last Entry from the Database InputDb."""
    inputDatabase = SQLFORM(db.dbInput)
    queryLastEntry = db.executesql('select id, inputTitle,\
                                    inputText from dbInput')

    lastEntry = queryLastEntry[-1]
    lastID = queryLastEntry[-1][0]
    lastTitel = queryLastEntry[-1][1]
    lastTitel = lastTitel.encode('utf-8')
    lastText = queryLastEntry[-1][2]
    lastText = lastText.encode('utf-8')

    return lastID, lastTitel, lastText


def insertTagsToParsedDB(lastID, lastTitel, lastText):
    """Function to process the input, POS-tag it and write it in the
    DB dbparsedText."""
    parsedDatabase = SQLFORM(db.dbParsedText)
    inputDatabase = SQLFORM(db.dbInput)

    dictNN = {}
    dictNE = {}

    # SQL Query to extract ID, Title and Text
    extractQueryInputDB = db.executesql('select id, inputTitle, inputText\
                                        from dbInput')
    lastText = extractQueryInputDB[-1][-1]

    # Begin of For-Loop for POS-Tagging
    for word, postag in tag(lastText, tagset='STTS'):
        word = word.decode('utf-8')

        if postag == 'NN':

            singularFormNN = singularize(word)

            if word == singularFormNN:
                pass
            else:
                word = singularFormNN

            if word not in dictNN.keys():
                dictNN[word] = 1
            elif word in dictNN.keys():
                dictNN[word] += 1
            else:
                pass

        elif postag == 'NE':

            singularFormNE = singularize(word)

            if word == singularFormNE:
                pass
            else:
                word = singularFormNE

            if word not in dictNE.keys():
                dictNE[word] = 1
            elif word in dictNE.keys():
                dictNE[word] += 1
            else:
                pass
        else:
            pass

    listNN = dictNN.items()
    listNE = dictNE.items()

    # for key, value in dict710WC.iteritems():
    #     print key
    # print dict710WC

    # print 'Letzte ID: ' + str(lastID)
    # print 'Letzter Titel: ' + str(lastTitel)
    # print 'Letzter Text: ' + lastText
    # print '\n\n'
    # print dictNE
    # print '\n'
    # print dictNN
    # return extractQueryInputDB
    # return locals()
    return dictNE, dictNN


def seeLastEntryParsedDB():
    """Function with a Query to get the last Entry from the Database with
    NLP-Stuff afterwards."""
    parsedDatabase = SQLFORM(db.dbParsedText)
    queryLastEntry = db.executesql('select id, inputTitle, inputText\
                                    from dbInput')
    lastEntry = queryLastEntry[-1]
    lastID = queryLastEntry[-1][0]
    lastTitel = queryLastEntry[-1][1]
    lastText = queryLastEntry[-1][2]

    # return dict(dings=dings)
    # print lastEntry
    # print 'Letzte ID: ' + str(lastID)
    # print 'Letzter Titel: ' + str(lastTitel)
    # print 'Letzter Text: ' + lastText
    # for word, pos in tag(dings, tagset="STTS"):
    #    if pos == "NE" or pos == "NN":
    #        print pos + '\t' + word
    # return dict(dings=dings)
    # return dings


def comparingDicts(dictNE, dictNN):
    """Function to compare the dictionaries of the given text and from
    the corpora."""
    # Defining list variables
    listDocumentAll = []
    listDocumentNE = []
    listDocumentNN = []

    # Defining variables to count for each DDC
    count330All = 0
    count330WC = 0
    count330NE = 0
    count330NN = 0
    count710All = 0
    count710WC = 0
    count710NE = 0
    count710NN = 0

    dict330All, dict330WC, dict330NE, dict330NN, dict710All, dict710WC,\
        dict710NE, dict710NN = loadDDCDicts()
    # for key, value in dictNE.iteritems():
    #     print key
    # print 'All:\t' + str(len(dict710All))
    # print 'WC:\t' + str(len(dict710WC))
    # print 'NE:\t' + str(len(dict710NE))
    # print 'NN:\t' + str(len(dict710NN))

    # Appending words from document dictionaries into lists
    for key, value in dictNE.iteritems():
        listDocumentAll.append(key)
        listDocumentNE.append(key)

    for key, value in dictNN.iteritems():
        listDocumentAll.append(key)
        listDocumentNN.append(key)

    # Counting all words in both DDCs
    for i in listDocumentAll:
        for j in dict710All.keys():
            if i == j:
                count710All += 1
            else:
                pass

        for k in dict710WC.keys():
            if i == k:
                count710WC += 1
            else:
                pass

        for l in dict330All.keys():
            if i == l:
                count330All += 1
            else:
                pass

        for m in dict330WC.keys():
            if i == m:
                count330WC += 1
            else:
                pass

    for i in listDocumentNE:
        for j in dict710NE.keys():
            if i == j:
                count710NE += 1
            else:
                pass

        for k in dict330NE.keys():
            if i == k:
                count330NE += 1
            else:
                pass

    for i in listDocumentNN:
        for j in dict710NN.keys():
            if i == j:
                count710NN += 1
            else:
                pass

        for k in dict330NN.keys():
            if i == k:
                count330NN += 1
            else:
                pass

    # Defining variables with sums of DDCs
    noAll = count710All + count330All
    noAll = float(noAll)
    noWC = count710WC + count330WC
    noWC = float(noWC)
    noNE = count710NE + count330NE
    noNE = float(noNE)
    noNN = count710NN + count330NN
    noNN = float(noNN)

    # Calculation Operations
    # If to avoid possible divide by 0 in the divisor
    if noAll != 0:
        result710All = (count710All/noAll)*100
        result330All = (count330All/noAll)*100
    else:
        result710All = 'Empty'
        result330All = 'Empty'

    if noWC != 0:
        result710WC = (count710WC/noWC)*100
        result330WC = (count330WC/noWC)*100
    else:
        result710WC = 'Empty'
        result330WC = 'Empty'

    if noNE != 0:
        result710NE = (count710NE/noNE)*100
        result330NE = (count330NE/noNE)*100
    else:
        result710NE = 'Empty'
        result330NE = 'Empty'

    if noNN != 0:
        result710NN = (count710NN/noNN)*100
        result330NN = (count330NN/noNN)*100
    else:
        result710NN = 'Empty'
        result330NN = 'Empty'

    # Print all results in the Terminal
    print 'Found tagged words:\n'
    print 'count710All:\t' + str(count710All)
    print 'count710WC:\t' + str(count710WC)
    print 'count710NE:\t' + str(count710NE)
    print 'count710NN:\t' + str(count710NN)
    print 'count330All:\t' + str(count330All)
    print 'count330WC:\t' + str(count330WC)
    print 'count330NE:\t' + str(count330NE)
    print 'count330NN:\t' + str(count330NN)
    print '#################################'
    print 'Summed up words:\n'
    print 'noAll:\t' + str(int(noAll))
    print 'noWC:\t' + str(int(noWC))
    print 'noNE:\t' + str(int(noNE))
    print 'noNN:\t' + str(int(noNN))
    print '#################################'
    print 'Results:\n'
    print 'result710All:\t' + str(result710All) + '%'
    print 'result330All:\t' + str(result330All) + '%'
    print 'result710WC:\t' + str(result710WC) + '%'
    print 'result330WC:\t' + str(result330WC) + '%'
    print 'result710NE:\t' + str(result710NE) + '%'
    print 'result330NE:\t' + str(result330NE) + '%'
    print 'result710NN:\t' + str(result710NN) + '%'
    print 'result330NN:\t' + str(result330NN) + '%'
    print '#################################'
    print ' '


def index():
    """Main Function."""
    returnSubmissionForm = defineSubmissionForm()
    # loadDDCDicts()
    lastID, lastTitel, lastText = getLastEntryInputDB()
    dictNE, dictNN = insertTagsToParsedDB(lastID, lastTitel, lastText)
    seeLastEntryParsedDB()
    if lastTitel == '':
        lastTitel = 'Was Empty'
    else:
        pass
    print '>>>>>\t\t' + lastTitel + '\t\t<<<<<\n'
    comparingDicts(dictNE, dictNN)
    return returnSubmissionForm
