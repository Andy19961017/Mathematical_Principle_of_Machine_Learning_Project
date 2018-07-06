import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import random as rd
import math

def parse_parameters():
	file1 = open('../csv/'+'W5'+'.csv' ,"r")
	data1 = csv.reader(file1 , delimiter= ",")
	file2 = open('../csv/'+'F5'+'.csv' ,"r")
	data2 = csv.reader(file2 , delimiter= ",")
	# read weight
	W=[]
	row_num=0
	for row in data1:
		# print(row)
		if row_num != 0:
			r=[]
			for i in range(len(row)):
				r.append(row[i])
			W.append(r)
		row_num+=1
	W.pop()
	W=np.array(W).astype(float)
	num_of_node=W.shape[0]
	# print()
	# read PDF
	F=[]
	row_num=0
	for row in data2:
		# print(row)
		if row_num != 0 and row_num != 1 and row_num != 2:
			r=[]
			for i in range(1,len(row)):
				r.append(row[i])
			F.append(r)
		row_num+=1
	F.pop()
	F=np.array(F).astype(float)
	num_of_theta=F.shape[0]//num_of_node
	file1.close()
	file2.close()
	return W, F, num_of_node, num_of_theta

W=parse_parameters()[0]
print('det',np.linalg.det(W))
v,w=np.linalg.eig(W)
for s in v:
	print('v',s)
d=W
l=[d]
print(W)
for i in range(1000):
	d=np.dot(d,W)
	for i in range(9):print(d[i])
	l.append(d)
# print(l[-1]+l[-2]+l[-3]+l[-4])
# print(l[-2]+l[-3]+l[-4]+l[-5])
# print(l[-3]+l[-4]+l[-5]+l[-6])
