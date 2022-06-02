# -*- coding: utf-8 -*-
class Example:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b

# make an instance of the class
e = Example(8, 10)
# use a method of the class
print(e.add())


#%% Another example: a class with more methods
from string import punctuation

class Analyzer:
    def __init__(self, s):
        for c in punctuation:
            s = s.replace(c, '')
        s = s.lower()
        self.words = s.split()
        
    def number_of_words(self):
        return len(self.words)
    
    def starts_with(self, s):
        return len([w for w in self.words if w[:len(s)]==s ])
    
    def number_with_length(self, n):
        return len([w for w in self.words if len(w)==n ])
        
s = 'This is a test of the class.'
analyzer = Analyzer(s)
print(analyzer.words)
print('Number of words:', analyzer.number_of_words())
print('Number of words starting with "t":', analyzer.starts_with('t'))
print('Number of 2-letter words:', analyzer.number_with_length(2))        
        
        


    