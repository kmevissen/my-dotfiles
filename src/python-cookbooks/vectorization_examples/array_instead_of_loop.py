import time
import numpy as np
from math import log10 as lg10

N = 10000000 # Number of records to process
speed = [] # Empty list to store operation speeds (time taken)

l1 = list(100*(np.random.random(N))+1)
print("Length of l1:",len(l1))

a1 = np.array(l1)
print("Shape of a1 object:",a1.shape)
print("Type of a1 object:",type(a1))

l2=[] # Just a blanck list to append to

t1=time.time()
for item in l1:
    l2.append(lg10(item))
t2 = time.time()
print("With for loop and appending it took {} seconds".format(t2-t1))
speed.append(t2-t1)

t1=time.time()
l2 = [lg10(i) for i in range(1,1000001)]
t2 = time.time()
print("With list comprehension, it took {} seconds".format(t2-t1))
speed.append(t2-t1)

t1=time.time()
a2=np.log10(a1)
t2 = time.time()
print("With direct Numpy log10 method it took {} seconds".format(t2-t1))
speed.append(t2-t1)