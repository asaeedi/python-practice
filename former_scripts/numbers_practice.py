# -*- coding: utf-8 -*-

from random import randint
import math

'''
A random number between a and b
'''
a = 1
b = 10

print('A random number between {} and {} : {}'.format(a, b, randint(a, b)))


# sin and pi
print('Pi is roughly ', math.pi)
print('Sin(30) is ', math.sin(30*math.pi/180))

print(abs(-34.76))
print(round(19.769, 2))
print(math.floor(23.27))
print(math.ceil(144.01))

# Write a program that generates and prints 50 random integers, each between 3 and 6

for i in range(50):
    print(randint(3, 6), end=' ')

print('')

'''
Write a program that generates a random number, x, between 1 and 50, a random number y
between 2 and 5, and computes x to the power of y.
'''
x = randint(1, 50)
y = randint(2, 5)
print(x, y, x**y)

'''
Write a program that generates a random decimal number between 1 and 10 with two decimal
places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00.
'''
dec_rand = (randint(0, 999))/100
print('A decimal randrom number:', dec_rand)

'''
Write a program that generates 50 random numbers such that the first number is between 1
and 2, the second is between 1 and 3, the third is between 1 and 4, . . . , and the last is between
1 and 51.
'''

for j in range(50):
    print('Random number between {} and {}: {}'.format(1, j+2, randint(1, j+2)) )

'''
Write a program that asks the user for a number of seconds and prints out how many minutes
and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. [Hint: Use the //
operator to get minutes and the % operator to get seconds.]
'''
t_in_sec = 123 #eval(input('Enter time in seconds: '))
mins = t_in_sec // 60
secs = t_in_sec % 60
print('{} seconds is {} minute(s) and {} second(s)'.format(t_in_sec, mins, secs))

'''
Write a program that asks the user for a number and prints out the factorial of that number.
'''

num = 4
fact = 1
for i in range(num):
    fact *= (i+1)

print('{}! = {}'.format(num, fact))

'''
Write a program that draws “modular rectangles” like the ones below. The user specifies the
width and height of the rectangle, and the entries start at 0 and increase typewriter fashion
from left to right and top to bottom, but are all done mod 10. Below are examples of a 3 × 5
rectangle and a 4 × 8.
'''

width = 8
height = 4
for k in range(width*height):
    if ((k+1)%width)!=0:
        print(k%10, ' ', end='')
    else:
        print(k%10, sep=' ', end='')        
        print('')
          










