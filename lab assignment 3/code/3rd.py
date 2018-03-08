import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.util import ngrams
from collections import Counter
from nltk.stem import WordNetLemmatizer

f= (open('input.txt').read())
z = sent_tokenize(f)
word_token = []
for a in z:
    word_token.append(word_tokenize(f))

l = []
Lm=WordNetLemmatizer()
for i in word_token:
    for x in i:
        l.append(Lm.lemmatize(x,'v'))
print('lemmatizing words, we get: ', l)


b = []
biagram_logic = ngrams(l,2)
for j in biagram_logic:
    b.append(j)
print('\n','biagram solution is :', b)

count = nltk.FreqDist(b)
freq= []
for i, j in count.items():
    freq.append((i,j))
print('\n', 'bigrams and frequencies are: ',freq)
common5= []
common5=count.most_common(5)
print('\n','repeated bi-grams are: ',common5)
text = []
for i in common5:
    text.append(i[0])
print('common 5 bigram :',text)
list=[]
for i in f.splitlines():
    for m in range(5):
        if text[m][0] in i.split() and text[m][1] in i.split():
            list.append(i)

print(' sentences contain 5 common: ',list)