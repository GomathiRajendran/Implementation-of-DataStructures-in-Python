class Stack(object):
    def __init__(self, limit = 20):
        self.stack = []
        self.limit = limit
    
    # for printing the stack contents
    def __str__(self):
        return ' '.join([str(i) for i in self.stack])
    
    # for pushing an element on to the stack
    def push(self, data):
        if len(self.stack) >= self.limit:
            print('Stack Overflow')
        else:
            self.stack.append(data)
            
    # for popping the uppermost element
    def pop(self):
        if len(self.stack) <= 0:
            print('Stack Underflow or stack is empty')
        else:
            return self.stack.pop()
            
    # for peeking the top-most element of the stack
    def peek(self):
        if len(self.stack) <= 0:
            print('Stack Underflow or stack is empty')
        else:
            return self.stack[-1]
        
    # to check if stack is empty
    def isEmpty(self):
        return len(self.stack) == 0
    
    # for checking the size of stack
    def size(self):
        return len(self.stack)
