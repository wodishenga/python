#python 提取一篇文章中出现次数最多的十个单词及出现的次数
import re
from collections import Counter 
word_dict = {}
with open('a.txt','r') as f:
	for line in f.readlines():
		templine = re.sub('[.|,]',' ',line)
		tmplist = templine.split()
		for words in tmplist:
			if words in word_dict:
				word_dict[words] += 1	
			else:
				word_dict[words] = 1
	count = Counter(word_dict)
	print(count.most_common()[:10])

