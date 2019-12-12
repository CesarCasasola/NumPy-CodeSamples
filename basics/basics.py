import numpy as np
import sys
#one dimensional array
a = np.array([1, 2, 3], dtype='int16')
print(a)
print(str(a.ndim) + ' dimensions')

#bidimensional array
b = np.array([[5.0, 3.0, 8.0], [0.05, 4.89, 75.36], [848, 987, 654]])
print (b)
#Get dimension
print(str(b.ndim) + " dimensions\n")

#Get shape
print("Shape of a: %s" % (a.shape, ))
print("Shape of b: %s\n" % (b.shape, ))


#Get datatype
print("Datatype of a: %s" % (a.dtype))
print("Datatype of b: %s\n" % (b.dtype))

#Get size of every item (bite size)
print("Size in bytes of the items of a: %d" % (a.itemsize))
print("Size in bytes of the items of b: %d\n" % (b.itemsize))

#Get size of the array (number of elements mxn)
print("Size of array a: %d" % (a.size))
print("Size of array b: %d\n" % (b.size))

#Get the total size of the array (in bytes)
print("Total size of the array a: %d" % (a.size * a.itemsize))
print("Total size of the array b: %d\n" % (b.size * b.itemsize))

#Get the total size of the array (in bytes) built in function
print("Total size of the array a: %d" % (a.nbytes))
print("Total size of the array b: %d\n" % (b.nbytes))

#tridimensional array
t = np.array([
        [[45.6, 34.2, 69.7],
          [58.6, 473.2, 78.2]],
        [[47, 65, 87.2],
          [21.3, 24.5, 36.8]]
    ], dtype='float16')
print(t)
print("Total elements of t: %d\n" % t.size)
