# -*- coding:utf-8 -*-'
import numpy as np
from nbayes_lib import NBayes

def loadDateSet():
    postingList = [['my','dog','has','flea','problems','help','please'],
                   ['maybe','not','take','him','to','dog','park','stupid'],
                   ['my','dalmation','is','so','cute','I','love','him','my'],
                   ['stop','posting','stupid','worthless','garbage'],
                   ['mr','licks','ate','my','steak','how','to','stop','him'],
                   ['quit','buying','worthless','dog','food','stupid']]
    classVec = [0 ,1 ,0,1 ,0,1]
    return postingList,classVec

dataSet ,listClasses = loadDateSet()
nb = NBayes()
nb.train_set(dataSet,listClasses)
nb.map2vocab(dataSet[0])
print nb.predict(nb.testset)

