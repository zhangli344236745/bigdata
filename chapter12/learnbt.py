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

path = "bat/train_set.bat"
bunch = readbunchobj(path)

tfidfspace = Bunch(target_name=bunch.target_name,label=bunch.label,filenames=bunch.filenames,tdm=[],vocabulary=[])
print bunch.contents

vectorizer = TfidfVectorizer(stop_words=stpwrdlist,sublinear_tf=True,max_df=0.5)