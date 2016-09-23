import numpy as np
import sys

col = sys.argv[1]
filename = sys.argv[2]
  
file = open(filename,'r')

A = []

for line in file:
	A.append(line.strip().split(' '))
file.close()

print A

Acol = []

for x in range(0,500):
	Acol.append(float(A[x][int(col)]))

print Acol

Acol=sorted(Acol)

print Acol
print Acol[499]

fout = open('ans1.txt','w')

for i in range(0,500):
	fout.write(str(Acol[i]))
	if i != 499:
		fout.write(',')
fout.close






