# -*- coding:utf-8 -*-'
from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt

(x_train,_),(x_test,_) = mnist.load_data()
x_train = x_train.astype('float32')/255.0
x_test = x_test.astype('float32') /255.0
x_train = np.reshape(x_train,(len(x_train),1,28,28))
x_test = np.reshape(x_test,(len(x_test),1,28,28))

noise_factor = 0.5
x_train_noisy = x_train + noise_factor + np.random.normal(loc=0.0,scale=1.0,size=x_train.shape)
x_test_noisy = x_test + noise_factor + np.random.normal(loc=0.0,scale=1.0,size=x_test.shape)
x_train_noisy = np.clip(x_test_noisy,0.,1.0)
x_test_noisy = np.clip(x_test_noisy,0.0,1.0)

n = 10
plt.figure(figsize=(20,2))
for i in range(n):
    ax = plt.subplot(1,n,1+1)
    plt.imshow(x_test_noisy[i].reshape(28,28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()


