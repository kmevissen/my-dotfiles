import numpy as np

rows = 3
columns = 5
values = np.zeros((rows, columns))
print(values)

print('\n')
values = np.zeros((rows, columns))
values[0,0] += 1
print(values)

print('\n')
values = np.zeros((rows, columns))
values[:] += [[1, 2, 3, 4, 5], [6,7,8,9,10], [11,12,13,14,15]]
print(values)


print('\n')
values = np.zeros((rows, columns))
values[:] += [[1, 2, 3, 4, 5], [6,7,8,9,10], [11,12,13,14,15]]
print(values.sum(axis=1))



print('\n')
print(np.log(values.sum(axis=1) / values))
