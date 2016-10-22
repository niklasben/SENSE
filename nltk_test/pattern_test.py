# -*- coding: utf-8 -*-

from pattern.de import parse, split

s = parse('Die Katze liegt auf der Matte.')
for sentence in split(s):
    for word in sentence:
        print(word)
