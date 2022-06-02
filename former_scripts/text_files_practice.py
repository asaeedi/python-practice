# -*- coding: utf-8 -*-

lines = [line.strip() for line in open('example.txt')]
print(lines)

# Second way to read a text file:
s = open('example.txt').read()
print(s)

#%% Writing to a text file
f = open('writefile.txt', 'w')
print("This is line number 7", file=f)
print("This is line number 8", file=f)
f.close()

#%% Read numbers from a text file, do something on them and then write them in a new text file
f1 = open('ftemps.txt', 'w')
temperatures = [line.strip() for line in open('temps.txt')]
for t in temperatures:
  print(int(t)*9/5+32, file=f1)
  
f1.close()

#%% Read basketball data from text file, calculate the ratio of win/all_games for all teams
lines = [line.strip() for line in open('basketball.txt')]
for team in lines:
  split_team = team.split(sep=',');
  win = int(split_team[2])
  loose = int(split_team[3])
  wl_ratio = (win/(win+loose))
  print('{:20s}'.format(split_team[1]), end = ' ', sep='')
  print('{:.3f}'.format(wl_ratio))

print('')  

# find teams with win-loose ratio between 0.5 and 0.8
for team in lines:
  split_team = team.split(sep=',');
  win = int(split_team[2])
  loose = int(split_team[3])
  wl_ratio = (win/(win+loose))
  if 0.5 <= wl_ratio <= 0.8:
    print(team)

#%% Play around with 10000 long most-used 
from pprint import pprint
wordlist = [line.strip() for line in open('google_words.txt')]

# print words with more than 15 letters
for word in wordlist:
  if len(word) >= 15:
    print(word)
    
print('')

# another way to do that
pprint([word for word in wordlist if len(word) >= 15])    
print('')

# Print all the words that start with qu or th.
for word in wordlist:
  if word[:2]=='qu' or word[:2]=='th':
    print(word)
print('')

# Determine what percentage of words start with a vowel
count = 0
for word in wordlist:
  if word[0] in 'aeiou':
    count += 1
print('{:.2f}% of the words start with vowels'.format(100*count/len(wordlist)))    


# Print all 7-letter words that start with th and end in ly. Things like this are good for
# cheating at crosswords
for word in wordlist:
  if word[:2]=='th' and word[-2:]=='ng':
    print(word)
print('') 

# Print the first ten words that start with q.
i = 0;
for word in wordlist:
  if word[0]=='q' and i<10:
    i += 1
    print(word)

print()
    
#%% Find the longest word that has all the letters a, b, c, d, and e.
long_words = []
max_len = 0
for word in wordlist:    
  if 'a' in word and 'b' in word and 'c' in word and 'd' in word and 'e' in word:
      print(word)
      if len(word)>max_len:
          long_word = word
          max_len = len(word) 
print()          
print(long_word)
print(max_len)      
print()

#%%     
'''Excersize 10.
Wordplay – Use the file wordlist.txt for this problem. Find the following:
'''

# (a) All words ending in ime
for word in wordlist:
  if word[-4:]=='ying':
    print(word)
    
print('')


#%% (b) All words whose second, third, and fourth letters are ave
for word in wordlist:
  if word[1:4]=='sta':
    print(word)
    
print('')

#%% How many words contain at least one of the letters r, s, t, l, n, e
count = 0
for word in wordlist:
    for letter in 'rstlne':
        if letter in word:
            count += 1
            break    
print('{} (out of {}) words contain at least one of the letters r, s, t, l, n, e'.format(count, len(wordlist)))
print('')

#%% All words with no vowels
count = 0
for word in wordlist:
    for letter in 'aeiou':
        if letter in word:
            count += 1
            break    
print('{} (out of {}) words has no vowels'.format(len(wordlist) - count, len(wordlist)))
print('')

#%% All words that contain every vowel

for word in wordlist:
    count = 0
    for letter in 'aeiou':
        if letter in word:
            count += 1
    if count == len('aeiou'):
        print(word)

print('')


#%% (g) Whether there are more t12-letter words or 14-letter words
count_12 = 0
count_14 = 0
for word in wordlist:
    if len(word)==12:
        count_12 += 1
    if len(word)==14:
        count_14 += 1
if count_12 > count_14:
    print('The number of 12-letter words ({}) is greater that of 14-letter words ({})'.format(count_12, count_14))
else:
    print('The number of 14-letter words ({}) is greater that of 12-letter words ({})'.format(count_14, count_12))
    
print('')

#%% (h) The longest word in the list
