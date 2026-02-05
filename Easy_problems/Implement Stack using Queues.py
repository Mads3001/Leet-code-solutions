

# a queue can only pop from the first element, but we need to pop the last element.
# we can basically just do the same trick again. We just keep track of the front and back
# deques does not support slicing, so we need to make a copy each time we reverse.

from collections import deque

class MyStack:

    def __init__(self):
        self.topq = deque()
        self.bot = deque()

    def push(self, x: int) -> None: # it gets pushed to the bottom
        self.bot.appendleft(x)
        

    def pop(self) -> int:
        # the top is configured each time it needs to be read, since it always changes.
        self.bot.reverse()
        self.topq.extend(self.bot)  # the top is then the bottom reversed. To not lose data we extend it.
        self.bot.clear()
        return self.topq.pop()

    def top(self) -> int:
        
        self.bot.reverse()
        self.topq.extend(self.bot)  # the top is then the bottom reversed
        self.bot.clear()
        return self.topq[-1]
        

    def empty(self) -> bool:
        if self.topq or self.bot:
            return False
        return True
    




