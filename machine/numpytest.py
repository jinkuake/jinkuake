import numpy as np
a = np.array([[3,4,5,6,7,8],
              [4,5,6,7,8,9]])
print(a.shape)
b = a.reshape(3,4)
print(b)
c = a.flatten()
print(c)
d = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])

print(d[:,1:3])

a = np.array(['a','s','d','f'])
b = np.array([1,2,3,4])
c = np.array([4,5,6,7])
d = np.eye(4)
print(a.dtype)
print(a.ndim)
arr = np.array([1, 2.2, 3, 4.9])
a = arr.astype(int)
print(a)
print(arr.dtype)

e = np.arange(12).reshape(2, 3, 2)
print(e)
e_0 = e.sum(axis=0)
print(e_0)

e_1 = e.sum(axis = 1)
print(e_1)