import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
from numpy import square

cat_data = genfromtxt('CAT_5Y.csv', delimiter=',')
tgt_data = genfromtxt('TGT_5Y.csv', delimiter=',')

m = len(cat_data)-1
x_zero = []
x_one = []
y = []


for i in range(1,m):
	x_zero.append(1)
	x_one.append(tgt_data[i][4])
	y.append(cat_data[i][4])

x = [x_zero, x_one]

alpha = 0.0000005
iterations = 1500
theta = [0.0,0.0]

cost_sum = [0,0]
h_of_x = 0
J = 0
J_array = []

#Determine cost function
def get_J():
	cost_sum_temp = 0
	for i in range(0,m-1):
		h_of_x = (theta[0]*x[0][i]) + (theta[1]*x[1][i])
		cost_sum_temp += square(h_of_x - y[i])
	J = (1.0/(2.0*m))*cost_sum_temp
	J_array.append(J)

#Gradient Descent
for i in range(0,1500):
	for j in range(0,len(theta)):
		for i in range(0,m-1):
			h_of_x = (theta[0]*x[0][i]) + (theta[1]*x[1][i])
			cost_sum[j] += (h_of_x - y[i] )*x[j][i]
	theta[0] = theta[0] - (alpha*(1.0/m))*cost_sum[0]
	theta[1] = theta[1] - (alpha*(1.0/m))*cost_sum[1]
	get_J()
	cost_sum = [0,0]


print(theta)

plt.plot(J_array)
plt.show()
