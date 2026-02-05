



# we need to create a working queue by using two stacks.
# by using two stacks we could do it by having one queue that represents the front and one for the back.
# when the front queue (the next elements that should be used) are empty, then the back of the queue should be added in reversed order to the front queue.

class MyQueue:

    def __init__(self):
        self.front = []
        self.back = []

    def push(self, x: int) -> None:
        self.back.append(x)
        

    def pop(self) -> int:
        if not self.front:
            self.front = self.back[::-1]
            self.back.clear()
        return self.front.pop()

    def peek(self) -> int:
        if not self.front:
            self.front = self.back[::-1]
            self.back.clear()
        return self.front[-1]
        

    def empty(self) -> bool:
        if self.front or self.back:
            return False
        return True
        