import numpy as np

stats = np.array([[1,2,3],[4,5,6]])
print("stats array:\n%s\n" % stats)

#Find the min value
print("The min value: np.min(stats):\n%s\n" % (np.min(stats)))
print("The min value in axis 1: np.min(stats, axis=1):\n%s\n" % (np.min(stats, axis=1)))
print("The min value in axis 0: np.min(stats, axis=0):\n%s\n" % (np.min(stats, axis=0)))

#Max value
print("The max value: np.max(stats, axis=0):\n%s\n" % (np.max(stats, axis=0)))

#Sum of the values
print("The sum of the values of each row: np.sum(stats, axis=1):\n%s\n" % (np.sum(stats, axis=1)))
