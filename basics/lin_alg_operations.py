import numpy as np


#Matrix multiplication
a = np.ones((3, 2))
b = np.full((2, 3), 2)
print("Matrix mult, np.matmult(a, b)\na:\n%s\nb:\n%s\na*b:\n%s\n" % (a, b, (np.matmul(a, b))))

#Find the determinate of an identity
c = np.identity(3)
print("The determinant of identity(3) np.linalg.det(c):\n%s\n" % (np.linalg.det(c)))

#Find the inverse of an identity
print("The inverse of identity(3) is np.linalg.inverse(c):\n%s\n" % (np.linalg.inv(c)))

