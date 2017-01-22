# -*- coding:utf-8 -*-'
import sys
import os
from sklearn.datasets.base import Bunch
import pickle
from sklearn import feature_selection
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

reload(sys)
sys.setdefaultencoding('utf-8')

def readbunchobj(path):
    file_obj = open(path,"rb")
    bunch = pickle.load(file_obj)
    file_obj.close()
    return bunch

def writebunchobj(path,bunchobj):
    file_obj = open(path,"wb")
    pickle.dump(bunchobj,file_obj)
    file_obj.close()

def readfile(path):
    fp = open(path,'rb')
    content = fp.read()
    fp.close()
    return content

path = "bat/train_set.bat"
bunch = readbunchobj(path)

tfidfspace = Bunch(target_name=bunch.target_name,label=bunch.label,filenames=bunch.filenames,tdm=[],vocabulary=[])
print bunch.contents

stopword_path = "stopword/stop_words.txt"

stpwrdlist = readfile(stopword_path).splitlines()
print stpwrdlist

vectorizer = TfidfVectorizer(stop_words=stpwrdlist,sublinear_tf=True)
transformer = TfidfTransformer()
tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)
tfidfspace.vocabulary = vectorizer.vocabulary_

space_bath = "bag/tfspace.bat"
writebunchobj(space_bath,tfidfspace)