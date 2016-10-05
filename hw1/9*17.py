import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from math import sqrt

f = open('train.csv','r')
data = []

for line in f:
	data.append(line.strip().split(','))
f.close()
#////train.csv///

w,h = 480,12*18
x = [[0 for x in range(w)] for y in range(h)] 

for k in range(12):				#column,month
	for l in range (18):		#column,feature
		if (l-11)%18 != 0:
			for i in range(20):		#row,day
				for j in range(3,27):
					x[l+k*18][i*24+j-3] = float(data[(20*k+i)*18+l][j])
#print x
X = np.array(x)
print X.shape
b,dLdb = 0,0
w = []
for i in range(162):   
	w.append(0.3)
dLdw = []
for i in range(162):
	dLdw.append(0)
totalm = 0
ypredict = 0
learningrate = 1000
Gt = []
Gtb = 0
for i in range(162):
	Gt.append(0)
#print W
print'--------------------initial w ok-----------------------------------------'
while True:
	for i in range(471):
		for j in range(12):
#--------------------------numbers of x,y data-----------------------------------
			yhat = float(x[18*j+9][i+9])
			xx = []
			for k in range(18):
				xx = xx+x[18*j+k][i:i+9]
			X = np.array(xx)
			W = np.array(w)
			ypredict = np.dot(X,W)+b
#------------------------- Yhat,Ypredict,X ok-----------------------------------
			dLdb = dLdb + (-2)*(yhat-ypredict)
			Gtb = Gtb + dLdb**2
			for k in range(162):
				dLdw[k] = dLdw[k] + (-2)*(yhat-ypredict)*xx[k]
				Gt[k] = Gt[k] + dLdw[k]**2
			#print Gt
	#print dLdb,dLdw[1],dLdw[2]
	print 'w',b,w
	print dLdw,round(dLdb)
	totalm = totalm + abs(dLdb)
	for i in range(162):
		totalm = totalm + abs(dLdw[i])
	if (totalm < 1.62):
		print round(b),w
		break
	for i in range(162):
		if Gt[i]!= 0:
			w[i] = w[i] - learningrate*dLdw[i]/(Gt[i]**0.5)
		b = b - learningrate*dLdb/(Gtb**0.5)
		dLdw[i] = 0
	dLdb = 0
	totalm = 0
print'--------------------------------------------------------------------------'








	
	
	
	
	



























