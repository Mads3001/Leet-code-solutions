

# the input is a list of integers.
# the output needs to be the squared values of them in an ascending order.


def sortedSquares(self, nums: list[int]) -> list[int]:

    for index, number in enumerate(nums): # the index is tracked
        nums[index] = number ** 2 # the number from the list is set to its square. This can be done due to the index being tracked.
    nums.sort()
    return nums


numbers = [-4,-1,0,3,10]
numbers = [-7,-3,2,3,11]
print(sortedSquares(0, numbers))

# a faster method would be to write a for loop in the return.

def sortedSquares(self, nums: list[int]) -> list[int]:

    return sorted([x * x for x in nums]) # this doesn't need to store anything, but creates a new list (I think). 
# a very fast solution, since it doesn't assign new values. It might also just be faster, since it doesn't use exponents.
# the normal multiplication algorithm is maybe faster than the exponent one.
