
# a circular queue is good for the first in first out structure without using too many ressources.


class MyCircularQueue:

    def __init__(self, k: int): # create the queue
        self.queue = [-1 for _ in range(k)] # standard value is -1 and is not a valid value.
        self.space = k
        self.head = 0 # the head will always start at the first cell. This makes it so, it is initialized before the first enque, so it will be properly assigned.
        self.tail = -1 
        self.length = k

    def enQueue(self, value: int) -> bool: # add a value to the queue
        if self.space == 0:
            return False
        self.tail = (self.tail + 1) % self.length # it is circular so the tail will rotate.
        self.queue[self.tail] = value # the value is stored.
        self.space -= 1 # space is reduced by 1.
        return True

    def deQueue(self) -> bool: # remove a value from the queue
        if self.space == self.length: # if it is empty. every cell is empty.
            return False
        self.head = (self.head + 1) % self.length # the head is moved and the value is set to now be able to be overwritten
        self.space += 1 # one space is restored.
        return True

    def Front(self) -> int: # return the head value
        if self.space == self.length:
            return -1
        return self.queue[self.head]


    def Rear(self) -> int: # return the tail value.
        if self.space == self.length:
            return -1
        return self.queue[self.tail]


    def isEmpty(self) -> bool:
        return self.space == self.length
        

    def isFull(self) -> bool:
        return self.space == 0
    

# this version works and is very efficient compared to otherts in terms of memory (beats 93,78 %). only around 59,62 % in speed though.
# a second time it beat 100 % in runtime. It is probably leetcode being weird again, but the solution worked flawlessly.