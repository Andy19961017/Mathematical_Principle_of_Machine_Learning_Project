import numpy as np

a=[
[0,0,0,1,1,1],
[0.1,0,0,0,0,0],
[0.9,0,0,0,0,0],
[0,0.2,0.4,0,0,0],
[0,0.3,0.5,0,0,0],
[0,0.5,0.1,0,0,0]
]

v,w=np.linalg.eig(a)

for s in v:
	print('v',s)
print('w',w)

d=a
print(1)
print(np.array(a))
for i in range(30):
	d=np.dot(d,a)
	print(i+2)
	print(d)