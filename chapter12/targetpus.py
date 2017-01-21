# -*- coding:utf-8 -*-'
from sklearn.datasets.base import Bunch
import os
import sys
import pickle

def savefile(savepath,content):
    fp = open(savepath,'wb')
    fp.write(content)
    fp.close()

def readfile(path):
    fp = open(path,'rb')
    content = fp.read()
    fp.close()
    return content

bunch = Bunch(target_name=[],label=[],filenames=[],contents=[])
word_path = "bat/train_set.bat"
seg_path ="seg/"

catelist = os.listdir(seg_path)
bunch.target_name.extend(catelist)

for mydir in catelist:
    fullName =  seg_path + mydir
    bunch.label.append(mydir)
    bunch.filenames.append(fullName)
    bunch.contents.append(readfile(fullName).strip())

file_obj = open(word_path,"wb")
pickle.dump(bunch,file_obj)
file_obj.close()

print "build "