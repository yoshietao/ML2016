#this is the generative model,in order to handle classification problem

import numpy as np
import sys
import math

trainset = sys.argv[1]
model    = sys.argv[2]

#////train.csv///
f = open(trainset,'r')

data = []
for line in f:
	data.append(line.strip().split(','))
f.close()

class0 = []
class1 = []

for i in range (4000):
	if float(data[i][58]) == 0:
		class0.append(data[i])
	else:
		class1.append(data[i])
len0 = len(class0)
print len0
len1 = len(class1)

mean0 = [] #58
mean1 = []
variance0 = [] #58
variance1 = []

for i in range(58):
	tempmean = 0
	for j in range (len0):
		tempmean = tempmean + float(class0[j][i])
	tempmean = float(tempmean)/len0
	mean0.append(tempmean)

	tempmean = 0
	for j in range (len1):
		tempmean = tempmean + float(class1[j][i])
	tempmean = float(tempmean)/len1
	mean1.append(tempmean)	

	tempvar = 0
	for j in range(len0):
		tempvar = tempvar + (float(class0[j][i]) - mean0[i])**2
	tempvar = tempvar/(len0-1)
	variance0.append(tempvar)

	tempvar = 0
	for j in range(len1):
		tempvar = tempvar + (float(class0[j][i]) - mean1[i])**2
	tempvar = tempvar/(len1-1)
	variance1.append(tempvar)

print len(mean0),len(mean1),len(variance0),len(variance1)

pc0 = float(len0)/(len0+len1)
pc1 = float(len1)/(len0+len1)

fout = open(model,'w')
fout.write(str(pc0))
fout.write('\n')
fout.write(str(pc1))
fout.write('\n')
for i in range(58):
	fout.write(str(mean0[i]))
	if i == 57:
		fout.write('\n')
	else:
		fout.write(',')
for i in range(58):
	fout.write(str(mean1[i]))
	if i == 57:
		fout.write('\n')
	else:
		fout.write(',')
for i in range(58):
	fout.write(str(variance0[i]))
	if i == 57:
		fout.write('\n')
	else:
		fout.write(',')
for i in range(58):
	fout.write(str(variance1[i]))
	if i == 57:
		fout.write('\n')
	else:
		fout.write(',')
