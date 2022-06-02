# -*- coding: utf-8 -*-

# conditional operators: > < <= >= == !=
# and or not

def say_hello():
    print('Hello World!')
    
print('Print before function')
say_hello()
print('Print after function')
    

def draw_square():
    print('*' * 15)
    print('*', ' '*11, '*')
    print('*', ' '*11, '*')
    print('*' * 15)
    
draw_square()
print('')
print('')
draw_square()


#%% Arguments
def draw_square_LW(L, W):
    print('*' * L)
        
    for j in range(W-2):
        print('*', ' '*(L-4), '*')
    
    print('*' * L)
    print('')
    print('')
  
    
draw_square_LW(10, 5)    

#%% Return values
def upperCase(string):
    return(string.upper())

upper_word = upperCase('hello world! I am Python!')    
print(upper_word)
upperCase('hello world! I am Python!')


#%% Return multiple values
def area_circ(r):
    from math import pi
    area = 2*pi*r
    circ = pi*r**2
    return([area, circ])

r = 20    
A, C = area_circ(r)    
print('A circle with r = {} has an area of {:.2f} and a circumference of {:.2f}'.format(r, A, C))    


#%% Default arguments and keyword arguments
def multiple_print(string, n=1):
    print(string * n)
    print()
    
multiple_print('Hello', 5)
multiple_print('Hello')

    
#%% Global variables
'''
In order to change the value of a global variable, it is needed to use the 'global' keyword and then modify it
'''
def reset():
    global time_left
    time_left = 0
def print_time():
    print(time_left)


time_left = 30
print(time_left)
reset()
print_time()


#%%
'''
1. Write a function called rectangle that takes two integers m and n as arguments and prints
out an mxn box consisting of asterisks. Shown below is the output of rectangle(2,4)
****
****
'''

def rectangule(L, W):
    for j in range(W):
        print('*' * L)
        
rectangule(20, 5)


#%%
'''
2. (a) Write a function called add_excitement that takes a list of strings and adds an exclamation
point (!) to the end of each string in the list. The program should modify the
original list and not return anything.
'''
def add_excitement(str_list):
    for i in range(len(str_list)):
        str_list[i] = str_list[i] + '!'

list_1 = ['Ali', 'has', 'two', 'umbrellas']
print(list_1)
add_excitement(list_1)
print(list_1)
add_excitement(list_1)
print(list_1)


#%%
'''
3. Write a function called sum_digits that is given an integer num and returns the sum of the
digits of num.
'''
def sum_digits(num):
    sum_digits = 0
    str_num = str(num)
    str_num.split()
    for str_integers in str_num:
        sum_digits += int(str_integers)
    return sum_digits

num = 999
print('Sum of digits of {} is {}'.format(num, sum_digits(num)))


#%%
'''
4. The digital root of a number n is obtained as follows: Add up the digits n to get a new number.
Add up the digits of that to get another new number. Keep doing this until you get a number
that has only one digit. That number is the digital root.
For example, if n = 45893, we add up the digits to get 4 + 5 + 8 + 9 + 3 = 29. We then add up
the digits of 29 to get 2 + 9 = 11. We then add up the digits of 11 to get 1 + 1 = 2. Since 2 has
only one digit, 2 is our digital root.
'''

def digital_root(n):
    dig_root = str(n)
    while(len(dig_root)>1):
        sum_digits = 0
        dig_root.split()
        for integers in dig_root:
            sum_digits += int(integers)
        dig_root = str(sum_digits)
    
    return int(dig_root)

num = 45893
digital_root(num)
print('The digital root of {} is {}'.format(num, digital_root(num)))
            
#%%
'''

'''       
    
    
    



