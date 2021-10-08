import numpy

a = numpy.array([[1, 2, 3], [4, 5, 6]])

newArray = numpy.append(a, [[50, 60, 70]], axis = 0)

print(newArray)