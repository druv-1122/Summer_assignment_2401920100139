class MyQueue(object):

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x):
        # Push element into input stack
        self.inStack.append(x)

    def pop(self):
        # Move elements only when outStack is empty
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())

        # Pop the front element
        return self.outStack.pop()

    def peek(self):
        # If outStack is empty, transfer elements
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())

        # Return front element
        return self.outStack[-1]

    def empty(self):
        # Check if queue is empty
        return len(self.inStack) == 0 and len(self.outStack) == 0
