# -*- coding: utf-8 -*-
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

import errno
import fnmatch
import os
import re
import mmap
import nltk
from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords, PlaintextCorpusReader
from nltk.tokenize import wordpunct_tokenize
from nltk.tag import PerceptronTagger, BrillTagger
import treetaggerwrapper as ttw
from treetagger import TreeTagger
import shutil
import pprint
from pattern.de import parse, split, predicative
import pattern.de

# for dirpath, dirs, files in os.walk('../DDCs/deu'):
#     # print dirpath[-3:]
#     if dirpath[-3:] == '710' or dirpath[-3:] == '330':
#         # print dirpath
#         for filename in fnmatch.filter(files, '*.xml'):
#
#             foldername = '../temp/temp_' + dirpath[-3:] + '/'
#             newfilename = filename[11:-4] + '.txt'
#
#             with open(dirpath + '/' + filename, 'r') as openfile:
#                 s = mmap.mmap(openfile.fileno(), 0, access=mmap.ACCESS_READ)
#                 if s.find('<dc:description xml:lang="deu">') != -1:
#                     line = openfile.read()
#                     start = line.index('<dc:description xml:lang="deu">') + \
#                         len('<dc:description xml:lang="deu">')
#                     end = line.index('</dc:description>', start)
#
#                     if not os.path.exists(os.path.dirname(foldername)):
#                         try:
#                             os.makedirs(os.path.dirname(foldername))
#                         except OSError as exc:  # Guard against race condition
#                             if exc.errno != errno.EEXIST:
#                                 raise
#
#                 newfilename = filename[11:-4] + '.txt'
#                 with open(foldername + newfilename, 'w') as newfile:
#                     newfile.write(line[start:end])


foldername2 = '../temp/pos_tagged/'

if not os.path.exists(os.path.dirname(foldername2)):
    try:
        os.makedirs(os.path.dirname(foldername2))
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

# tt_en = TreeTagger(encoding='utf-8', language='english')
# pprint(tt_en.tag('Does this thing work?'))

tagger = ttw.TreeTagger(TAGLANG='de', TAGDIR='/home/niklas/treetagger/')
# satz = u'Dies ist ein Testsatz.'
# print type(satz)
# satzu = satz.decode('utf-8')
# tags = tagger.tag_text(satz)
# pprint.pprint(tags)

datei = open('196.txt', 'r')
dat = datei.read()

s = parse(dat, tagset='STTS')
s = split(s)
print s.sentences[0]
print predicative('neugierige')

with open('196.txt', 'r') as openfile:
    for line in openfile:
        nltk.tag.brill.BrillTagger(line)

# datu = dat.decode('utf-8')
# print tagger.tag_text(dat)
# print datu
# tags = tagger.TagText(datu)
# # for tag in tags:
# #     print tag
datei.close()

# for dirpath, dirs, files in os.walk('../temp'):
#     for filename in fnmatch.filter(files, '*.txt'):
#         tagger.tag_file_to('../temp/pos_tagged/'+filename, encoding='utf-8')


# for dirpath, dirs, files in os.walk('../temp/desc_umlaute'):
#     for filename in fnmatch.filter(files, '*.txt'):
#         with open(dirpath + '/' + filename, 'r') as originalfile, \
#          open('../temp/desc_pos/' + filename, 'w') as writefile:
#             for line in originalfile:
#                 s = parse(line)
#                 for sentence in split(s):
#                     sentence = str(sentence)
#                     sentence = sentence.lstrip('Sentence(\'').rstrip('\')')
#                     writefile.write(sentence + '\n\n')


# stopword_list = stopwords.words('german')
# stopword_list.extend(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')',
#                      '[', ']', '{', '}'])
# stopword_list = set(stopword_list)
# print stopword_list

# foldername2 = '../temp/desc/'

# if not os.path.exists(os.path.dirname(foldername2)):
#     try:
#         os.makedirs(os.path.dirname(foldername2))
#     except OSError as exc:  # Guard against race condition
#         if exc.errno != errno.EEXIST:
#             raise


# for dirpath, dirs, files in os.walk('../temp'):
#     with open('../temp/desc/desc_' + dirpath[-3:] + '.txt', 'w') as writefile:
#         for filename in fnmatch.filter(files, '*.txt'):
#             with open(dirpath + '/' + filename, 'r') as openfile:
#                 line = openfile.read()
#             writefile.write(line + '\n\n')


# replacements_umlaute = {
#                     '\\xc3\\xa4': 'ä',
#                     '\\xc3\\xbc': 'ü',
#                     '\\xc3\\xb6': 'ö',
#                     '\\xc3\\x9f': 'ß'
#                     }

# foldername3 = '../temp/desc_umlaute/'

# if not os.path.exists(os.path.dirname(foldername3)):
#     try:
#         os.makedirs(os.path.dirname(foldername3))
#     except OSError as exc:  # Guard against race condition
#         if exc.errno != errno.EEXIST:
#             raise

# for dirpath, dirs, files in os.walk('../temp/desc'):
#     for filename in fnmatch.filter(files, '*.txt'):
#         with open(dirpath + '/' + filename, 'r') as originalfile, \
#          open('../temp/desc_umlaute/' + filename, 'w') as writefile:
#             for line in originalfile:
#                 line = line.strip()
#                 for src, target in replacements_umlaute.iteritems():
#                     line = line.replace(src, target)
#                 writefile.write(line)

# shutil.rmtree('../temp')

# line = line.split()
# for i in line:
#     i = i.lower()
#     i = i.rstrip(',').rstrip('.').rstrip('?').rstrip('!')
#     if i in stopword_list:
#         pass
# else:
#   writefile.write(i + '\n')
