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

file = open(str(path)+'all_label.p','rb')
all_label = pickle.load(file)
file.close()

x_train = []
y_train = []
X_test  = []
Y_test  = []

for i in range(10):
	for j in range(500):
		x_train.append(all_label[i][j])
		y_train.append([i])
	'''
	for j in range(250,500):
		X_test.append(all_label[i][j])
		Y_test.append([i])
	'''
X_train = np.array(x_train)
X_Train = X_train.reshape(X_train.shape[0],3,32,32)
X_Train = X_Train.astype('float32')
X_Train /= 225
'''
X_test = np.array(X_test)
X_test = X_test.reshape(X_test.shape[0],3,32,32)
X_test = X_test.astype('float32')
X_test /= 225
'''
#print X_train.shape

Y_train = np.array(y_train)
#Y_test = np.array(Y_test)
print Y_train.shape
model = Sequential()

model.add(Convolution2D(16, 3, 3, border_mode='same', input_shape=X_Train.shape[1:]))
model.add(Activation('relu'))
model.add(Convolution2D(16, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(32, 3, 3, border_mode='same'))
model.add(Activation('relu'))
model.add(Convolution2D(32, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64, 3, 3, border_mode='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())

model.add(Dense(512, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation = 'softmax'))

model.compile(loss = 'sparse_categorical_crossentropy',optimizer = 'adam',metrics = ['accuracy'])
model.save('emptymodel.h5')

earlystopping = EarlyStopping(monitor='val_loss', patience=5)

model.fit(X_Train, Y_train, batch_size = 100, nb_epoch = 5, shuffle=True) # validation_data=(X_test, Y_test), callbacks=[earlystopping],

score = model.evaluate(X_Train,Y_train)
print 'acc',score[1]
while score[1] < 0.9:
	model.fit(X_Train, Y_train, batch_size = 100, nb_epoch = 5, shuffle=True) # validation_data=(X_test, Y_test), callbacks=[earlystopping],
	score = model.evaluate(X_Train,Y_train)
	print 'acc',score[1]

model.save('epoch.h5')
#------------------------------------------------------------------------------------
