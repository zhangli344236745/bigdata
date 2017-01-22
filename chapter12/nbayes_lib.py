# -*- coding:utf-8 -*-'
import numpy as np

class NBayes(object):
    def __init__(self):
        self.vocabulary = []
        self.idf = 0
        self.tf = 0
        self.tdm = 0
        self.Pcates = {}
        self.labels = []
        self.doclength = 0
        self.vocablen = 0
        self.testset = 0

    def train_set(self,trainset,classVec):
        self.create_prob(classVec)
        self.doclength = len(trainset)
        tempset = set()
        [tempset.add(word) for doc in trainset for word in doc]
        self.vocabulary = list(tempset)
        self.vocablen = len(self.vocabulary)
        self.calc_wordfreq(trainset)
        self.build_tdm()

    def create_prob(self,classVec):
        self.labels = classVec
        labeltemps = set(self.labels)
        for labelitem in labeltemps:
            self.Pcates[labelitem] = float(self.labels.count(labelitem))/float(len(self.labels))

    def calc_wordfreq(self,trainset):
        self.idf = np.zeros([1,self.vocablen])
        self.tf = np.zeros([self.doclength,self.vocablen])
        for index in xrange(self.doclength):
            for word in trainset[index]:
                self.tf[index,self.vocabulary.index(word)] += 1
            for signword in set(trainset[index]):
                self.idf[0,self.vocabulary.index(signword)] += 1


    def build_tdm(self):
        self.tdm = np.zeros([len(self.Pcates),self.vocablen])
        sumlist = np.zeros([len(self.Pcates),1])
        for indx in xrange(self.doclength):
            self.tdm[self.labels[indx]] += self.tf[indx]
            sumlist[self.labels[indx]] = np.sum(self.tdm[self.labels[indx]])
        self.tdm = self.tdm/sumlist

    def map2vocab(self,testdata):
        self.testset = np.zeros([1,self.vocablen])
        for word in testdata:
            self.testset[0,self.vocabulary.index(word)] += 1

    def predict(self,testset):
        if np.shape(testset)[1] != self.vocablen:
            print "error"
            exit(0)
        predvalue = 0
        preclass = ""
        for tdm_vect,keyclass in zip(self.tdm,self.Pcates):
            temp = np.sum(testset*tdm_vect*self.Pcates[keyclass])
            if temp > predvalue:
                predvalue = temp
                preclass = keyclass
            return preclass

