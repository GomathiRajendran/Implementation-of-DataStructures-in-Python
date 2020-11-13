# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 20:44:22 2020

@author: R GOMATHI
"""

import  Stack

def DeciToBin(decimal, base = 2):
    myStack = Stack.Stack(30)
    while decimal > 0:
        myStack.push(decimal % base)
        decimal //= base

    result = ''
    while not myStack.isEmpty():
        result += str(myStack.pop())

    return result

if __name__ == '__main__':
    print(DeciToBin(256))
