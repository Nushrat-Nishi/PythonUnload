x = [0, 1, 2, 3.5, 'car', 5, 6, 7, 8]

print("x = ",x)
print("x[2] = ",x[2])
print("x[4][0] = ",x[4][0])
print("x[4][0:2] = ",x[4][0:2])
print("x[-1] = ",x[-1])
print("x[-2] = ",x[-2])
print("x[0:4] = ",x[0:4])

print("----------------------------------------------")
import numpy as np
y = np.array([0, 1, 2, 3.5, 4, 5, 6, 7, 8])
print("y = ",y)

print("Calculate average => np.mean(y) = ",np.mean(y))
print("MAx value => np.max(y) = ",np.max(y))
print("Min value => np.min(y) = ",np.min(y))

print("np.ones(5) = ",np.ones(5))
print("np.zeros(5) = ",np.zeros(5))
print("np.empty(5) = ",np.empty(5))
print("np.linspace(0,6,5) = ",np.linspace(0,6,5))
print("----------------------------------------------")
import matplotlib.pyplot as plt
t = np.linspace(0,1,8)  # here 8
z = np.array([1, 2, 3.5, 4, 5, 6, 7, 8]) # here 8 elements. so it's same
plt.plot(t, z, 'ro')
plt.show()

a = "7"
b = 3
c = 5.0

print("int(a)+b = ", int(a)+b)
print("a+str(b) = ", a+str(b))