# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorizationdisplay_form
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
from pattern.de import parse, split, pprint, tag, parsetree, singularize
from pprint import pprint
import os
import json
import sys


# Set default encoding to UTF-8
reload(sys)
sys.setdefaultencoding('utf-8')

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

    # DDC 710 with all words
    with open(filepath + 'dict710All.json', 'r') as readDict710All:
        dict710All = json.load(readDict710All)

    # DDC 710 without common used words of all DDCs
    with open(filepath + 'dict710WithoutCommons.json', 'r') as readDict710WC:
        dict710WC = json.load(readDict710WC)

    # for key, value in dict710WC.iteritems():
    #     print key


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

    # print 'Letzte ID: ' + str(lastID)
    # print 'Letzter Titel: ' + str(lastTitel)
    # print 'Letzter Text: ' + lastText
    # print '\n\n'
    # print dictNE
    # print '\n'
    # print dictNN
    # return extractQueryInputDB


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
    # print lastEntry
    # print 'Letzte ID: ' + str(lastID)
    # print 'Letzter Titel: ' + str(lastTitel)
    # print 'Letzter Text: ' + lastText

    # for word, pos in tag(dings, tagset="STTS"):
    #    if pos == "NE" or pos == "NN":
    #        print pos + '\t' + word
    # return dict(dings=dings)
    # return dings


def index():
    """Main Function."""
    returnSubmissionForm = defineSubmissionForm()
    loadDDCDicts()
    lastID, lastTitel, lastText = getLastEntryInputDB()
    insertTagsToParsedDB(lastID, lastTitel, lastText)
    seeLastEntryParsedDB()
    # print seeLastEntryParsedDB()
    # loadDDCDicts()
    return returnSubmissionForm


"""
def user():

    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow
    administrator to manage users

    return dict(form=auth())


@cache.action()
def download():

    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]

    return response.download(request, db)


def call():

    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv

    return service()


def display_form():

    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()

    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))
"""
