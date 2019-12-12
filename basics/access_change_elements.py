import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7],[8, 9, 10, 11, 12, 13, 14]])

#Get an specific element array[r, c]
print("The element [1, 5] of a is: %d\n" % a[1, 5])

#Printing the elemnts using nested for loops
print("Printing the elments using nested for loops:")
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        print(a[i, j])
print("\n")

#Get specific row
print("The second row is: %s\n" % (a[1, :],))

#Get specific column
print("The third column is: %s\n" % (a[:, 2], ))

#Get a pattern of columns/rows [startindex:endindex:stepsize]
print("The even elements of the first row are: %s\n" % (a[0, 1:6:2]))

#Assign values
a[1, 5] = 20
a[:, 2] = 4
a[:, 6] = [6, 7]
print("The new vector is: %s\n" % (a))


#3d example
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Un arreglo 3d:\n%s\n" % (b))
print("Accessing element of b[1, 1, 0]: %d\n" % b[1,1,0])
print("Accessing elements of b[1, 1, :]:\n%s\n" % b[1,1,:])
b[0, 1, 0] = 14
b[1, 1, :] = [15, 16]
print("The new b is:\n %s" % b)


