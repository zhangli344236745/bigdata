# -*- coding:utf-8 -*-'
import sys
import os
import jieba

reload(sys)
sys.setdefaultencoding('utf-8')

def savefile(savepath,content):
    fp = open(savepath,'wb')
    fp.write(content)
    fp.close()

def readfile(path):
    fp = open(path,'rb')
    content = fp.read()
    fp.close()
    return content

corpus_path = "small/"
seg_path ="seg/"
catelist = os.listdir(corpus_path)

for mydir in catelist:
    fullName =  corpus_path + mydir
    content = readfile(fullName).strip()
    print content
    content_seg = jieba.cut(content)
    savefile(seg_path + mydir," ".join(content_seg))

print "close"