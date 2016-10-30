# -*- coding: utf-8 -*-
#from gluon import current

db = DAL('sqlite://storage.sqlite')
db.define_table('dbInput',
                Field('inputTitle', 'string',
                      widget=lambda field,value: SQLFORM.widgets.string.widget(field,
                                                                               value,
                                                                               _class='form-control',
                                                                               _placeholder=T('Title'))),
                Field('inputText', 'text',
                      widget=lambda field,value: SQLFORM.widgets.text.widget(field,
                                                                             value,
                                                                             _class='form-control',
                                                                             _placeholder=
                                                                             T('Bitte geben Sie den zu untersuchenden Text in das Feld ein.'),
                                                                             _rows='10',
                                                                             _cols='100',
                                                                             _required='yes',
                                                                             _autofocus='yes'
                                                                            ),
                      requires=IS_NOT_EMPTY())
               )

db.dbInput.inputTitle.label = T('Label')
# db.dbInput.inputTitle.comment = T('Comment')
db.dbInput.inputText.label = T('Text')
# db.dbInput.inputText.comment = T('Comment')

# current.db = db
