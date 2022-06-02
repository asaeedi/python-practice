# -*- coding: utf-8 -*-

import math

num = 19

flag = 0

sq_num = math.floor(math.sqrt(num))
for i in range(2, sq_num+1):
    if num%i==0:
        flag = 1
        
if flag==1:
    print('{} is not a prime number'.format(num))
else:
    print('{} is a prime number'.format(num))        
