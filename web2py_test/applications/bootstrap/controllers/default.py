# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorizationdisplay_form
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
from pattern.de import parse, split, pprint, tag
from pprint import pprint


def seeLastEntry():
    """Function with a Query to get the last Entry from the Database with NLP-Stuff afterwards."""
    parsedDatabase = SQLFORM(db.dbParsedText)
    query = db.executesql('select id, inputText from dbInput')
    dings = query[-1][1]
    
    for word, pos in tag(dings,
                     tagset="STTS"):
        if pos == "NE" or pos == "NN":
            print word + '\t' + pos
    return dict(dings=dings)


def defineForm():
    """Function to build the Form."""
    form=SQLFORM(db.dbInput)
    form.element(_type='submit')['_class'] = 'btn btn-default btn-sm'
    form.element('input[type=submit]',
             replace=lambda button: CAT(button,
                                        INPUT(_class='btn btn-warning btn-sm',
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
    return dict(form=form)


def index():
    """Main Function."""
    returnForm = defineForm()
    returnLastEntry = seeLastEntry()
    return returnForm


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
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users

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
