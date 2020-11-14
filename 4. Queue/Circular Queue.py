# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 00:56:22 2020

@author: R GOMATHI
"""

class CircularQueue(object):
    def __init__(self, limit = 10):
        self.limit = limit
        self.queue = [None for i in range(limit)]  
        self.front = self.rear = -1

    # for printing the queue
    def __str__(self):
        if (self.rear >= self.front):
            return ' '.join([str(self.queue[i]) for i in range(self.front, self.rear + 1)])
  
        else: 
            q1 = ' '.join([str(self.queue[i]) for i in range(self.front, self.limit)])
            q2 = ' '.join([str(self.queue[i]) for i in range(0, self.rear + 1)])
            return q1 + ' ' + q2

    # for checking if queue is empty
    def isEmpty(self):
        return self.front == -1

    # for checking if the queue is full
    def isFull(self):
        return (self.rear + 1) % self.limit == self.front

    # for adding an element to the queue
    def enqueue(self, data):
        if self.isFull():
            print('Queue is Full!')
        elif self.isEmpty():
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.limit  
            self.queue[self.rear] = data 

    # for removing an element from the queue
    def dequeue(self):
        if self.isEmpty():
            print('Queue is Empty!')
        elif (self.front == self.rear):  
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.limit 

if __name__ == '__main__':
    
    myCQueue = CircularQueue(5)
    myCQueue.enqueue(5)
    myCQueue.enqueue(4)
    myCQueue.enqueue(3)
    myCQueue.enqueue(2)
    myCQueue.enqueue(1)
    print("Elements in Queue: ",myCQueue)
    myCQueue.dequeue()
    myCQueue.dequeue()
    myCQueue.enqueue(1)
    myCQueue.enqueue(6)
    print("Elements in Queue: ",myCQueue)