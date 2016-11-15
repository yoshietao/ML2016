# -*- coding: utf-8 -*-
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.models import load_model
from keras.callbacks import EarlyStopping
import numpy as np
import pickle
import sys

path 	     = sys.argv[1]
output_model = sys.argv[2]

x_label = []
y_label = []

print 'load'
all_label = pickle.load(open(str(path)+'all_label.p','rb'))

print 'start'
for i in range (10):
	for j in range(500):
		x_un = []
		for k in range(1024):
			x = all_label[i][j][k]*0.587 
			x = x + all_label[i][j][k+1024]*0.114 
			x = x + all_label[i][j][k+2048]*0.299  # gray value(GBR)
			x = round(x,2)
			x_un.append(x)
		x_label.append(x_un)
		y_label.append(i)
del all_label
x_label = np.array(x_label)
x_label = x_label.astype('float32')/255
print x_label.shape
print 'label gray process ok'

unlabel = pickle.load(open(str(path)+'all_unlabel.p','rb'))
unlabel = np.array(unlabel)
print unlabel.shape

for i in range(1024):
	unlabel[:,i] = unlabel[:,i]*0.587+unlabel[:,i+1024]*0.114+unlabel[:,i+2048]*0.299

unlabel,a,b = np.hsplit(unlabel,np.array([1024,2048]))
unlabel = unlabel.astype('float32')/255

del a,b

print unlabel.shape
print 'unlabel gray process ok'


for i in range(10):  #10
	print 'add ',i, 'round' 
	for j in range(450):  #450
		minvalue = 30000
		minindex = 50
		for k in range(5000):
			temp = np.dot(unlabel[i*10+j]-x_label[k],unlabel[i*10+j]-x_label[k])
			if temp < min:
				minvalue = temp
				minindex = y_label[k]
		x_label = x_label.tolist()
		x_label.append(unlabel[i*10+j])
		x_label = np.array(x_label)
		y_label.append(minindex)
y_label = np.array(y_label)

model = Sequential()

print x_label.shape

model.add(Dense(100, input_dim = 1024, activation = 'sigmoid'))
model.add(Dense(100, activation = 'sigmoid'))
model.add(Dense(10, activation = 'softmax'))
model.compile(loss = 'sparse_categorical_crossentropy',optimizer = 'adam',metrics = ['accuracy'])
model.fit(x_label, y_label, batch_size = 50, nb_epoch = 30)
score = model.evaluate(x_label,y_label)
print 'acc',score[1]

model.save(output_model)