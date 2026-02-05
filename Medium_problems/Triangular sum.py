
# you get an array where you need to calculate the triangular sum and return it with the sum(triang) % 10


# 15 (+15) # the value doubles, but goes down by the first and last element
# 24 (+9) (-6)
# 36 (+12) (-12)
# 36- + 12 = 48 (+12) (-34)
# 48 (+0) (-48)
# the first and last elements are the only ones that are not added twice to the next step.
# every element inbetween are added twice to the next level.
# we can maybe take advantage of that.
# the amount it loses out on also starts growing. we then need a method to track the values of the outermost values in the triangle.
# it starts out by being 
# nums[i] + nums[-(i + 1)] # nums[0] + nums[-1] (6)
# in the second row it is: nums[0] + nums[1] + nums[-1] + nums[-2] (12)
# third row is: (nums[0] + nums[1]) + nums[1] + nums[-2]


# we can make a loop that takes the sum of the array and overwrite values at the first and last element over time, as the array should become smaller.
# it all gets stored in a variable and gets mod 10'd at the last step.

"""
def triangularSum(self, nums: list[int]) -> int:
    # the loop should persist until all the elements with a value greater than zero is either 2 or 1.
    triangle_sum = sum(nums)
    length = len(nums)
    i = 0
    while length > 2: # we must just overwrite values instead of removing, since removing the first element is not very effecient.
        triangle_sum += triangle_sum
        print(triangle_sum)
        # nums[i] = 0
        # nums[-(i + 1)] = 0
        length -= 1
    
    return triangle_sum % 10

# the current iteration ends up being very annoying, when there begins to be many more levels to the triangle
"""


def triangularSum(self, nums: list[int]) -> int:
    # lets just try solving it the old brute force way.
    # we'll use a temporary array to store the next step in
    return_array = nums
    next_step = []
    while 1 < len(return_array):
        for i in range(len(return_array) - 1):
            next_step.append(return_array[i] + return_array[i + 1])
        return_array = next_step[::-1]
        next_step.clear()
    return return_array[0] % 10

# it is slow and memory intensive, but it works. I needed to use some math theory and linear algebra, if the optimal approach would be used.





# one of the best ones according to time is:

class Solution:
    def triangularSum(self, nums: list[int]) -> int:

        n = len(nums)
        newNums = nums
        while n>1:
            
            newNums = [(newNums[i] + newNums[i+1]) % 10 for i in range(n-1) ] 
            # it practically does the same thing, but just overwrite itself instead of making a second array.
            # maybe i don't need to store the array.
            n-=1
        return newNums[0]
    # this is actually slower, since it tries a modulo calculation for each cell instead of doing it at the last value.
    # i just tried submitting and it wasn't even faster. It somehow used less memory. This doesn't make sense. This has O(N) space complexity
    # my solution had O(1) space complexity
    # must be the shallow copy.
    


def triangularSum(self, nums: list[int]) -> int:
    return_array = nums # this also just overwrites itself and removes an element for each iteration.

    while 1 < len(return_array):
        for i in range((len(return_array) - 1)): # len is 5. i goes from 0 -> 3
            return_array[i] = return_array[i] + return_array[i + 1]
            # we just remove the last cell for each iteration.
        return_array.pop()
    return return_array[0] % 10

# this version should use less memory and maybe be a smidge faster.
# it can maybe also just be done inplace?




def triangularSum(self, nums: list[int]) -> int:
    # this is done inplace.
    n = len(nums) # instead of using .pop we can just make the array artificially shorter
    while 1 < n:
        
        for i in range((n - 1)): # len is 5. i goes from 0 -> 3
            nums[i] = nums[i] + nums[i + 1]
            # we just remove the last cell for each iteration.
        n -= 1
    return nums[0] % 10

# it is apparently slower, when done inplace. What if a just remove the .pop and just makes it artificially shorter?
# I can't make it use less memory. This version is faster though, because we removed the .pop.


input = [1,2,3,4,5]

print(triangularSum(0,input))



# this is apperently the real fast solution that uses the chinese remainder theory

class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        n=len(nums)-1
        ans, A=nums[0], 1
        for k in range(1, n+1): # the whole triangle can be solved in one pass, since some math theory can be used to calculate how many times
            # the number is applied to the next value before disappearing. The outer values only contribute once. That was what i tried to do in my initial solution
            # but it became too much. This code figures out how close the values are to the center and multiplies the number a certain amount of times and adds it to the bottom
            # this goes over the problem in one singular pass.
            # very smart solution that i tried to do, but failed, due to not knowing a loop structure that could do it.
            A=A*(n-k+1)//k
            ans=(ans+nums[k]*A)%10
        return ans