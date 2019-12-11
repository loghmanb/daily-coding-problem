'''
Min Stack
Asked in: Yahoo, Amazon, Adobe, Microsoft

https://www.interviewbit.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
getMin() – Retrieve the minimum element in the stack.
Note that all the operations have to be constant time operations.

Questions to ask the interviewer :

Q: What should getMin() do on empty stack? 
A: In this case, return -1.

Q: What should pop do on empty stack? 
A: In this case, nothing. 

Q: What should top() do on empty stack?
A: In this case, return -1
'''

class MinStack:
    def __init__(self):
        self.data = []
        self.min_data = []
        
    # @param x, an integer
    def push(self, x):
        self.data.append(x)
        if not self.min_data or \
                x<=self.min_data[-1]:
            self.min_data.append(x)

    # @return nothing
    def pop(self):
        if not self.data:
            return None
        if self.data[-1]==self.min_data[-1]:
            self.min_data.pop()
        return self.data.pop()

    # @return an integer
    def top(self):
        return self.data[-1] if self.data else -1

    # @return an integer
    def getMin(self):
        return self.min_data[-1] if self.min_data else -1