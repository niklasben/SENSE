#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
from treetagger import TreeTagger

tt = TreeTagger(language='english')
print(tt.tag('What is the airspeed of an unladen swallow?'))

pprint.pprint(tt.tag('What is the airspeed of an unladen swallow?'))
