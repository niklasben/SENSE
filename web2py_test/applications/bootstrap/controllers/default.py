# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorizationdisplay_form
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

def index():
    form=SQLFORM(db.dbInput)
    form.element(_type='submit')['_class'] = 'btn btn-default btn-sm'
    form.element('input[type=submit]',
             replace=lambda button: CAT(button,
                                        INPUT(_class='btn btn-warning btn-sm',
                                              _type='reset',
                                              _value=T('Reset'))
                                        )
             )
    return dict(form=form)

"""
def index():
    form=SQLFORM(db.dbInput,
                 labels=None,
                 showid=True,
                 comments=True,
                 submit_button='Submit',
                 delete_label='Check to delete:',
                 buttons=['submit', 'reset'],
                 separator=': '
                )
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'

    form.element(_type='submit')['_class'] = 'btn btn-default btn-sm'
    form.element('input[type=submit]',
             replace=lambda button: CAT(button,
                                        INPUT(_class='btn btn-warning btn-sm',
                                              _type='reset',
                                              _value=T('Reset'))
                                        )
             )
    return dict(form=form)
"""

"""
form=FORM('Your name:',
INPUT(_name='name', requires=IS_NOT_EMPTY()),
              INPUT(_type='submit'))
    if form.accepts(request,session):
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
    return dict(form=form)

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
