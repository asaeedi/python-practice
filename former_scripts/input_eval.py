# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
sep='' removes the separation between different blocks of printing
end='' removes the enter at the end of the line, so that make you able to concatenate results of two print functions 
'''
temp = eval(input('Insert the temperature in Celsius: '))
print('The temperature in Celsius is {},'.format(temp), ' which in Fahrenheit is ', (9/5)*temp + 32, '.', sep = '')

