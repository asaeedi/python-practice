# -*- coding: utf-8 -*-

# conditional operators: > < <= >= == !=
# and or not
 
import math

age = 3.5
if age<2:
    print('You are an infant!')
if 2<=age<10:
    print('You are a child!')
if 10<=age<18:
    print('You are a teenager!')
if age>=18:
    print('You are an adult!')    


time = 201
score = 97

if time >150 and score<1000:
    print('Game continued!')

if not (time<200 or score>500):
    print('Game over!')


grade = 54 #eval(input('Insert your score: '))

if grade>=90:
    print('Score is A')
elif grade>=80:
    print('Score is B')
elif grade>=60:
    print('Score is C')
elif grade>=30:
    print('Score is D')
else:
    print('Score is F')    


'''
Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temperature is in. Your program should convert the temperature to the other unit. The conversions
are F = 9/5C + 32 and C = 5/9(F − 32).
'''
temp = 100 #eval(input('Enter a temperature: '))
unit = 'A'
while not (unit=='f' or unit =='F' or unit=='c' or unit=='C'):
    unit = 'C' #input('Enter unit: c or C for Celcius and f or F for Farenheit: ')


if unit=='c' or unit=='C':
    other_unit = 'F'
    equi_temp = round((9/5)*temp + 32, 2)
elif unit=='f' or unit=='F':
    other_unit = 'C'
    equi_temp = round((5/9)*(temp - 32), 2)
    
print('Temperature {} {} is equivalent to {} {}.'.format(temp, unit, equi_temp, other_unit))


'''
Write a program that asks the user to enter a number and prints out all the divisors of that
number. [Hint: the % operator is used to tell if a number is divisible by something. 
'''
input_num = 122 #eval(input('Enter an integer: '))

sq_num = math.floor(math.sqrt(input_num))

for i in range(0, sq_num):
    if input_num%(i+1)==0:
        print(i+1, input_num//(i+1), end=' ')

print('')
'''
Write a program that asks the user for two numbers and prints Close if the numbers are
within .001 of each other and Not close otherwise.
'''
a = 1.221
b = 1.3201
abs_diff = round(abs(a-b), 5)
if abs_diff < 0.001:
    print('Difference: {}; Close'.format(abs_diff))
else:
    print('Difference: {}; Not close'.format(abs_diff))


    