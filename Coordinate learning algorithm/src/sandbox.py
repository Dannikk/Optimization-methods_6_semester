import numpy as np


fff = lambda num: np.random.uniform(-1, 1, num)
ar = np.random.binomial(size=10, n=1, p=0.2)
print(ar)
# ar = 2 * ar - np.ones(10)
#
# arr = fff(5)
# print(arr, type(arr))
# print(ar, type(ar))
#
# a = np.empty(2)
# a.fill(1)
# print(a)