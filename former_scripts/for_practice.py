# -*- coding: utf-8 -*-

for i in range(5):
    print('This is line number', i+1)
    
for j in range(10, 0, -1):
    print('Counting down to ', j)
    
print('Even numbers less than 20')
   
for k in range(2, 20, 2):
    print(k, end=' ')    

print('')    
for m in range(6):
    print('*'*10)
    
for n in range(10):
    print('*'*(n+1))
    
for p in range(50):
    print((p+1), 'I love Taban jan :)')
    
for i in range(20):
    print((i+1), '---', (i+1)**2)
    
for j in range(100, 0, -2):
    print(j, end=' ')

print('')
print('')
h = 10
w = 40
for k in range(h):
    if k==0 or k==(h-1):
        print('*'*w)
    else:
        print('*', ' '*(w-2), '*', sep='')

print('')

h_tri = 10
for m in range(h_tri):
    print('*'*(1+m))

print('') 
    
for n in range(h_tri, 0, -1):
    print('*'*(n))

print('Diagonal shape with only one for loop!')
print('')
h_diam = 7

half_h = 1 + h_diam//2

for p in range(h_diam):
    print(' '*abs(half_h-p-1), '*'*(2*(half_h - abs(half_h-p-1))-1) , sep='')
    
#half-abs(x-half)    