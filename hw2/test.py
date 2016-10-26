import numpy as np
import sys
import math

def sigmoid(z):
	return 1/(1+math.exp(-z))

model 	 = sys.argv[1]
testdata = sys.argv[2]
output   = sys.argv[3]

data = []
f = open(model,'r')

for line in f:
	data.append(line.strip().split(','))
f.close()

#data[0]:w
#data[1]:b

W = np.array([float(j) for j in data[0]])
b = float(data[1][0])


testx = []
f = open(testdata,'r')

for line in f:
	testx.append(line.strip().split(','))
f.close()

fout = open(output,'w')
fout.write('id,label\n')
for i in range(600):
	X = np.array([float(j) for j in testx[i]])
	ypredict = sigmoid(np.dot(X,W)+b)
	if ypredict >= 0.5:
		ypredict = 1
	else:
		ypredict = 0
	fout.write(str(i+1))
	fout.write(',')
	fout.write(str(ypredict))
	fout.write('\n')