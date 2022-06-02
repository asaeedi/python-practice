# -*- coding: utf-8 -*-

import math

st1 = 'Hello'
st2 = "World"
print(st1, st2)

# get input from user
input_text = 'Hi there' #input('Insert some text: ')
print('Text entered by the user: ', input_text)
print('Length of string is', len(input_text))

# get input number from user
input_num = 1397 #eval(input('Enter a number: '))
print('The number user entered is', input_num)

# concatenation by + and *
s1 = 'AB'
s2 = 'ab'
s3 = s1+s2
s4= s1*4 + s2*5
print(s3)
print(s4)

# the 'in' operator
string = 'people'
srch_st = 'oep'

if srch_st in string:
    print('The string "{}" has the sequence "{}"'.format(string, srch_st))
else:
    print('The string "{}" does not contain the sequence "{}"'.format(string, srch_st))
 
# string indexing
string = 'rythm'
print(string[0])
print(string[1])
print(string[-1])
print(string[-2])


sequence = 'abcdefghij'
for i in range(len(sequence)):
    print(i, sep = ' ', end = ' ')

print('')
    
for i in range(len(sequence)):
    print(sequence[i], sep = ' ', end = ' ')
    
print('')
print('')
print(sequence[:5])
print(sequence[7:])
print(sequence[-2:])
print(sequence[: -3])
print(sequence[:])
print(sequence[0:9:2])
print(sequence[: : -1])
    

# strings are immutable, i.e. it is not possible to modify their elements
s = 'Ballon'
# s[0] = 'T' # not possible
s = s[:2]+'LL'+s[4:]
print(s)

print('')
print('')

# String methods: .lower and .upper
st = 'shahrekord'
print(st)
upper_st = st.upper()
print(upper_st)
lower_st = upper_st.lower()
print(lower_st)


# String methods: .replace
st = 'UVWXYZ'
print(st)
st_replaced = st.replace('VWXY', 'ab')
print(st_replaced)


 # String methods: .count
string = 'Tick'*9
count_str = 'ickT'

print(string)
n_count = string.count(count_str)
print('There are {} repetitions of {} in {}'.format(n_count, count_str, string))
  

# String methods: .index
text = 'Spontaneous'
search_text = 'n'
first_occur = text.index(search_text)
print('The first occurance of {} in {} is at index number {}'.format(search_text, text, first_occur))

# String methods: isalpha
text = 'Tehran'
isletter = text.isalpha()
if isletter:
    print('{} has only letters in it!'.format(text))
else:
    print('{} has letters and digits!'.format(text))

print('')
print('')

# String methods: isdigit
text = '1399T'
isdigit = text.isdigit()
if isdigit:
    print('{} has only digits in it!'.format(text))
else:
    print('{} has digits and letters!'.format(text))


# String methods: isdecimal
text = '10'
isdecimal = text.isdecimal()
if isdecimal:
    print('{} is a decimal number!'.format(text))
else:
    print('{} is not a decimal number!'.format(text))
    
print('')
print('')

# The escape charachter
print('Hi there\n\nHe said \"I can\'t do it!\"') 

print('')
print('')

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that asks the user for a string and prints out the location of each 'a'
in the string.
'''
text = 'Eat an apple a day and keep the doctor away!'
for i in range(len(text)):
    if text[i] == 'a':
        index = i
        print(index)

print('')        
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that asks the user for a string and creates a new string that doubles
each character of the original string. For instance, if the user enters Hello, the output should be
HHeelllloo.
'''
string = 'Message4'
double_str = ''

for c in string:
    double_str += c*2

print(string)
print(double_str)    

print('')       
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''        


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that asks a user for their name and prints it in the following funny
pattern:
'''
input_str = 'Alireza'
for i in range(len(input_str)):
    print(input_str[:i+1], end=' ')

print('')
print('')        
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''        


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that removes all capitalization and common punctuation from a
string s.
'''
string = 'Today, some people (and not all of them) say: "We don\'t care about society!"'
print(string)
string = string.lower()
for c in ',.;:-?!()\'"':
    string = string.replace(c, '')
    
