#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
import treetaggerwrapper


tagger = treetaggerwrapper.TreeTagger(TAGLANG='en')
tags = tagger.tag_text("This is a very short text to tag.")
pprint.pprint(tags)
