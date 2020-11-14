# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 23:12:44 2020

@author: R GOMATHI
"""
class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Queue(object):
    def __init__(self,limit):
        self.queue = [0]*limit
        self.rear = 0
        self.front = 0
        self.limit = limit
    
    def isEmpty(self):
        return len(self.queue == 0)
    
    def enqueue(self,data):
        if(self.rear == self.limit):
            print("Queue is full!")
        else:
            self.queue[self.rear] = data
            self.rear+=1
            
    def dequeue(self):
        if(self.front == self.rear == self.limit):
            print("Queue is empty")
        else:
            temp = self.queue[self.front]
            del self.queue[self.front]
            self.front+=1
            return temp
    
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    
    def size(self):
        return len(self.queue)

if __name__ == '__main__':
    
    myQueue = Queue(5)
    myQueue.enqueue(5)
    myQueue.enqueue(4)
    myQueue.enqueue(3)
    myQueue.enqueue(2)
    myQueue.enqueue(1)
    print("Elements in Queue: ",myQueue)
    print("Size of Queue: ",myQueue.size())
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.enqueue(1) 
    print("Elements in Queue: ",myQueue)
    print("Size of Queue: ",myQueue.size())
    
# enqueue : O(1)
# dequeue : O(1)