# -*- coding: utf-8 -*-
"""Docstring."""

import sys
import treetaggerwrapper as ttw
from treetagger import TreeTagger
import pprint


tagger = ttw.TreeTagger(TAGLANG='de', TAGDIR='/home/niklas/treetagger/')
#tagger = ttw.TreeTagger(TAGLANG='de')

# with open(sys.argv[1], 'r') as inputfile:
#     for line in inputfile:
#         line = line.decode('utf-8')
#         tags = tagger.tag_text(line)
#         pprint.pprint(tags)

# tt = TreeTagger(language='english')
tt = ttw.TreeTagger(TAGLANG='en', TAGDIR='/home/niklas/treetagger/')
pprint(tt.tag_text('What is the airspeed of an unladen swallow?'))
