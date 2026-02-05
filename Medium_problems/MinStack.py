
# we need to create a first-in first-out data structure.
# all actions should be constant time complexity.
# For the getMin we need a new way to store the minimum value.
# we can do that with a tuple, by storing the current lowest value with each value in the stack.



class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            prev_min = float("inf")
        else:
            prev_min = self.stack[-1][1] # making this assigment local also flushes the value, so it will also be removed, if we pop an element.
        self.stack.append((val, min(val, prev_min)))

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
    




# using default min instead of tuples might make a difference.

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return min(self.stack)

# the min is definitely the slowest.

# what about implementing a whole second stack for just tracking the minimum value?
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
    
# this was faster and used less memory somehow. I guess tuples are not that space efficient.

