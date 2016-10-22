import numpy as np
import sys
import math

model 	 = sys.argv[1]
testdata = sys.argv[2]
output   = sys.argv[3]

def Pxc(x,miu,var):
	pxc = 1
	for i in range(1,58):
		pxc = pxc*(float(1)/(2*math.pi)**0.5)*(float(1)/var[i]**0.5)*math.exp(-1*(x[i]-miu[i])**2/(2*var[i]))
	return pxc

data = []
f = open(model,'r')

for line in f:
	data.append(line.strip().split(','))
f.close()

#data[0]:pc0
#data[1]:pc1
#data[2]:mean0
#data[3]:mean1
#data[4]:variance0
#data[5]:variance1

pc0 = float(data[0][0])
pc1 = float(data[1][0])
mean0 = np.array([float(j) for j in data[2]])
mean1 = np.array([float(j) for j in data[3]])
variance0 = np.array([float(j) for j in data[4]])
variance1 = np.array([float(j) for j in data[5]])

testx = []
f = open(testdata,'r')

for line in f:
	testx.append(line.strip().split(','))
f.close()

fout = open(output,'w')
fout.write('id,label\n')
for i in range(600):
	X = [float(j) for j in testx[i]]
	ypredict = (Pxc(X,mean0,variance0))/(Pxc(X,mean0,variance0)+Pxc(X,mean1,variance1))
	if ypredict >= 0.5:
		ypredict = 0
	else:
		ypredict = 1
	fout.write(str(i+1))
	fout.write(',')
	fout.write(str(ypredict))
	fout.write('\n')