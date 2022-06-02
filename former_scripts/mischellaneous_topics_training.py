# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:58:31 2019

@author: ga84nag
"""

'''
Miscellaneous topics II
'''

print(str(12))
print(str(3.14))
print(str([1,2,3]))

print('')
print('')

print(int('46'))
print(float('3.14'))
print(int(3.14))

print('')
print('')

print(list(range(10)))
print(list('ali'))


'''
Here is an example that finds all the palindromic numbers between 1 and 10000. A
palindromic number is one that is the same backwards as forwards, like 1221 or 64546.
'''
'''
for i in range(1,10001):
    s = str(i)
    if s==s[::-1]:
        print(s)

'''

'''
Write a program that takes a number num and adds its digits. For instance, given the
number 47, the program should return 11 (which is 4 + 7)
'''
num = 541
str_num = str(num)
list_num = list(str_num)

sum_num = sum([int(item) for item in list_num])
print('sum of digits of {} is {}'.format(num, sum_num))


'''
Write a program that uses list and range to create the list [3,6, 9, . . . , 99].
'''
myList = list(range(3,100,3))
print(myList)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that asks the user to enter a word. Rearrange all the letters of the word
in alphabetical order and print out the resulting word. For example, abracadabra should
become aaaaabbcdrr.
'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

text = 'hgrqabnzcbrxpq'
list_text = list(text)
list_text.sort()
sorted_text = ''.join(list_text)
print(text)
print(sorted_text) 

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that uses a boolean flag variable in determining whether two lists have any
items in common.
'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
L1 = [1,2,3,4]
L2 = [4,5,6,1]
common_flag = 0
common_flag = len([1 for item in L1 for item2 in L2 if item==item2])
if common_flag:
    print('The two lists have at {} common item(s)'.format(common_flag))
else:
    print('The two lists have no common items')

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that creates the list [1,11,111,1111,...,111...1], where the entries
have an ever increasing number of ones, with the last entry having 100 ones.
'''
from pprint import pprint
one_list = [int(''.join(['1']*i)) for i in range(1,21)]
pprint(one_list)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program to determine how many of the numbers between 1 and 10000 contain the
digit 3.
'''
n_contain_3 = 0

for i in range(1, 101):
    temp = list(str(i))
    if temp.count('3')>0:
        n_contain_3 += 1

print('There are {} numbers between 1 and 1001 contain digit 3'.format(n_contain_3))

print('')
print('')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
11. Write a program that finds all pairs of six-digit palindromic numbers that are less than 20
apart. One such pair is 199991 and 200002
'''
palindromic = []
for i in range(100000,1000000):
    str_i = str(i) 
    if str_i==str_i[::-1]:
        palindromic.append(i)

less_20 = [[palindromic[i], palindromic[i+1]] for i in range(0, len(palindromic)-1) \
           if palindromic[i+1]-palindromic[i] < 20 ]
print(less_20)
print('')
print('')

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
12. The number 1961 reads the same upside-down as right-side up. Print out all the numbers
between 1 and 100000 that read the same upside-down as right-side up
'''
digits = ['2','3','4','5','7']
n_repeat = 0
for num in range(100000):
    list_num = list(str(num))
    n_repeat = len([list_num.count(items) for items in digits ])
    if n_repeat==0:
        print('')
        
    

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
