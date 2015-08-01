import json
import random
import user

name = 'reyarch'

with open('users/{0}/first_words.json'.format(name), 'r') as fs:
	first_words = json.load(fs)

with open('users/{0}/relation_dict.json'.format(name), 'r') as fs:
	relation_dict = json.load(fs)

flist = []
for k in first_words:
	flist += [k]*len(first_words[k])

message = random.choice(flist)
cur_word = random.choice(first_words[message])
while cur_word != 'ENDBABY':

	message = message + ' ' + cur_word
	cur_word = random.choice(relation_dict[cur_word])
print message

