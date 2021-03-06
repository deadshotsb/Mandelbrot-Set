import numpy
import matplotlib.pyplot as argplane


def rec(Re,Im,mx):# for generating the recursive condition
    c=complex(Re,Im)
    z=0.0j#base condition
    for i in range(mx):
        z=z*z+c
        if z.real*z.real+z.imag*z.imag>=4:
            return i
    return mx

columns=1000#setting an arbitrary division factor of columns

rows=1000#setting an arbitrary division factor of rows

result=numpy.zeros([rows,columns])# initialising a set of coordinates


for row_index,Re in enumerate(numpy.linspace(-2,1,rows)):
    for column_index,Im in enumerate(numpy.linspace(-1,1,columns)):
        result[row_index,column_index]=rec(Re,Im,200)

argplane.figure(dpi=100)#regulating the resolution of image

argplane.imshow(result.T,cmap='twilight',interpolation='bilinear',extent=[-2,1,-1,1])#plotting the graph

argplane.show()#displaying on the screen