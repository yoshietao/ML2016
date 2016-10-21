import numpy as np
import sys
import math
#----------------------sigmoid--------------------------------
def sigmoid(z):
	return 1/(1+math.exp(-z))
#----------------------read file----------------------------------
trainset = sys.argv[1]
model    = sys.argv[2]

#////train.csv///
f = open(trainset,'r')
data = []

for line in f:
	data.append(line.strip().split(','))
f.close()

print data[0]
#---------------------------variables-------------------------------
b,dLdb = 0,0
w = []
for i in range(58):   
	w.append(0.1)
b = -0.435481421735

w = [-0.00049233550803256013, -0.31908764653402905, -0.26654572504663387, 0.21976171093656197, 0.65664239340706987, 0.49228151266979431, 0.58690314598223514, 1.5015366617925747, 0.62274928893644144, 0.50107655064785306, 0.027730337210848121, -0.10479007124327246, -0.31144104272231093, 0.099281306090578364, -0.020314145592442975, 0.98814298130527389, 0.86643690335469115, 0.96867079719030513, 0.1999331676671883, 0.014725174747235016, 1.0335482017995614, 0.19499647186817251, 0.20365320685786492, 1.3145353829066129, 1.3833769719739706, -0.82044662755725306, -0.71231541776941532, -0.66511586512412568, 0.15365382082502146, -0.73627942954784331, -0.39050112822238675, -0.76081047034105531, -0.45776848473559878, -0.69855686027130459, -0.12023800624655462, -0.51891459381420468, -0.26887781123639304, -0.8954243375208405, -0.1978153833346234, -0.67075308400651734, -0.29355992337841441, -0.98454296181925038, -0.8911297421855563, -0.61627632427569057, -0.86320393706492793, -0.65423674922733621, -0.83168944995313066, -1.3736145327774731, -1.0745102170740599, -0.9659165065937052, -0.46314252806262313, -0.76261956930606278, 0.147855126872945, 1.6916952164909731, 0.73162161883079679, -0.010515144077999881, 0.0060218202943769453, 0.00026178395655229633]

dLdw = []
for i in range(58):
	dLdw.append(0)

learningrate = 1
Gt = []
Gtb = 0
for i in range(58):
	Gt.append(0)
count = 0
#print W
print'--------------------Gradient descent-----------------------------------------'
while True:
	RMSE = 0
	count = count + 1
	for i in range (2000):
		yhat = float(data[i][58])
		X = np.array([float(j) for j in data[i][0:58]])
		W = np.array(w)
		#print X
		ypredict = sigmoid(np.dot(X,W)+b)
		if ypredict >= 0.5:
			ypredict1 = 1
		else:
			ypredict1 = 0
		#print ypredict
		RMSE = RMSE + abs(yhat - ypredict1)
		dLdb = dLdb + (yhat - ypredict)
		Gtb = Gtb + dLdb**2
		for j in range(58):
			dLdw[j] = dLdw[j] + (yhat - ypredict)*X[j]
			Gt[j] = Gt[j] + dLdw[j]**2
	print w,b,RMSE
	if (RMSE < 200):
		print w,b 
		break
	b = b + learningrate*dLdb/(Gtb**0.5)
	dLdb = 0
	for i in range(58):
		w[i] = w[i] + learningrate*dLdw[i]/(Gt[i]**0.5)
		dLdw[i] = 0
print'--------------------------------------------------------------------------'

fout = open(model,'w')
for i in range(58):
	fout.write(str(w[i]))
	if i == 57:
		fout.write('\n')
	else:
		fout.write(',')

fout.write(str(b))
print'-------------------------------------------------------'









	
	
	
	
	



























