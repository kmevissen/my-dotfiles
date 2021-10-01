import numpy as np

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

for i in zip(arr1, arr2):
  print(i)



arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[100, 200, 300], [400, 500, 600] ])

for i in zip(arr1, arr2):
  print(i)







for i in ([(s + 1, t - s + 1) for s, t in zip(arr1, arr2)]):
  print(i)