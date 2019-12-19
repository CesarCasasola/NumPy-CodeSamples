import numpy as np

#Element wise arithmetic
a = np.array([1,2,3,4])
print("Element wise sum +=2:\n%s\n" % (a + 2))

print("Element wise sub a - 2:\n%s\n" % (a-2))

print("Element wise mult a * 2:\n%s\n" % (a * 2))

print("Element wise div a / 2:\n%s\n" % (a/2))

print("Element wise pow a ** 2:\n%s\n" % (a ** 2))

#Suming same size arrays
b = np.array([[7, 8], [9, 10]])
c = np.array([[5, 4], [2, 3]])
print("Suming same size arrays:\nb:\n%s\nc:\n%s\nb+c:\n%s\n" % (b, c, (b+c)))

#Element wise trig operations
print("Sin of a, np.sin(a): \n%s\n" % (np.sin(a)))
print("Cos of a, np.cos(a):\n%s\n" % (np.cos(a)))
