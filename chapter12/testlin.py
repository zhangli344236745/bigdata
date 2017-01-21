# -*- coding:utf-8 -*-'
from numpy import *
import matplotlib.pyplot as plt

dataSet = [[-0.017612,14.053064],[-1.395634,4.66254],[-0.75217,6.538620],[-1.322371,7.152353]]
dataMat = mat(dataSet).T
print dataMat

mylist = [1,2,3,4,5]
a = 10
mymat = mat(mylist)
print a*mymat

myRand  = random.rand(3,4)
print myRand

print("____________")
mymatrix = mat([[1,2,3],[4,5,6],[7,8,9]])
print mymatrix * 10
print sum(mymatrix)
print power(mymatrix,2)

plt.scatter(dataMat[0],dataMat[1],c="red",marker="o")

X = linspace(-2,2,100)
Y = 2.* X + 9

plt.plot(X,Y)
plt.show()


print("________________")
vectormat = mat([[1,2,3],[4,5,6]])
v12 = vectormat[0] - vectormat[1]
print vectormat[0]
print vectormat[1]
print vectormat.T
