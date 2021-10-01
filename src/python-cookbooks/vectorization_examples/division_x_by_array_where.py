import numpy as np

arr = np.array([4, 11, 13, 18, 0], dtype=float)

arr_divided = np.divide(46, arr, out=np.zeros_like(arr), where=arr != 0)

print(arr_divided)


arr_log = np.log(arr_divided, where=arr_divided!=0)
print(arr_log)

arr_sqrt = np.sqrt(arr_log)
print(arr_sqrt)



#
# arr2 = np.log(2 / arr)
# # arr3 = np.log(np.divide(2,arr, where=arr != 0))
#
#
# # arr4 = np.sqrt(arr2)
# #
# # np.sqrt(np.log(self.total.sum(axis=1)) / x, where=self.total != 0)
#
# print(arr2)
# # print(arr3)
#
# # print(arr4)
#
#
#
# print(len(arr), len(arr2))

