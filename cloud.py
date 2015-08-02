import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from scipy.misc import imread

name = 'reyarch'

with open('users/{0}/first_words.json'.format(name), 'r') as fs:
	first_words = json.load(fs)

with open('users/{0}/relation_dict.json'.format(name), 'r') as fs:
	relation_dict = json.load(fs)

all_words = sorted(relation_dict, key=lambda x: len(relation_dict[x]))

text = open('all_words.txt', 'r').read()
pepe_mask = imread('pepe.jpeg')

wc = WordCloud(background_color="white", max_words=2000, mask=pepe_mask,
               stopwords=STOPWORDS.add("heart"))
wc.generate(text)
wc.to_file('pepecloud.png')
plt.imshow(wc)
plt.axis("off")
plt.show()