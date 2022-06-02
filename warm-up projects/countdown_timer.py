# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 08:29:58 2022

@author: ga84nag
"""

import time

#today = time.localtime()
#now = time.ctime(time.time())

def cdtime(T):
    while T:
        tmin, tsec = divmod(T, 60)
        timer = '{:02d}:{:02d}'.format(tmin, tsec)
        print(timer, end="\n")
        time.sleep(1)
        T -= 1
    print('Timer completed!')
        
    
def main():
    myTime = input('Enter seconds: ')
    cdtime(int(myTime))
    
if __name__ == '__main__':
    main()