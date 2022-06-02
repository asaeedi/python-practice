# -*- coding: utf-8 -*-

import math
'''
Write a program that counts how many of the squares of the numbers from 1 to 100 end in a 1.
'''

count = 0
for i in range(1, 101):
    if (i**2)%10 == 1:
        print(i, end = ' ')
        count += 1
 
print('')       
print('{} squares of numbe from 1 to 100 end in a 1'.format(count))


'''
Write a program that asks the user to enter a value n, and then computes (1+ 1 2 + 1 3 +· · ·+ 1n)−
ln(n). The ln function is log in the math module.
'''
num = 10 #eval(input('Enter a number: '))
sum_inv = 0
for j in range(1, num+1):
    sum_inv += 1/j
    
sum_inv = sum_inv - math.log(num)
print('The expected expression is: {}'.format(sum_inv))    
    

'''
Write a program to compute the sum 1 − 2 + 3 − 4 + · · · + 1999 − 2000
'''
sum_sub = 1
for k in range(2, 2001):
    if k%2 == 0:
        sum_sub -= k
    else:
        sum_sub += k
        
print('sum_sub is {}'.format(sum_sub))        
    

'''
Write a program that swaps the values of three variables x, y, and z, so that x gets the value
of y, y gets the value of z, and z gets the value of x.
'''
x = 1
y = 2
z = 3
print('x={}, y={}, z={}'.format(x, y, z))

x, y, z = y, z, x
print('x={}, y={}, z={}'.format(x, y, z))

# solution 2
x = 1
y = 2
z = 3
print('solution 2:')
print('x={}, y={}, z={}'.format(x, y, z))
temp_x = x
x = y
y = z
z = temp_x
print('x={}, y={}, z={}'.format(x, y, z))


'''
Write a program to count how many integers from 1 to 1000 are not perfect squares, perfect
cubes, or perfect fifth powers.
'''
n_sq = 0
n_cube = 0
n_fifth = 0
i=1
while (i**2 <= 1000) or (i**3 <= 1000) or (i**5 <= 1000):
    if i**2 <= 1000:
        n_sq += 1
    if i**3 <= 1000:
        n_cube += 1
    if i**5 <= 1000:
        n_fifth += 1
    i += 1
        
print('Between 1 and 1000, there are {} perfect squares, {} perfect cubes, and {} perfect fifth powers.'.format(n_sq, n_cube, n_fifth))        


'''

'''



