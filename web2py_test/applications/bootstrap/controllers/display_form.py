# -*- coding: utf-8 -*-
'''def display_form():
    form=SQLFORM(db.dbInput)
    form.element(_type='submit')['_class'] = 'btn btn-default btn-sm'
    form.element('input[type=submit]',
             replace=lambda button: CAT(button,
                                        INPUT(_class='btn btn-warning btn-sm',
                                              _type='reset',
                                              _value=T('Reset'))
                                        )
             )
    return dict(form=form)'''


'''def display_form():
    form=FORM('Test',
              INPUT(_name='name', requires=IS_NOT_EMPTY()),
              INPUT(_type='submit'))
    if form.accepts(request,session):
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
    return dict(form=form)'''
