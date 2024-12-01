# STACK
class Stack:
    def __init__(self, max_length):
        self.stack = [None] * max_length
        self.top = -1
        self.max_length = max_length

    def size(self):
        """Get Size of the stack"""
        return self.top + 1

    def is_empty(self):
        """Get if stack is empty"""
        return self.top == -1
    
    def is_full(self):
        """Get if stack is full"""
        return self.size() >= self.max_length

    def push(self, item):
        """To add an item at the top of a stack"""
        if self.is_full():
            raise OverflowError("Stack Overflow: Maximum size of stack is reached")
        
        self.top += 1
        self.stack[self.top] = item
        return None
    
    def pop(self):
        """To remove an item from the top of a stack"""
        if self.is_empty():
            raise IndexError("Cannnot remove from empty array")
        
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item
    
    def peek(self):
        """Return the top element without deleting it"""
        if self.is_empty():
            raise IndexError("Cannnot remove from empty array")
        
        return self.stack[self.top]
    
    def display(self):
        """Show the stack"""
        return self.stack[: self.top + 1]



