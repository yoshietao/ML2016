# -*- coding: utf-8 -*-
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.models import load_model
from keras.callbacks import EarlyStopping
import numpy as np
import pickle
import sys

path 		= sys.argv[1]
input_model = sys.argv[2]
output_csv  = sys.argv[3]

model = load_model(input_model)

test = pickle.load(open(str(path)+'test.p','rb'))
test = np.array(test['data'])
test = test.astype('float32')
test/=255

test = model.predict(test.reshape(10000,3,32,32))

predictindex = np.zeros(10000)

for i in range (10000):
	maxp = 0
	for j in range (10):
		nextp = test[i][j]
		if (nextp > maxp) :
			maxp = nextp
			predictindex[i] = int(j)
print predictindex

fout = open(output_csv,'w')
fout.write('ID,class\n')
for i in range (10000):
	fout.write(str(i)+str(',')+str(int(predictindex[i]))+str('\n'))

