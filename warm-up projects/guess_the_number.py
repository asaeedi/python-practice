# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from numpy import round

num = int(input('Insert a number in the range of [0 100] to be guessed: \n'))

a = 0
b = 100
step = 50

guess = step

resp = 'n'

while b-a > 1:
    resp = input('Is it > than {} ?\n'.format(guess))    
    if resp == 'y':
        a = guess
        step = step/2
        guess =  int(round(a + step))
    elif resp == 'n':
        b = guess
        step = step /2
        guess = int(round(a + step))
    else:
        resp = input('Only \'y\' or \'n\'..\n')            
else:
    resp = input('Is it {} ?'.format(a))
    if resp == 'y':
        print('Then the number is {} !'.format(a))
    else:
        print('Then the number is {} !'.format(b))
        
    
    


