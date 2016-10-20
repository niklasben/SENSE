# -*- coding: utf-8 -*-

import treetaggerwrapper
import pprint
# from treetagger.TreeTagger import TreeTagger
# from pprint.pprint import pprint
#
# tt = TreeTagger(language='english')
# pprint(tt.tag('What is the airspeed of an unladen swallow?'))

tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')
tags = tagger.tag_text("This is a very short text to tag.")
pprint.pprint(tags)
