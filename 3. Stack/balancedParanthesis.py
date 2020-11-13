# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 20:25:47 2020

@author: R GOMATHI
"""
import Stack

def balancedParenthesis(string):
    flag = 1
    index = 0
    myStack = Stack.Stack(len(string))
    while (index < len(string)) and (flag == 1):
        check = string[index]
        if check == '(':
            myStack.push(check)
        else:
            if myStack.isEmpty():
                flag = 0
            else:
                myStack.pop()
        index += 1

    if flag == 1 and myStack.isEmpty():
        return True
    else:
        return False

if __name__ == '__main__':
    print(balancedParenthesis('()(()()'))
    print(balancedParenthesis('((()))'))
