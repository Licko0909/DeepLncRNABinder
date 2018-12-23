import os
import sys
from numpy import array
from numpy import argmax
from keras.utils import to_categorical
import numpy as np
import string

from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
import numpy


import h5py
filename = sys.argv[1]
f = h5py.File(filename, 'r')
x_train = np.array(f['x_train'])
x_test = np.array(f['x_test'])
y_train = np.array(f['y_train'])
y_test = np.array(f['y_test'])
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

import Models
name = sys.argv[2]
NUM_KERNEL = 32
Models.smallCNN(x_train,y_train,x_test,y_test,1,x_train.shape[1:3],11,NUM_KERNEL,name)

#NUM_KERNEL = 16
#Models.smallCNN(x_train,y_train,x_test,y_test,1,x_train.shape[1:3],11,NUM_KERNEL,name)

#NUM_KERNEL = 64
#Models.smallCNN(x_train,y_train,x_test,y_test,1,x_train.shape[1:3],11,NUM_KERNEL,name)
