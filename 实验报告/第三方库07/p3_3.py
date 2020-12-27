# -*- coding: utf-8 -*- 
# @Time : 2020/12/13 0013 18:49 
# @Author : agul
# @File : p3_3.py 
# @description:

# import wordcloud
# import jieba
# from scipy.misc import imread
# img = imread('kongming1.png')
#
# stopwords = [line.strip() for line in open('stopwords.txt', encoding='utf-8').readlines()]
# article = open("三国演义.txt", encoding='utf-8').read()
# words = jieba.lcut(article)
# lst = []
# for word in words:
#     if (word in stopwords) or len(word) == 1:
#         continue
#     elif word == '玄德' or word == '玄德曰' or word == '主公':
#         newword = '刘备'
#     elif word == '关公' or word == '云长':
#         newword = '关羽'
#     elif word == '丞相':
#         newword = '曹操'
#     elif word == '孔明' or word == '孔明曰':
#         newword = '诸葛亮'
#     else:
#         newword = word
#     lst.append(newword)
# text = ' '.join(lst)
# cloud = wordcloud.WordCloud(font_path='simsun.ttc', mask=img, background_color='white').generate(text)
# cloud.to_file('hello.png')



from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import jieba


def trans_CN(txt):
    stopwords = [line.strip() for line in open('stopwords.txt', encoding='utf-8').readlines()]
    words = jieba.lcut(txt)
    lst = []
    for word in words:
        if (word in stopwords) or len(word) == 1:
            continue
        elif word == '玄德' or word == '玄德曰' or word == '主公':
            newword = '刘备'
        elif word == '关公' or word == '云长':
            newword = '关羽'
        elif word == '丞相':
            newword = '曹操'
        elif word == '孔明' or word == '孔明曰':
            newword = '诸葛亮'
        else:
            newword = word
        lst.append(newword)
    text = ' '.join(lst)
    return text


with open("三国演义.txt",encoding='UTF-8') as fp:
    txt = fp.read()
    text = trans_CN(txt)
    mask = np.array(image.open("kongming1.png"))
    wordcloud = WordCloud(
        font_path='simsun.ttc',
        width=1000, height=700,
        background_color="white",
        mask=mask,
    ).generate(text)
    image_produce = wordcloud.to_image()
    image_produce.show()