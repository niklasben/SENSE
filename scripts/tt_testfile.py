# -*- coding: utf-8 -*-

from treetagger import TreeTagger
from pprint import pprint

tt = TreeTagger(language='english')
pprint(tt.tag('What is the airspeed of an unladen swallow?'))
