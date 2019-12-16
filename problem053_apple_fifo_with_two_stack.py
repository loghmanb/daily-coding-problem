'''
This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.
'''

class FIFOQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def enqueue(self, val):
        self.in_stack.append(val)
    
    def dequeue(self):
        if not self.in_stack and \
                not self.out_stack:
            return None
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

if __name__ == "__main__":
    data = [
            [
                [['e', 5], ['e', 6], ['e', 7], ['d'], ['e', 8], ['d'], ['d'], ['d'], ['d'], ['e', 2], ['e', 4], ['d']]
            ]
        ]
    for d in data:
        print ('init queue for', d[0])
        q = FIFOQueue()
        for cmd in d[0]:
            if cmd[0]=='d':
                print('out', q.dequeue())
            else:
                print('in', cmd[1])
                q.enqueue(cmd[1])
