# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:12:43 2022

@author: ga84nag
"""

n = int(input())
num = ''
transfer = 0
sign = (n<0)

if sign:
    n = -n
    
while n >= 3:
    res = transfer + n%3
    if res == 2:
        num = 'T' + num
        transfer = 1
    else:
        num = str(res) + num
        transfer = 0
    n //= 3

res = transfer + n

if res == 3:
    num = '10' + num
elif res == 2:
    num = '1T' + num
else:
    num = str(res) + num

if sign:
    num = num.replace('1', '2')
    num = num.replace('T', '1')
    num = num.replace('2', 'T')
  
    
print(num)
    