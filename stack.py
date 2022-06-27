class stack:
    def __init__(self,initialVal=[]):
        self.stack=initialVal
    def push(self,element):
        self.stack.append(element)
        return self.stack 
    def pop(self):
        if len(self.stack)==0:
            return "Stack is Empty"
        return self.stack.pop(-1)
    def peek(self):
        return self.stack[-1]
    def printStack(self):
        return self.stack
