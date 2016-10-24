# -*- coding: utf-8 -*-

from pattern.de import parse, split, pprint, tag
# from pprint import pprint

# s = parse('Die Katze liegt auf der Matte.')
# for sentence in split(s):
#     for word in sentence:
#         print(word)
#     pprint(sentence)

pprint(parse('Die Katze liegt auf der Matte mit weniger als 10%.',
             tags=True, chunks=True, relations=True, lemmata=True,
             encoding='utf-8', tagset="STTS"))

for word, pos in tag('Die Katze liegt auf der Matte mit weniger als 10%.',
                     tagset="STTS"):
    if pos == "ARTDEF" or pos == "NN":
        print word + '\t' + pos
