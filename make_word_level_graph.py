# How to use
# 1. Install TreeTagger: https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/
# 2. Install TreeTaggerWrapper, Matplotlib
# 3. python3 make_word_level_graph.py
# Output: list of the number of word for each level, unknown words, png

import treetaggerwrapper as ttw

file_name = 'kennedy'
file_name = 'obama'

def get_level(file_name):
    tagger = ttw.TreeTagger(TAGLANG='en')
    tags = tagger.tag_file(file_name + '.txt')
    tags2 = ttw.make_tags(tags)

# with open(file_name + '.tag', 'w') as f:
#     for tag in tags:
#         f.write("%s\n" % tag)

    import re

    words = []

    for tag in tags2:
        if re.search('^\w', tag.lemma):
            for word in tag.lemma.lower().split('-'):
                words.append(word)

    words = list(set(words))

    import word_level

    sentence_level = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    unknown_words = []

    for word in words:
        level = word_level.get_level(word)
        sentence_level[level] += 1
        if level == 0:
            unknown_words.append(word)

    print(sentence_level)
    print(unknown_words)

    return sentence_level

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig = plt.figure()
plt.subplots_adjust(wspace=0.4, hspace=0.6)
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

sentence_level = get_level('kennedy')
left = np.array(range(len(sentence_level)))
height = np.array(sentence_level)
ax1.bar(left, height)
ax1.set_ylim(bottom=0, top=200)
ax1.set_xlabel('level of words')
ax1.set_ylabel('num of words')
ax1.set_title('speach Kennedy')

sentence_level = get_level('obama')
left = np.array(range(len(sentence_level)))
height = np.array(sentence_level)
ax2.bar(left, height)
ax2.set_ylim(bottom=0, top=200)
ax2.set_xlabel('level of words')
ax2.set_ylabel('num of words')
ax2.set_title('speach Obama')

plt.savefig('graph.png')
