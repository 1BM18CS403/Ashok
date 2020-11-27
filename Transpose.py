#List comprehensionMethod
def transpose(l1,l2):
    
    l2 =[[row[i] for row in l1] for i in range(len(l1[0]))]
    return l2

l1 = [[4, 5, 3, 9], [7, 1, 8, 2], [5, 6, 4, 7]]
l2 = []
print(transpose(l1,l2))

#Using Numpy
import numpy  

mat = [[4, 5, 3, 9], [7, 1, 8, 2], [5, 6, 4, 7]]
trans = numpy.transpose(1ma)
print(trans)
