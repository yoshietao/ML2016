import math

fin = open('train.csv','r')

rawdata = []

for line in fin:
		rawdata.append(line.strip().split(','))
#print rawdata
fin.close()

datapm = []
datapm10 = []
count = 0
countt = 0
divide = 0
# 10 pm2.5 feature

for i in range(1,4321):
	if (i-10)%18 == 0:      #search pm2.5 line
		for j in range (3,27):	
			datapm.append(rawdata[i][j])
			count = count + 1
		if i == 352:
			divide = count
	if (i-9)%18 == 0:
		for j in range (3,27):	
			datapm10.append(rawdata[i][j])
#print datapm
print count  #5760
print divide #480

pm = []
for i in range(count/divide): #count/divide = 12
	for j in range(divide-9):
		pm.append(datapm[j:j+10])
		countt = countt + 1

pm10 = []
for i in range(count/divide): #count/divide = 12
	for j in range(divide-9):
		pm10.append(datapm10[j:j+10])
#------------------------moredata-------------------------
#------------------------diff2----------------------------
y = []
for i in range(countt):
	y.append(0)

w = []
for i in range(5):
	w.append(0)
w[0] = 2.5
w[1] = 0.9			#9pm2.5
w[2] = 0.125		#(9-8)pm2.5	
w[3] = 0.125		#(9-8)pm10
w[4] = 0.125

learningrate = 150

dLdw = []
for i in range(5):
	dLdw.append(0)

Gt = []
for i in range(5):
	Gt.append(0)

lambbbda = 0.5

while True:
	for i in range (countt):
		y[i] = w[0] + w[1]*float(pm[i][8]) + w[2]*(float(pm[i][8])-float(pm[i][7])) + w[3]*(float(pm10[i][8])-float(pm10[i][7]))+w[4]*(float(pm[i][8])-2*float(pm[i][7])+float(pm[i][6]))+lambbbda*(w[0]**2+w[1]**2+w[2]**2+w[3]**2)

		dLdw[0] = dLdw[0]+(float(pm[i][9])-y[i])*(-2)+2*lambbbda*w[0]
		dLdw[1] = dLdw[1]+(float(pm[i][9])-y[i])*(-2)*float(pm[i][8])+2*lambbbda*w[1]
		dLdw[2] = dLdw[2]+(float(pm[i][9])-y[i])*(-2)*(float(pm[i][8])-float(pm[i][7]))+2*lambbbda*w[2]
		dLdw[3] = dLdw[3]+(float(pm[i][9])-y[i])*(-2)*(float(pm10[i][8])-float(pm10[i][7]))+2*lambbbda*w[3]
		dLdw[4] = dLdw[4]+(float(pm[i][9])-y[i])*(-2)*(float(pm[i][8])-2*float(pm[i][7])+float(pm[i][6]))+2*lambbbda*w[2]

		Gt[0] = Gt[0] + dLdw[0]*dLdw[0]
		Gt[1] = Gt[1] + dLdw[1]*dLdw[1]
		Gt[2] = Gt[2] + dLdw[2]*dLdw[2]
		Gt[3] = Gt[3] + dLdw[3]*dLdw[3]
		Gt[4] = Gt[4] + dLdw[4]*dLdw[4]
			#complete summing the Loss derivative(dLdw[0~9])
	print dLdw
	if((abs(dLdw[0]) < 0.01) & (abs(dLdw[1]) < 0.01) & (abs(dLdw[2]) < 0.01) & (abs(dLdw[3]) < 0.01) & (abs(dLdw[4]) < 0.01)):
		print w
		break

	for i in range(5): # new w[0~4]
		w[i] = w[i] - learningrate*dLdw[i]/math.sqrt(Gt[i])
		dLdw[i] = 0


fin = open('test_X.csv','r')
data = []
for line in fin:
		data.append(line.strip().split(','))
fin.close()

datapmm = []
pmm10 = []
for i in range(0,4320):
	if (i-9)%18 == 0:      #search pm2.5 line	
		datapmm.append(data[i][2:11])
	if (i-8)%18 == 0:      #search pm2.5 line	
		pmm10.append(data[i][2:11])
for i in range(240):
	y[i] = 0

fout = open('diff121.csv','w')
fout.write('id,value\n')
for i in range(240):
	y[i] = w[0] + w[1]*float(datapmm[i][8]) + w[2]*(float(datapmm[i][8])-float(datapmm[i][7])) + w[3]*(float(pmm10[i][8])-float(pmm10[i][7]))+w[4]*(float(datapmm[i][8])-2*float(datapmm[i][7])+float(datapmm[i][6]))+lambbbda*(w[0]**2+w[1]**2+w[2]**2+w[3]**2)

	fout.write('id_')
	fout.write(str(i))
	fout.write(',')
	fout.write(str(y[i]))
	fout.write('\n')