__author__ = 'gohper'
# -*- coding:utf-8 -*-

import pynlpir

pynlpir.open()

s = "聊天机器人到底该怎么做呢?"
segs = pynlpir.segment(s)
for seg in segs:
    print seg[0],'\t',seg[1]

print ("_____")


s1 = "海洋是如何形成的"
segs = pynlpir.segment(s1,pos_names='all')
for seg in segs:
    print seg[0],'\t',seg[1]

print("_________")
key_words = pynlpir.get_key_words(s,weighted=True)
for key_word in key_words:
    print key_word[0],'\t',key_word[1]

pynlpir.close()



