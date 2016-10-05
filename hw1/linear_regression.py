import numpy as np
#import sys

fin = open('train.csv','r')

rawdata = []

for line in fin:
		rawdata.append(line.strip().split(','))

fin.close()

#print rawdata

datapm = []
count = 0

# 10 pm2.5 feature

for i in range(1,4321):
	if (i-10)%18 == 0:      #search pm2.5 line
		for j in range (15):	
			datapm.append(rawdata[i][3+j:j+13])
			count = count + 1

print 'count = ',count  #count = 240*15 = 3600
#print data10
#---------------------ok till here---------------------------
y = []
for i in range(count):
	y.append(0)

w = []
for i in range(2):
	w.append(0)
w[0] = 0.05
w[1] = 0.5 


learningrate = 0.0000003

# b = w[0]
dLdw = []
for i in range(0,2):
	dLdw.append(0)

while True:
	dLdwjj = 1
	for i in range(0,2): # new w[0~1]
		w[i] = w[i] - learningrate*dLdw[i]
		dLdw[i] = 0

	for i in range (count):
		y[i] = w[0] + w[1]*float(datapm[i][8])
		#yi complete
		dLdw[0] = dLdw[0]+(-2)*(float(datapm[i][9])-y[i])		
		dLdw[1] = dLdw[1]+(-2)*(float(datapm[i][9])-y[i])*float(datapm[i][8])
	#complete summing the Loss derivative(dLdw[0~9])
	for i in range(0,2):
		dLdwjj = dLdwjj*dLdw[i]
	print dLdw
	if(abs(dLdwjj) < 0.00005):
		print w
		break


fin = open('test_X.csv','r')
data = []
for line in fin:
		data.append(line.strip().split(','))
fin.close()

datapmm = []
for i in range(1,4321):
	if (i-9)%18 == 0:      #search pm2.5 line	
		datapmm.append(data[i][10])

fout = open('linear_regression.csv','w')
fout.write('id,value\n')
for i in range(240):
	fout.write('id_')
	fout.write(str(i))
	fout.write(',')
	fout.write(str(w[0]+w[1]*float(datapmm[i])))
	fout.write('\n')


