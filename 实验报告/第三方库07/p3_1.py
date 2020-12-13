# -*- coding: utf-8 -*- 
# @Time : 2020/12/13 0013 14:18 
# @Author : agul
# @File : p3_1.py 
# @description:
import jieba

stopwords = [line.strip() for line in open('stopwords.txt', encoding='utf-8').readlines()]
article = open("三国演义.txt", encoding='utf-8').read()
words = jieba.lcut(article)
word_freq = {}
for word in words:
    if (word in stopwords) or len(word) == 1:
        continue
    elif word == '玄德' or word  == '玄德曰' or word == '主公':
        newword='刘备'
    elif word == '关公' or word == '云长':
        newword='关羽'
    elif word == '丞相':
        newword='曹操'
    elif word=='孔明' or word == '孔明曰':
        newword='诸葛亮'
    else:
        newword=word

    if newword in word_freq:
        word_freq[newword] += 1
    else:
        word_freq[newword] = 1
freq_word = []
for word, freq in word_freq.items():
    freq_word.append((word, freq))
freq_word.sort(key = lambda x:x[1], reverse=True)
for word, freq in freq_word [:10]:
    print(word, freq)