print(string)    
print('')
print('')    
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''        


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
People often forget closing parentheses when entering formulas. Write a program that asks
the user to enter a formula and prints out whether the formula has the same number of opening and closing parentheses.
'''
formula = 'sin(2*pi + log(a/(20)))' #input('Enter your formula: ')
open_prant = formula.count('(')
close_prant = formula.count(')')
if open_prant==close_prant:
    print('The formula has the same number of \'(\' and \')\' ')
else:
    print('The number of \'(\' and \')\' are not equal!')
    
        
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''        


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that asks the user to enter a word and then capitalizes every other letter of
that word. So if the user enters rhinoceros, the program should print rHiNoCeRoS.
'''
string = 'corresponding'
print(string)
for i in range(len(string)):
    if i%2==0:
        print(string[i].upper(), end='', sep='')
    else:
        print(string[i], end='', sep='')
 
print('')       
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''        


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that asks the user to enter a word and determines whether the word is a
palindrome or not. A palindrome is a word that reads the same backwards as forwards.
'''
word = 'mama'
flag = 1
L = len(word)
i = 0
mid_point = L//2
while (i< 1 + mid_point):
    if word[i] != word[L-1-i]:
        flag = 0
        break
    else:
        i += 1

if flag:
    print(word, 'is palindrome!')   
else:
    print(word, 'is not palindrome!')

print('')               
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Ask the user for a number and then print the following, where the pattern ends at the number
that the user enters.
1
 2
  3
   4
'''
num = 5 #eval(input('Enter a number: '))
for j in range(num):
    print(' '*j, (j+1), sep='')

print('')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that asks the user to enter a string, then prints out each letter of the string
doubled and on a separate line. For instance, if the user entered HEY, the output would be
HH
EE
YY
'''
text = 'ALIREZA'
for c in text:
    print(c*2)

print('')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that asks the user to enter their name in lowercase and then capitalizes the
first letter of each word of their name.
'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
text = 'ali saeedi aboueshaghi irani'
print(text)
print(text[0].upper(), end='')
for k in range(1, len(text)):
    if text[k-1]==' ':
        print(text[k].upper(), end='')
    else:
        print(text[k], end='') 

print('')


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that generates the 26-line block of letters partially shown below. Use a loop
containing one or two print statements.
    abcdefghijklmnopqrstuvwxyz
    bcdefghijklmnopqrstuvwxyza
    cdefghijklmnopqrstuvwxyzab
    ...
    yzabcdefghijklmnopqrstuvwx
    zabcdefghijklmnopqrstuvwxy
'''
alphabet = 'abcd'
for i in range(len(alphabet)):
    print(alphabet[i :], end='')
    print(alphabet[:i])

# how about one print statement???
print('')

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Write a program that asks the user for a large integer and inserts commas into it according
to the standard American convention for commas in large numbers. For instance, if the user
enters 1000000, the output should be 1,000,000
'''
large_num = '1234'
L = len(large_num)
n_commas = math.ceil(L/3) - 1
rem3 = L%3
if rem3==0:
    rem3=3

for i in range(L):
    if i==rem3-1 and i!=L-1:
        print(large_num[i], ',', sep='', end='')
        rem3 += 3
    else:
        print(large_num[i], sep='', end='')        
    
    
print('')

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
In calculus, the derivative of x4 is 4x3. The derivative of x5 is 5x4. The derivative of x6 is
6x5. This pattern continues. Write a program that asks the user for input like x^3 or x^25
and prints the derivative. For example, if the user enters x^3, the program should print out
3x^2
'''
formula = 'x^12' #input('insert formula in form of x^n: ')
power = eval(formula[2:])
print(power, 'x^', power-1, sep='')



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''