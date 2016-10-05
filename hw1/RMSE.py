import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt


fin = open('correctanswer.csv','r')
data = []
for line in fin:
		data.append(line.strip().split(','))
fin.close()

#print data

datapmm = []
for i in range(1,241):	
	datapmm.append(float(data[i][1]))


fin = open('diff121.csv','r')
data1 = []
for line in fin:
		data1.append(line.strip().split(','))
fin.close()

new = []
for i in range(1,241):	
	new.append(float(data1[i][1]))

new = np.array(new)
datapmm = np.array(datapmm)
print new
print datapmm

RMSE = sqrt(mean_squared_error(datapmm, new))
#mse = ((datapmm - new) ** 2).mean(axis=None)

#RMSE = sqrt(mse)
print RMSE