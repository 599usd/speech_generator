class User(object):
	"""User class for users in slack"""
	def __init__(self, uid, name):
		self.id = uid
		self.name = name
		self.first_words = {}
		self.relation_dict = {}

	def addMessage(self, text_list):
		for i in xrange(len(text_list)):
			cur_word = text_list[i]
			if cur_word == "":
				pass
			if i == 0:
				if i + 1 == len(text_list):
					if cur_word in self.first_words:
						self.first_words[cur_word].append('ENDBABY')
					else:
						self.first_words[cur_word] = ['ENDBABY']
				else:
					if cur_word in self.first_words:
						self.first_words[cur_word].append(text_list[i+1])
					else:
						self.first_words[cur_word] = [text_list[i+1]]
			elif i == len(text_list) - 1:
				if cur_word in self.relation_dict:
						self.relation_dict[cur_word].append('ENDBABY')
				else:
					self.relation_dict[cur_word] = ['ENDBABY']
			else:
				if cur_word in self.relation_dict:
						self.relation_dict[cur_word].append(text_list[i+1])
				else:
					self.relation_dict[cur_word] = [text_list[i+1]]