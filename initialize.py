import json
import unicodedata
import os
from user import *

with open('slack/users.json') as users_json:
	user_info = json.load(users_json)

id_to_name = {u['id'].encode('ascii', 'ignore'):u['name'].encode('ascii', 'ignore') for u in user_info}

users = {}
for uid in id_to_name:
	new_user = User(uid, id_to_name[uid])
	users[uid] = new_user

for f in os.listdir('slack/general/'):
	with open('slack/general/{0}'.format(f)) as cur_log:
		log = json.load(cur_log)
		for message in log:
			try:
				cur_user = message['user']
				text_list = message['text'].encode('ascii', 'ignore').split(' ')
				for word in text_list:
					if word[0] != '<' and word[0] != '&':
						aw_f.write('{0} '.format(word))
				users[cur_user].addMessage(text_list)
			except:
				pass

print 'graphs assembled'

for u in users:
	if not os.path.exists('users/{0}'.format(users[u].name)):
		os.makedirs('users/{0}'.format(users[u].name))
	with open('users/{0}/first_words.json'.format(users[u].name), 'w') as fs:
		json.dump(users[u].first_words, fs)
	with open('users/{0}/relation_dict.json'.format(users[u].name), 'w') as fs:
		json.dump(users[u].relation_dict, fs)

print 'files printed'