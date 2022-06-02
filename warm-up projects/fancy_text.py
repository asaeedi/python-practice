# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 09:11:39 2022

@author: ga84nag
"""
'''
def text_processor(text, **kwargs):
    print('\n\n', text, '\n\n')
    for keys, values in kwargs.items:
        if values == 'bo':
            print(text + text)
'''            
   
    
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
    
    
def main():
    print("The output is:" + color.BLUE + 'Python 3!')    
    print("This is bold text looks like:",'\033[1m' + 'Python' + '\033[0m')
    #text_processor(input('Insert your text, followed by your desired processing: bo, it, fa, blfast, blslow\n'))
    
    
if __name__ == '__main__':    
    main()