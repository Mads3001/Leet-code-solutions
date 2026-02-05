
# the input is an array of integers that are side lengths of a triangle.
# the function must form a triangle with a non-zero area.
# the output should be the largest perimeter of a valid triangle that can be constructed with the side lengths.

def largestPerimeter(self, nums: list[int]) -> int:
    # we just sort the list

    if len(nums) < 3: # if less than 3 elements, then no triangle can be created.
        
        return 0
    nums.sort()
    
    for i in range(1, len(nums) - 1):
        if nums[-i] < nums[-(i + 1)] + nums[-(i + 2)]: # this goes out of index. it needs to stop at len(nums) - 1
            return nums[-i] + nums[-(i + 1)] + nums[-(i + 2)]

    return 0


input = [2,1,2]
print(largestPerimeter(0, input))

# it is maybe slower, when using subscribt instead of index.
# I'll try with index.

def largestPerimeter(self, nums: list[int]) -> int:
    # we just sort the list

    nums.sort(reverse=True) # this time we use index instead of subscribt.
    
    for i in range(len(nums) - 2):
        if nums[i] < nums[i + 1] + nums[i + 2]:
            return nums[i] + nums[i + 1] + nums[i + 2]

    return 0

# still slow. Maybe it can be done by writing a loop that takes the max values and iterates over them?

def largestPerimeter(self, nums: list[int]) -> int:

    large = max(nums)
    nums.remove(large)
    small1 = max(nums)
    nums.remove(small1)
    small2 = max(nums)
    nums.remove(small2)

    while large > small1 + small2: # if the triangle is invalid
        if nums: # checks, if there are any elements left
            large, small1 = small1, small2
            small2 = max(nums)
            nums.remove(small2) # this rotates and consumes the largest value and practically does the same thing as the other loop. This time it just searches and removes
            # instead of sorting everything.
        else: # if all elements have been consumed and its still an invalid triangle, then there is no answer.
            return 0
    return large + small1 + small2 # if the while loop terminates due to it being a valid triangle, then the perimeter is returned.

# this is very memory effecient, but still not fast



# ... This is very annoying. the fastest solution is fine, since it uses heapq and makes sense to be fast. Every other fast solution is just the same as my original solutions.
# the tools that evuluate are simply just flawed and have random variation.



# the heapq solution
import heapq

class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)

        while len(nums) >= 3:
            a = -heapq.heappop(nums)
            b = -heapq.heappop(nums)
            c = -nums[0]

            if b + c > a:
                return a + b + c
            
            heapq.heappush(nums, -b)
        
        return 0
    
