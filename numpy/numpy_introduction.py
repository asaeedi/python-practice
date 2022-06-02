# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:25:52 2019

@author: Ali Saeedi
"""

# Numpy
import numpy as np
 
a = np.arange(20).reshape(4,5)
L = a.shape

print(a)
print('Number of axes is ', a.ndim)
print('Number of elements in dimensions: ', a.shape)
print('The rank of the matrix is ', len(a.shape))
print('Total number of elements is ', a.size)
print('Data type is ', a.dtype)
print('Size of each item in Byte is ', a.itemsize)


#%% making arrays in Python
x = np.array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
print(x)

x = np.array([(1.5, 3, 4.5), (2, 4, 6)], dtype='complex')
print(x)

# note the need to an extra pair of paranthesis
z = np.zeros((6, 3))
print(z)
print('')

z = np.ones((3, 7))
print(z)

e = np.empty((4, 4))
print(e)
print('')

zl = np.zeros_like(x, dtype='int')
print('zl = \n', zl)
print('')

ol = np.ones_like(x, dtype='int')
print('ol = \n', ol)
print('')

# the arange method works like range in lists
x = np.arange(11)
print('x = ', x)
y = np.arange(20, 30)
print('y = ', y)
z = np.arange(11, 50, 4)
print('z = ', z)
print('')

#%% plotting a sinusoidal waveform with matplotlib
# determine the number of elemenst by linspace method
from numpy import pi
np.set_printoptions(precision=2, linewidth=150)
x = np.linspace(0, pi, 500, endpoint=True)
f = 3
y = np.sin(2*pi*f*x)

# plot the vector
import matplotlib.pyplot as plt
plt.figure(1, figsize=[8, 5])
plt.title('A simple plot in Python')
plt.plot(x, y, 'b', linewidth=2)
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude ($\mu$V)')
plt.show()


#%% Supplots in Python
# for plotting in a separate window use the command 'matplotlib qt' in Python Shell
# for inline plotting use '%matplotlib inline' in Python Shell

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()


#%% Basic operations on arrays
a = np.array([1, 5, 4, 2]).reshape(2, 2)
b = np.arange(10,50, 10).reshape(2, 2)
print(a)
print(b)
print('')

# elementwise operations
print('a+b is:\n', a+b)
print('')

print('a-b is:\n', a-b)
print('')

# note that the '*' is the element-wise product operator in Python (in contrast to MATLAB)
print('a*b (elementwise product) is:\n', a*b)
print('')

# matrix product
print('a.b (matrix product) is:\n', np.dot(a, b))
print('')


#%% Unary operations
r = np.random.randint(1, 21, (4, 10))
print(r)
print('')

print('sum of all elemests is :\n', np.sum(r))
print('')

print('sum of elemests in rows is :\n', np.sum(r, axis=0))
print('')

print('sum of elemests in columns is :\n', np.sum(r, axis=1))
print('')

print('min of elemests in rows is :\n', np.min(r, axis=0))
print('')

print('max of elemests in columns is :\n', np.max(r, axis=0))
print('')

#%% Call functions from np
def func(x, y):
    return 2*x-y

a = np.random.randint(1, 11, (3, 5))
b = np.random.randint(1, 11, (3, 5))
print(a)
print('')

print(b)
print('')

c = func(a, b)
print(c)
print('')

# interesting way of input.. it's like a meshgrid
res = np.fromfunction(func, (3, 10), dtype=int)
print(res)


#%% Slicing, indexing, iterating
#a = np.random.randint(1, 60, (4, 6))
a = np.array([[31, 14, 10, 38, 25, 30],
             [17, 18, 19, 32, 17, 10],
             [56, 50, 35, 48, 41, 38],
             [33, 33, 51, 25,  4, 43]])
print(a)
print('')

print(a[1, 2])
print(a[0, -1]) # last column in the first row
print(a[-1, -1]) # last value

print(a[1:3, 0:4])
print('')

print(a[:, -1])
print('')

print(a[:2, 3:])
print('')

# When fewer indices are provided than the number of axes, the missing indices are considered complete slices:
print(a[3])
print('')

# Iterating over multidimensional arrays is done with respect to the first axis:
for row in a:
    print(row)
print('')
    
# make a ndarray flat using the flat method:
from copy import copy
b = copy(a)
for i in b.flat:
    print(i, end=' ')
    
    
#%% More methods on arrays
#a = np.random.randint(1, 60, (4, 6))
a = np.array([[31, 14, 10, 38, 25, 30],
             [17, 18, 19, 32, 17, 10],
             [56, 50, 35, 48, 41, 38],
             [33, 33, 51, 25,  4, 43]])
print(a)
print('')
    
print('Max of a is {} which is {}th index of a'.format(a.max(), a.argmax()) )
print('Args max along axis 0 are ', a.argmax(axis=0))
print('Args min along axis 1 are ', a.argmin(axis=1))

b = np.copy(a)
b.sort(axis=0, kind='quicksort')
print('Sorted a is :\n', b)
print('Sort index of b is :\n', a.argsort(axis=0))   
    


#%% More on array methods
r = np.random.randint(1, 100, (5, 8))
r_tr = np.transpose(r)
print(r)
print(np.shape(r))

print('')

print(r_tr)
print(np.shape(r_tr))

#%% horizontal and vertical stacking
a = 10*np.random.random((2, 3))
b = 10*np.random.random((2, 3))
c = 10*np.random.random((2, 3))

print('a is\n', a)
print('')
print('b is\n', b)
print('')
print('c is\n', c)
print('')

vstack = np.vstack((a, b, c))
print(vstack)
print('')

hstack = np.hstack((a, b, c))
print(hstack)


#%% Split horizontally and vertically
x = np.random.randint(1, 100, (4, 12))
print(x)
print('')

a, b, c = np.hsplit(x, 3)
print(a)
print('')
print(b)
print('')
print(c)
print('')

d, e = np.vsplit(x, 2)
print(d)
print('')
print(e)
print('')


#%% Question methods
a = np.random.randint(20, 400, (6, 10))
print('a is\n', a)

print('if all elements of a are greater than 10? ', np.all(a>10))
print('if any element in a is less 100?', np.any(a<100))
print('where are the elements less than 70', np.where(a<70))

#%% Some more functions on ndarrays

# range or peak-to-peak
a = np.random.randint(1, 99, (4, 8))
print(a)
print(np.ptp(a, axis=0))
print('')
print(np.ptp(a, axis=1))
print('')

# inner-product
v = np.random.randint(1, 10, (1, 3))
w = np.random.randint(1, 10, (1, 3))

print(v)
print(w)

print(np.inner(v, w))
print(np.sum(v[:]*w[:]))


#%% Working with complex numbers
a = np.array([[1+2j, -3-3j, 5j], [9+4j, 5-1j, 4]], dtype='complex')
print(a)
print('')
print('real part of a is \n', np.real(a))

print('')
print('imagairy part of a is \n', np.imag(a))


#%% Fancy indexing and tricks
a = np.array(range(1, 16))**2
print(a)
print('')

i = np.array([0, 3, 8, 1, 10])
print(a[i])
print('')

j = np.array([[1, 4], [14, 3], [8, 9]])
print(a[j])
print('')

palette = np.array( [ [0,0,0], # black
                     [255,0,0], # red
                     [0,255,0], # green
                     [0,0,255], # blue
                     [255,255,255] ] ) # white

image = np.array( [ [ 0, 1, 2, 0 ],
                    [ 0, 3, 4, 0 ] ] )
    
print(palette[image])    
print('')


#%% Still indexing and slicing
a = np.arange(12).reshape(3, 4)
print(a)

i = np.array([[0, 1],
              [1, 2]])
    
j = np.array([[2, 1],
              [3, 3]])

print('')

print(a[i,j])
print('')

print(a[i, 2])
print('')


print('Note this slicing...\n', a[:, j])
print('')

#%% 

time = np.linspace(20, 145, 5)
data = np.sin(np.arange(20)).reshape(5,4)

print('time = :', time)
print('\n\ndata is :\n', data)
ind = np.argmax(data, axis=0)
print(ind)

time_max = time[ ind]
print(time_max)


#%%
import numpy as np
import matplotlib.pyplot as plt
def mandelbrot( h,w, maxit=20 ):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
    c = x+y*1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)
    for i in range(maxit):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2 # who is diverging
        div_now = diverge & (divtime==maxit) # who is diverging now
        divtime[div_now] = i # note when
        z[diverge] = 2 # avoid diverging too much
    
    return divtime

plt.imshow(mandelbrot(400,400))
plt.show()


#%% Histograms
from matplotlib import pyplot as plt
mu, sigma = 10, 1
dist = np.random.normal(loc=mu, scale=sigma, size=2000)
plt.figure(1, figsize=(10,4))
plt.subplot(121)
plt.hist(dist, bins=50, density=True, color='g')
plt.xlabel('Spike rate (/sec)')
plt.ylabel('Probablity')

# plot the histogram and get the n and bins
(n, bins) = np.histogram(dist, bins=50, density=True)
plt.subplot(122)
plt.plot(0.5*(bins[1:] + bins[:-1]), n, '.-r')
plt.xlabel('Spike rate (/sec)')
plt.show()


#%% Data types in Python
a = np.array([0, 1, 2, 3], dtype='float64')
print(a)
print('')

b = np.array([2.34, 14.54, 34.98], dtype='int')
print(b, '\n')

c = np.float64(a)
print('c =', c, '\n')

d = np.int64(b)
print('d =', d, '\n')

d = np.dtype(int)
print(d)

#%% Miscelaneous
a = np.array([1, 4, 3, 8, 10])
print(a)
print(type(a))
b = a.tolist()
print(b)

# another way
print(list(a))

# fill all indices with a single value
a.fill(-3)
print(a)

# concatenate two or more vectors
a = np.array([0, 9, 6], float)
b = np.array([-1, 3.7, -12, 8], float)
c = np.array([1, 2], float)
d = np.concatenate((a, b, c))
print(d)

#%% test if an array contains NaN or infinite values
a = np.array([1, np.NaN, 3+2j, np.Inf])
print('is a NaN? \n', np.isnan(a))
print('')

print('is a finite? \n', np.isfinite(a))
print('')

#%% Array item selection by boolean arrays
a = np.random.randint(10, 101, 20)
print(a)

sel_a = a[a>=50]
print('items greater than 50:\n', sel_a)

sel_a = a[a<20]
print('items less than 20:\n',sel_a)

sel_a = a[np.logical_and(a>=15, a<=40)]
print('items between 15 and 40:\n',sel_a)

#%% Some Linear Algebra using np.linalg
a = np.array([[4, 2, 0], [9, 3, 7], [1, 2, 1]], float)
print(a)

print('Det of a is {:.2f}'.format(np.linalg.det(a)))
print('')

b = 4*np.eye(3)
print(b)
print('Det of b is {:.2f}'.format(np.linalg.det(b)))
print('')

invA = np.linalg.inv(a)
print('A invers is \n', invA)
print('')

print('', np.dot(a, invA))


# eigenvalues and eigenvectors
eigvals, eigvecs = np.linalg.eig(a)
print(eigvals)
print('')
print(eigvecs)


