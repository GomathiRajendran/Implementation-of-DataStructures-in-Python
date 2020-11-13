# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 20:12:58 2020

@author: R GOMATHI
"""

import Stack

def reverse(string):
    mystack = Stack.Stack(len(string))
    rev = ''
    for i in string:
        mystack.push(i)
        
    while(not mystack.isEmpty()):
        rev+=mystack.pop()
        
    print("reversed String: ",''.join(rev))
    
if __name__ == '__main__':
    reverse('Monty Python')