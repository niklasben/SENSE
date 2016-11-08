# -*- coding: utf-8 -*-

from pattern.de import parse, split, pprint, tag, parsetree, singularize
import os
import json
import re
import operator


filename = os.path.splitext('testfile.txt')[0]
dict_name_nn = 'dict_' + filename + '_nn'
dict_name_ne = 'dict_' + filename + '_ne'
json_name_nn = dict_name_nn + '.json'
json_name_ne = dict_name_ne + '.json'

dict_name_nn = {}
dict_name_ne = {}

with open('testfile.txt', 'r') as openfile:
    read_text = openfile.read()
    parsetree_text = parsetree(read_text)
    # pprint(parsetree_text)
    # read_text = read_text.rstrip('\n')
    # print(re.findall(r'[\w]+|[.,!?;]', read_text))
    # pprint(parse(read_text, tags=True, chunks=True, relations=True,
    #              lemmata=True, encoding='utf-8', tagset='STTS'))
    for word, pos in tag(read_text, tagset='STTS'):
        if pos == 'NN':

            singularForm = singularize(word)

            if word == singularForm:
                pass
                # plural = True
                # print word + '\t' + singularForm + '\t' + str(plural)
            else:
                word = singularForm
                # plural = False
                # print word + '\t' + singularForm + '\t' + str(plural)

            if word not in dict_name_nn.keys():
                dict_name_nn[word] = 1
            elif word in dict_name_nn.keys():
                dict_name_nn[word] += 1
            else:
                pass
        elif pos == 'NE':

            singularForm = singularize(word)

            if word == singularForm:
                pass
                # plural = True
                # print word + '\t' + singularForm + '\t' + str(plural)
            else:
                word = singularForm
                # plural = False
                # print word + '\t' + singularForm + '\t' + str(plural)

            if word not in dict_name_ne.keys():
                dict_name_ne[word] = 1
            elif word in dict_name_ne.keys():
                dict_name_ne[word] += 1
            else:
                pass
        else:
            pass


# sorted_x = sorted(dict_name.items(), key=operator.itemgetter(1), reverse=True)
# print sorted_x

print 'Normale Nomen (NN): '
for key in dict_name_nn.iterkeys():
    print key + '\t' + str(dict_name_nn[key])
print '\n'

print 'Eigennamen (NE): '
for key in dict_name_ne.iterkeys():
    print key + '\t' + str(dict_name_ne[key])

# with open(json_name, 'w') as writefile:
#     json.dump(dict_name, writefile, indent=4)
