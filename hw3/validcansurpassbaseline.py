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

model = load_model('epoch.h5')
print 'load_model OK'

batchsize = 100
count = 0

x_train = []
y_train = []
all_label = pickle.load(open(str(path)+'all_label.p','rb'))
for i in range (10):
	for j in range(500):
		x_train.append(all_label[i][j])
		y_train.append([i])
del all_label
x_train = np.array(x_train)

unlabel = pickle.load(open(str(path)+'all_unlabel.p','rb'))
unlabel = np.array(unlabel)

while unlabel.shape[0] > 5000:
	#print '---------------computing new label & add unlabeled data----------------------------------'
	unlabshape = unlabel.shape[0]
	result = model.predict(unlabel.reshape(unlabshape,3,32,32))
	del model, unlabshape
	addunlabel = []	
	uunlabel = []
	X_test = []
	Y_test = []
	conut = 0
	for i in range(unlabel.shape[0]):
		maxp = 0
		predictp = 0
		predictindex = 0
		for j in range (10):
			nextp = float(result[i][j])
			if (nextp > maxp) :
				maxp = nextp
				predictindex = j
				predictp = maxp
		if (predictp > 0.7) :
			count += 1
			if count < 20000:
				addunlabel.append(unlabel[i])
				y_train.append([predictindex])
			else:
				X_test.append(unlabel[i])
				Y_test.append([predictindex])
		else:
			uunlabel.append(unlabel[i])
		del maxp,predictp,predictindex
	del unlabel
	unlabel = np.array(uunlabel)
	del uunlabel, result
	#print '------------------create new X, Y data------------------------------'
	addunlabel = np.array(addunlabel)
	X_test = np.array(X_test)
	X_test = X_test.reshape(X_test.shape[0],3,32,32)
	shape = x_train.shape[0]
	x_train = x_train.astype('float32')
	addunlabel = addunlabel.astype('float32')
	X_test = X_test.astype('float32')
	x_train/=255
	X_test/=555
	addunlabel/=255
	x_train = np.concatenate((x_train,addunlabel),axis = 0)
	del addunlabel
	shape = x_train.shape[0]
	x_train = x_train.reshape(shape,3,32,32)
	del shape
	#print '------------------train new data------------------------------------'
	model = load_model('emptymodel.h5')

	score = [0,0]
	earlystopping = EarlyStopping(monitor = 'val_loss', patience = 2)
	while score[1] < 0.85:
		model.fit(x_train, np.array(y_train), batch_size = 100, callbacks=[earlystopping], validation_data=(X_test, np.array(Y_test)), nb_epoch = 5, shuffle=True) 

		score = model.evaluate(x_train, np.array(y_train))
		print 'label acc ',score[1]
	del score	
	#score = model.evaluate(X_test, np.array(Y_test))
	#print 'unlabel acc ',score[1]
model.save(output_model)
