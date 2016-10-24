# -*- coding: utf-8 -*-

from pattern.de import parse, split, pprint, tag
import os
import json
import re


filename = os.path.splitext('testfile.txt')[0]
dict_name = 'dict_' + filename
json_name = dict_name + '.json'

dict_name = {
    'Name': filename,
    'Dings': 'Zeug'
}

with open('testfile.txt', 'r') as openfile:
    read_text = openfile.read()
    # read_text = read_text.rstrip('\n')
    # print(re.findall(r'[\w]+|[.,!?;]', read_text))
    pprint(parse(read_text, tags=True, chunks=True, relations=True,
                 lemmata=True, encoding='utf-8', tagset='STTS'))

# for word, pos in tag(read_text, tagset='STTS'):
#     if pos == 'XY':
#         print word + '\t' + pos

with open(json_name, 'w') as writefile:
    json.dump(dict_name, writefile, indent=4)
