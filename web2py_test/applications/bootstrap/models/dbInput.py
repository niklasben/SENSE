# -*- coding: utf-8 -*-
#from gluon import current
from gluon.custom_import import track_changes; track_changes(True)

db = DAL('sqlite://storage.sqlite', migrate=True, fake_migrate=True, lazy_tables=False)

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


db.define_table('dbParsedText',
                Field('fk_dbInput', 'reference dbInput'),
                Field('parsedTitle', 'list:string'),
                Field('parsedText', 'list:string'),
                Field('taggedTextNE', 'list:string'),
                Field('taggedTextNN', 'list:string'),
                migrate='dbparsedText.table'
               )

db.dbParsedText.fk_dbInput.label = T('Foreign Key')
# db.dbParsedText.fk_dbInput.comment = T('Foreign Key')
db.dbParsedText.parsedTitle.label = T('Parsed Title')
# db.dbInput.inputTitle.comment = T('Parsed Title')
db.dbParsedText.parsedText.label = T('Parsed Text')
# db.dbInput.inputText.comment = T('Parsed Text')
db.dbParsedText.taggedTextNE.label = T('NE tagged from Text')
# db.dbInput.taggedTextNE.comment = T('NE tagged from Text')
db.dbParsedText.taggedTextNN.label = T('NN tagged from Text')
# db.dbInput.taggedTextNN.comment = T('NN tagged from Txt')


# current.db = db
