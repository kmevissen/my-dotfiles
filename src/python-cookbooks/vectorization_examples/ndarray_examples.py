import numpy as np

k = 10
batches = 5
m = 3

a = np.arange(k)

single_row = np.random.choice(np.arange(k), (batches))

batches_rows_m_columns = np.random.choice(np.arange(k), (batches, m))

# some reshaping
A = np.array([1,2,3,4,5,6])
B = np.reshape(A, (-1, 2))
print(B)
B = np.reshape(A, (1, -1))
print(B)