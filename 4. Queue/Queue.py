class Queue(object):
    
    def __init__(self,limit=20):
        self.queue = []
        self.limit = limit
        
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return  self.size()<= 0
        
    def enqueue(self,data):
        if self.size() >= self.limit:
            print("Queue is Full!")
        else:
            self.queue.append(data)
                        
    def dequeue(self):
        if self.size()==0:
            print("Queue is Empty!")
        else:
            self.queue.pop(0)        
        
    def peek(self):
        if(self.size!=0):
            return self.queue[0]
        else:
            return "Queue is empty"
        
# enqueue = O(n)
# Dequeue = O(n)