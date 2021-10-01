import numpy as np
import time

speed = [] # Empty list to store operation speeds (time taken)
LENGTH = 1000
arr = np.arange(1000)


def myfunction(x):
  return np.sqrt(x)
m = np.vectorize(myfunction)

t1=time.time()
for i in arr:
  myfunction(i)
t2 = time.time()
print("With for loop and appending it took {} seconds".format(t2-t1))
speed.append(t2-t1)


t1=time.time()
m(arr)
t2 = time.time()
print("With for loop and appending it took {} seconds".format(t2-t1))
speed.append(t2-t1)


