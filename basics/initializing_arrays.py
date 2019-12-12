import numpy as np

#All 0s matrix
a = np.zeros(5)
a_3d = np.zeros((4, 4, 2), dtype='int32')
print("Matriz inicializada con np.zeros:\n%s\n" % (a_3d, ))

#All 1s matrix
b = np.ones((9, 6), dtype='int16')
print("Matriz inicializada con np.ones:\n%s\n" % (b))

#Any other number
c = np.full((3, 3), 7)
print("Matrix initialized with np.full:\n%s\n" % (c))

#Identity matrix
print("Identitiy matrix:\n%s\n" % np.identity(4))

#Full like
print("Full like matrix:\n%s\n" % np.full_like(c, 4))

#Random decimal numbers
print("Random initialized array:\n%s\n" % np.random.rand(4, 2, 3))

#Random decimal numbers as sample
print("Random initilized array as sample:\n%s\n" % np.random.random_sample(c.shape))


#Random integers
print("Random int array np.random.randint(startvalue, maxValue, size=(m, n):\n%s\n" % np.random.randint(7, 40, size=(3, 3)))


#Repeat in axis 0
print("Repeat in axis 0: \n%s\n" % np.repeat([[1, 2, 3]], 3, axis=0))

#Repeat in axis 1
print("Repeat in axis 1: \n%s\n" % np.repeat( [[1, 2, 3]], 3, axis=1))

#Challenge matrix
cm = np.ones((5, 5), dtype="int16")
midle = np.zeros((3, 3), dtype="int16")
midle[1, 1] = 9
cm[1:4, 1:4] = midle
print("Challenge matrix:\n%s\n" % cm)

#Be careful when copying arrays
a = np.array([1, 2, 3])
b = a
b[0] = 100
print("b = a, b has a hardlinked copy of a:\na:\n%s\nb:\n%s\n" % (a, b))

a = np.array([1, 2, 3])
b = a.copy()
b[0] = 100
print("b = a.copy(), b has a simple copy of a:\na:\n%s\nb:\n%s\n" % (a, b))

