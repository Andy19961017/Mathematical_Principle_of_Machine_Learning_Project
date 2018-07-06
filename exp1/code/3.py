from sys import argv
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import random as rd
import math

true_theta=int(argv[3])-1
theta_intersted=int(argv[4])-1
num_of_iteration=int(argv[5])

class random_matrix:
	def __init__(self):
		file1 = open('../csv/'+argv[1]+'.csv' ,"r")
		data1 = csv.reader(file1 , delimiter= ",")
		file2 = open('../csv/'+argv[2]+'.csv' ,"r")
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

		self.W=W
		self.F=F
		self.num_of_node=num_of_node
		self.num_of_theta=num_of_theta
		self.W_product=self.get_one_matrix_sample()
		self.count=1

	def get_observation(self):
		X=np.zeros((self.num_of_node)).astype(int)
		for i in range(self.num_of_node):
			X[i]=0 if rd.random()<self.F[true_theta+i*self.num_of_theta,0] else 1
		return X

	def get_one_matrix_sample(self):
		W_hat=np.zeros((self.num_of_node+1,self.num_of_node+1))
		W_hat[:-1,:-1]=self.W
		W_hat[-1,-1]=1
		X=self.get_observation()
		for i in range(self.num_of_node):
			print(X[i], self.F[i*self.num_of_theta+true_theta,X[i]], self.F[i*self.num_of_theta+theta_intersted,X[i]])
			W_hat[i,-1]=math.log( self.F[i*self.num_of_theta+true_theta,X[i]] / self.F[i*self.num_of_theta+theta_intersted,X[i]] )
		print('One sample:\n', W_hat)
		return W_hat

	def multiply_once(self):
		self.W_product=np.dot(self.W_product,self.get_one_matrix_sample())
		self.count+=1
		# print(self.count,'matrices:')
		# print(self.W_product)

if len(argv)!=6:
	print('Usage: python3 3.py W F true_theta theta_intersted num_of_iteration')
rm=random_matrix()
for i in range(num_of_iteration-1):
	rm.multiply_once()