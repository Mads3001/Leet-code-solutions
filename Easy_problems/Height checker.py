
# an array of integers is input. The array should be sorted in ascending order.
# the code should check how many numbers are at the right position.


from copy import deepcopy
def heightChecker(self, heights: list[int]) -> int:
    
    expected = deepcopy(heights)
    expected.sort()
    wrong_spot = 0
    for _ in range(len(heights)):
        if heights[_] != expected[_]:
            wrong_spot += 1
    
    return wrong_spot

heights = [1,2,3,5,4]

print(heightChecker(0, heights))

# that solution is not fast. sorting is usually what makes it slower.
# a faster solution practically also just makes a deepcopy, but uses index instead of enumerate when comparing. Maybe that's faster.


def heightChecker(self, heights: list[int]) -> int:
    
    expected = deepcopy(heights)
    expected.sort()
    wrong_spot = 0
    for index, height in enumerate(heights):
        if height != expected[index]:
            wrong_spot += 1
    
    return wrong_spot

# this was my original solution. There's a difference of 150 megabytes of memory (my solution used less), but the other solution was 4 ms faster.
