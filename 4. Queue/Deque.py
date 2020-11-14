# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 23:04:06 2020

@author: R GOMATHI
"""

# Double ended Queues (Deque) supports both insertion and deletion at both the front and rear ends

class Deque(object):
    def __init__(self, limit = 10):
        self.queue = []
        self.limit = limit

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # check if queue is empty
    def isEmpty(self):
        return len(self.queue) <= 0

    # check if queue is full
    def isFull(self):
        return len(self.queue) >= self.limit

    # for inserting at rear
    def insertAtRear(self, data):
        if self.isFull():
            return
        else:
            self.queue.insert(0, data)

    # for inserting at front end
    def insertAtFront(self, data):
        if self.isFull():
            return
        else:
            self.queue.append(data)

    # deleting from rear end
    def deleteAtRear(self):
        if self.isEmpty():
            return
        else:
            return self.queue.pop(0)

    # deleting from front end
    def deleteAtFront(self):
        if self.isEmpty():
            return
        else:
            return self.queue.pop()

if __name__ == '__main__':
    myDeque = Deque()
    myDeque.insertAtFront(1)    # 1
    myDeque.insertAtRear(2)     # 2 1
    myDeque.insertAtFront(3)    # 2 1 3
    myDeque.insertAtRear(10)    #10 2 1 3
    print(myDeque)
    myDeque.deleteAtRear()      # 2 1 3
    print(myDeque)
    myDeque.deleteAtFront()     # 2 1
    print(myDeque)

    
    
#  Deque supports both stack and queue operations
