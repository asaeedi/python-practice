# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 10:43:14 2019

@author: Ali Saeedi
"""

nums = [3, 5, 7, 9]
print('The first element of list1 is', nums[0])
print('Length of nums is', len(nums))

diff_lists = [-23, 7, 'name', [2, 4, 6, 7]]
print(diff_lists[3])

print(diff_lists.count(7))
print(diff_lists.index('name'))

a = [1, 2, 3]
b = [9, 8]

print(a+b)
print(b*4)

# Looping through a list
mylist = [2, 3, 5, 7, 11, 13, 17, 19]
for i in range(len(mylist)):
    print(mylist[i])

print('')    

for item in mylist:
    print(item)
    
# Biult-in functions working on lists
ages = [23, 31, 20, 18, 22, 25, 29, 32, 35]
print('Max ages is:', max(ages))
print('Min ages is:', min(ages))
print('Average of ages is:', round(sum(ages)/len(ages), 2))


# List methods
# append
x = ['a', 'z', 'b', 'y']
x.append([24, 3])       # treats input as a single item
print(x)

# sort
num = [23, 11, 19, 0, -2, 10, -43, 10]
print('original:', num)
num.sort()
print('sorted:', num)
# reverse
num.reverse()
print('reversed:', num)

# remove (first occurance)
num.remove(10)
print('removed:', num)

# pop(p): remove item at position p and returns it
poped = num.pop(2)
print('poped item:', poped)
print('poped:', num)

# insert(p, x)
num.insert(2, 11)
print('inserted:', num)

print('')

L = [2, 4, 15, 8, 10, 12]
print(L)
L[2] = 6
print(L)
L.insert(0, 0)
print(L)
L.insert(7, 14)
print(L)

del L[3]
print(L)

del L[:4]
print(L)


'''
Write a program that generates a list L of 50 random numbers between 1 and 100.
'''
from random import randint
rand_list = [0]*50
for k in range(len(rand_list)):
    rand_list[k] = randint(1, 101)

print(rand_list)  
  
'''
# another alternative
L = []
for i in range(50):
    L.append(randint(1,100))    
print(L)

# a third alternative
L = []
for i in range(50):
    L = L + [randint(1,100)]    
print(L)
'''


'''
Count how many items in a list L are greater than 50.
'''
count_g50 = 0
for item in L:
    if item>50:
        count_g50 += 1
print('There are {} random numbers in L greater than 50'.format(count_g50))


'''
Replace each element in a list L with its square.
'''
for item in L:
    L[L.index(item)] = item**2
print(L)

'''
Write a program that prints out the two largest and two smallest elements of a list
called scores
'''
scores = []
for i in range(20):
    scores.append(randint(1, 50))

length_scores = len(scores)
print(scores)
scores.sort()
print(scores)
print('The two smallest values in scores are {} and {}'.format(scores[0], scores[1]))    
print('The two largest values in scores are {} and {}'.format(scores[-2], scores[-1]))    

print('')


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the
entries in the list that are greater than 10 with 10
'''
user_list = [0]*20
for i in range(20):
    user_list[i] = randint(1, 12)
print(user_list)    
for j in range(20):
    if user_list[j]>10:
        user_list[j]=10
        
print(user_list)
print('')        
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the
entries in the list that are greater than 10 with 10
'''

str_list = ['Farvardin', 'Ordibehesht', 'Khordad', 'Tir', 'Mordad', 'Shahrivar']
new_str_list = []

for i in range(len(str_list)):
    new_str_list.append(str_list[i][1:])
    
print(new_str_list)    


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that takes any two lists L and M of the same size and adds their elements
together to form a new list N whose elements are sums of the corresponding elements in L
and M. For instance, if L=[3,1,4] and M=[1,5,9], then N should equal [4,6,13].
'''
L = [3, 1, 4]
M = [1, 5, 9]
sum_lists = L + M
print(sum_lists)    # doesn't do the arithmetic, but appends the two lists
sum_lists = []

for i in range(len(M)):
    sum_lists.append(L[i]+M[i])

print(sum_lists)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that asks the user for an integer and creates a list that consists of the factors
of that integer.
'''
from math import sqrt, floor
num = 12321
factors = []
sq_num = floor(sqrt(num))
if sq_num == sqrt(num):
    perfect_flag = 1
else:
    perfect_flag = 0
    
for k in range(1, sq_num + 1):
    if num%k == 0:
        factors.append(k)
        factors.append(num//k)

# if perfect, remove one redundant sqrt(num)
if perfect_flag:
    factors.remove(sq_num)
factors.sort()    
print('factors of {} are: {}'.format(num, factors))
print(num, 'is prime!') if len(factors)==2 else print(num, 'is not prime!')

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that rotates the elements of a list so that the element at the first index moves
to the second index, the element in the second index moves to the third index, etc., and the
element in the last index moves to the first index.
'''
num_list = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(num_list)
num_list.append(num_list[0])
for i in range(len(num_list)-1):
    num_list[i] = num_list[i+1]
del num_list[-1]
print(num_list)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that removes any repeated items from a list so that each item appears at most
once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].
'''

r_list = [7,1,1,2,3,4,3,0,1,0,1,1,2,0,0,3,3,7,7]
print(r_list)
for item in r_list:
    n_count = r_list.count(item)
    if n_count>1:
        while(n_count>1):
            r_list.reverse()    # to keep the orders of appearance
            r_list.remove(item)
            n_count -= 1
            r_list.reverse()    # put them back to their original orders
            
print(r_list)            


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
