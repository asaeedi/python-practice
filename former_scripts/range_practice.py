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

print('Fibonacci series less than 1000')
a, b = 0, 1

while b<1000:
    print(b, end = ', ')
    a, b = b, a+b
    
    

    