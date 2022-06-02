# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 10:43:14 2019

@author: Ali Saeedi
"""

import random as rnd

names = ['ali', 'reza', 'adib', 'mahdi', 'sajjad', 'peyman', 'ehsan', 'hossein']
print(names)
current_name = rnd.choice(names)
print('Current player is', current_name)
some_names = rnd.sample(names, 3)
print('Some names:', some_names)

print('')

print('names in original order:')
for item in names:
    print(item, end=' ', sep=' ')

print('\n\nshuffled names shuffled:')
rnd.shuffle(names)
for item in names:
    print(item, end=' ', sep=' ')
    
print('')

rnd.shuffle(names)
teams = []
for i in range(0,len(names),2):
    teams.append([names[i], names[i+1]])
print(teams)
print('')


# Split method returns a list of the words of a string
string = 'Hello! Welcome to the most beautiful city in the world.'
print(string.split())

print('A random word from the string:', rnd.choice(string.split()))  

'''
Optional argument: The split method takes an optional argument that allows it to break the
string at places other than spaces. Here is an example:
'''
phone_num = '0913-281-79-52'
split_num = phone_num.split(sep='-')
print(split_num)


# Join: works opposite of split. Joint operates on lists and its output is a string.
# However: split is a method of strings which has an out put of list
L = ['A', 'B', 'C']
print(''.join(L))
print(' '.join(L))
print(', '.join(L))
print('**'.join(L))

print('-'.join(split_num))


'''
List comprehensions
'''
zeros = [0 for i in range(10)]
ones = [1 for k in range(10)]
print(zeros)
print(ones)

string = 'Hello'
L = [1,14,5,9,12]
M = ['one', 'two', 'three', 'four', 'five', 'six']

print([10*i for i in ones])
print([j for j in range(1, 16, 2)])
print([k for k in L])
print([i*2 for i in L])
print([m**2 for m in L])

print([letter.upper() for letter in string])
print([letter.lower() for letter in string if letter==letter.upper()])
print([item for item in M if item[0]=='t'])


# Multiple fors You can use more than one for in a list comprehension
L = [[i, j] for i in range(2) for j in range(3)]
print(L)

L = [[i, j] for i in range(1, 4) for j in range(i)]
print(L)



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that generates a list L of 50 random numbers between 1 and 100
'''
from random import randint
rand_list = [randint(1, 100) for i in range(50)]
print(rand_list)

'''
Count how many items in a list L are greater than 50
'''
L = [54, 88, 43, 58, 95, 16, 78, 36, 84, 39, 43, 70, 91, 42, 99, 78, 23, 79, 61, 26, 26, 67]
greater50 = len([i for i in L if i>50])
print(greater50, 'items are greater than 50')
print('')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Given a list L that contains numbers between 1 and 100, create a new list whose first
element is how many ones are in L, whose second element is how many twos are in L, etc.
'''
r_list = [18, 18, 12, 5, 16, 7, 14, 15, 15, 13, 3, 11, 1, 20, 3, 18, 10, 4, 1,18, 11, 3, 16,
          7, 13, 1, 4, 1, 18, 5, 6, 16, 12, 19, 7, 20, 4, 9, 15, 8]  #[randint(1, 20) for i in range(50)]

r_list.sort()
print('main list:')
print(r_list)
print('')
print([i for i in range(1, 21)])
print('# repetition')
n_repeat = [ r_list.count(item) for item in range(1, 21) ]
print(n_repeat)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Create a string that contains a random assortment of 100 letters
'''
from random import choice
alphabet = 'abcdefghijklmnopqrstuvwxyz'
rand_str = ''.join([choice(alphabet) for k in range(100)])
print(rand_str)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Two-dimensional lists
L = [[1,2,3],
     [4,5,6],
     [7,8,9]]

for r in range(3):
  for c in range(3):
    print(L[r][c], end=' ')
  print()

# Pretty printing
from pprint import pprint
pprint(L)

print('')
L = [[(i+1)*(i+1)*(j+1) for i in range(5)] for j in range(5)]
pprint(L)

print('')

# Get a row
row = L[3]
print(row)

# Get a column
col = [L[i][2] for i in range(5)]
print(col)

# Flattening a 2D list
flat_list = [single_items for row in L for single_items in row]
print(flat_list)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that asks the user to enter some text and then counts how many articles are
in the text. Articles are the words 'a', 'an', and 'the'.
'''
from string import punctuation
text = 'In the context, a an and the are articles. A and an are unknown articles and the the is the specific article.' #'input('Insert a text: ')
for c in punctuation:
  text = text.replace(c, '')
   
text = text.lower()
split_text = text.split()
print(split_text)

articles = ['a', 'an', 'the']
num_articles = sum([split_text.count(item) for item in articles])
print('The number of articles are:', num_articles)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that allows the user to enter five numbers (read as strings). Create a string
that consists of the user’s numbers separated by plus signs. For instance, if the user enters 2,
5, 11, 33, and 55, then the string should be '2+5+11+33+55'.
'''
text = '2,33,26,99,101'
split_text = text.split(',')
plus_text = '+'.join(split_text)
print(plus_text)
print(eval(plus_text))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a simple lottery drawing program. The lottery drawing should consist of six different
numbers between 1 and 48.
'''
from random import sample
lott_pool = [i for i in range(1, 49)]
won_lott = sample(lott_pool, 6)
print(won_lott)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a censoring program. Allow the user to enter some text and your program should print
out the text with all the curse words starred out. The number of stars should match the length
of the curse word. For the purposes of this program, just use the“curse” words darn, dang,
freakin, heck, and shoot. Sample output is below:
  
Enter some text:
Oh shoot, I thought I had the dang problem
figured out. Darn it. Oh well, it was a heck of a freakin try.
Oh *****, I thought I had the **** problem figured out.
**** it. Oh well, it was a **** of a ****** try.
'''
text = '''
Oh shoot, I thought I had the dang problem figured out. Darn it. Oh well, it was a heck of a freakin try.
'''
cens_list = ['darn', 'dang', 'freakin', 'heck', 'shoot']

print('original text:')
print(text)

'''
for c in punctuation:
  text = text.replace(c, '')   
text = text.lower()
  '''

for word in cens_list:
  text = text.replace(word, '*'*len(word))

text
print('censored text:')
print(text)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Section 8.3 described how to use the shuffle method to create a random anagram of a string.
Use the choice method to create a random anagram of a string
'''
names = ['ali', 'reza', 'adib', 'mahdi', 'sajjad', 'peyman', 'ehsan', 'hossein']
print(names)
shuffled_names = []

for i in range(len(names)):
  choice_name = choice(names)
  shuffled_names.append(choice_name)  
  names.remove(choice_name) 

print(shuffled_names)  
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Let L be a list of strings. Write list comprehensions that create new lists from L for each of the
following.
(a) A list that consists of the strings of s with their first characters removed
(b) A list of the lengths of the strings of s
(c) A list that consists of only those strings of s that are at least three characters long
'''
string = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
f_rmv = [item[1:] for item in string]
l_items = [len(item) for item in string]
long_items = [item for item in string if len(item)>4]
print(f_rmv)
print(l_items)
print(long_items)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Let L=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]. Use a list comprehension to
produce a list of the gaps between consecutive entries in L. Then find the maximum gap size
and the percentage of gaps that have size 2.
'''
L=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
gaps = [abs(L[i]-L[i+1]) for i in range(len(L)-1)]
print(gaps)
max_gaps = max(gaps)
print('Max gaps is', max_gaps)
n_gap_2 = sum([1 for item in gaps if item==2])
perc_n_gap_2 = n_gap_2/len(gaps)
print(n_gap_2,' (out of ', len(gaps), ') gaps of two  which is ', round(100*perc_n_gap_2, 2), '%', sep='')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that finds the average of all of the entries in a 4 × 4 list of integers.
'''
from pprint import pprint
L = [[randint(1, 20) for i in range(4)] for j in range(4)]
print(L)

summed = 0
average = sum([ sum(L[i]) for i in range(4) ])/4
# average = sum(summed)
print('Average is', average)
print('')

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that checks to see if a 4 × 4 list is a magic square. In a magic square, every
row, column, and the two diagonals add up to the same value
'''

matrix = [[16,2,3,13],
          [5,11,10,8],
          [9,	7,	6,	12],
          [4,	14,	15,	1]]
print(matrix)
sum_rows = [sum(matrix[i]) for i in range(4)]
sum_cols = [ sum([matrix[i][c] for i in range(4)]) for c in range(4)]
sum_diag_1 = sum( [matrix[i][i] for i in range(4)]  )
sum_diag_2 = sum(  [ matrix[i][3-i] for i in range(4) ]  )
print('sum of rows:', sum_rows)
print('sum of coloumns:', sum_cols)
print('sum of diagonal 1:', sum_diag_1)
print('sum of diagonal 2:', sum_diag_2)

if (sum_diag_1 == sum_diag_2) and (sum_cols==sum_rows) and (sum_diag_1==sum_rows[0]):
    print('We have a magical matrix')
else:
    print('Matrix is not magical')

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
This exercise is useful in creating a Memory game. Randomly generate a 6 × 6 list of assorted
characters such that there are exactly two of each character. An example is shown below.

@ 5 # A A !
5 0 b @ $ z
$ N x ! N z
0 - + # b :
- : + c c x

'''
from random import shuffle

another way to do that

n = 6
memory_mat = [[0]*n for i in range(n)]  # a n-n matrix for memory game
# random characters (half of n^2)
rand_char = [chr(randint(33, 126)) for i in range((n**2)//2)]

# random order from 1 to n^2
rand_order = [i for i in range(n**2)]
shuffle(rand_order)

for j in range(n**2):
    correct_rwo = rand_order[j]//n
    correct_col = rand_order[j]%n
    memory_mat[correct_rwo][correct_col] = rand_char[j//2]

print(rand_char)
print(rand_order)   
pprint(memory_mat) 

'''
shorter way to do that
n = 6
memory_mat = [['']*n for i in range(n)]  # a n-n matrix for memory game
# random characters (half of n^2)
rand_char = [chr(randint(33, 126)) for i in range((n**2)//2)] *2
shuffle(rand_char)
memory_mat = [ [rand_char[(i*n)+(j%n)] for j in range(n)] for i in range(n) ]
pprint(memory_mat)
'''
    
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''

'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''




''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''

'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''




''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''

'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''




''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''

'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



