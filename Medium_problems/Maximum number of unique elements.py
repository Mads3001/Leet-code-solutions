
# we get an array of numbers.
# we can add or subtract within the range of k to edit the numbers one at a time.
# the plan is to get as many unique elements as possible.

def maxDistinctElements(self, nums: list[int], k: int) -> int:

    # we can start out by sorting the array
    nums.sort()

    # then we just need to make every element as low as they can go without overlapping. It should start from the bottom up.

    nums[0] -= k
    i = 1 # we manually adjust the first element

    while i < len(nums):

        n = -k
        while n < k:
            if nums[i] + n < nums[i - 1] + 1: # this loop can be long, if k is big and there are a bunch of completely identical numbers in the array. It does work though.
                n += 1
            else:
                nums[i] += n
                break
    # the loop should make the element nums[i] become as small as possible without overlapping with another element.
    # it will then contribute to gaining insight into the value the next element must be bigger than.
    # at last we can check for duplicates by converting to a set and count the elements.

    return len(set(nums))

# the code misses 1 or 2 values sometimes.

# maybe rewriting the second loop can help


def maxDistinctElements(self, nums: list[int], k: int) -> int:
    nums.sort()
    nums[0] -= k
    i = 1 

    while i < len(nums):
        n = -k
        nums[i] -= k # it starts out at the minimum value.
        while n != k: # k is 2. n can range from -2 to 2 in this scenario. It runs once, when n == k and stops when nums[i] is the max amount. This works.
            # the loop stops, when nums[i] is the largest it can be. It breaks, when it is large enough at a smaller value.
            if nums[i] <= nums[i - 1]: # this is true until nums[i] is bigger because it will be increased by 1 after that.
                nums[i] += 1 # it will be increased, if it is still too small.
                n += 1
            else:
                break # when it is bigger, then the loop should break.
        i += 1
    return len(set(nums))



inp = [1,2,2,3,3,4]

#kinp = 2
#print(maxDistinctElements(0,inp,kinp))


# the loop runs out of time. We should also just have a check, if k can even make it a valid value. That way it only needs one check instead of a giant loop when
# hit with many identical elements.

def maxDistinctElements(self, nums: list[int], k: int) -> int:
    nums.sort()
    nums[0] -= k
    i = 1 

    while i < len(nums):
        n = -k
        
        nums[i] -= k 
        while n < k: 
            if nums[i] + 2*k == nums[i - 1]: # this should safeguard many repeating identical elements.
                nums[i] += 2*k
                break

            if nums[i] <= nums[i - 1]: 
                nums[i] += 1 
                n += 1
            else:
                break 
        i += 1
    return len(set(nums))

# maybe it would just be smarter to assign n better and going from there.




def maxDistinctElements(self, nums: list[int], k: int) -> int:
    nums.sort()
    nums[0] -= k
    i = 1 

    while i < len(nums):
        n = min(max(nums[i - 1] - nums[i], -k), k) # The difference should start out by being checked.
        # nums[i] - nums[i - 1] gives the difference to start with. it can be a maximum of k. The max min should reassign n so it is doesn't make a bunch of redundant looping.
        nums[i] += n
        while n < k:
            if nums[i] <= nums[i - 1]: 
                nums[i] += 1 
                n += 1
            else:
                break 
        i += 1
    return len(set(nums))

#inp = [1,1,1,1,1,1,1,1,5,5,5]
#kinp = 3

#print(maxDistinctElements(0,inp,kinp))


def maxDistinctElements(self, nums: list[int], k: int) -> int:
    nums.sort()
    nums[0] -= k
    i = 1 
    while i < len(nums):
        n = min(max(nums[i - 1] - nums[i], -k), k) # The difference should start out by being checked.

        # nums[i] - nums[i - 1] gives the difference to start with. it can be a maximum of k. 
        # The max min should reassign n so it is doesn't make a bunch of redundant looping.
        nums[i] += n # now it doesn't even need looping. This is now an O(N) solution instead of O(N^2)
        if n < k and nums[i] == nums[i - 1]:
            nums[i] += 1 
        i += 1
    return len(set(nums))

# inp = [1,1,1,1,1,1,1,1,5,5,5]
# kinp = 3
inp = [10,10,10,5,10]
kinp = 1

print(maxDistinctElements(0,inp,kinp))

# it could be faster, if it didn't write to the array, but just kept it in mind.



def maxDistinctElements(self, nums: list[int], k: int) -> int:

    if not nums:
        return 0 # if there are no numbers

    nums.sort()
    nums[0] -= k
    i = 1 
    last = nums[0]
    current = 0
    count = 1 # this keeps count of the unique.

    while i < len(nums):
        n = min(max(last - nums[i], -k), k) # The difference should start out by being checked.

        # nums[i] - nums[i - 1] gives the difference to start with. it can be a maximum of k. 
        current = nums[i] + n
        if n < k and current == last:
            current += 1
        if current > last:
            count += 1

        last = current
        i += 1
    return count


# the solution is O(N*log(N)). It is the optimal time complexity for this problem, but it is still very slow.


# this is faster somehow.
class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        if not nums:
            return 0
        nums.sort()
        count = 0
        prev = -(1 << 30)
        for a in nums:
            low = a - k
            high = a + k
            x = prev + 1
            if x < low:
                x = low
            if x <= high:
                count += 1
                prev = x
        return count
    


# this is the optimized version of my code:


def maxDistinctElements(self, nums: list[int], k: int) -> int:

    if not nums:
        return 0 # if there are no numbers

    nums.sort()
    nums[0] -= k
    last = nums[0]
    current = 0
    count = 1 # this keeps count of the unique.

    for num in nums[1:]: # this is faster than repeatedly accessing and checking with the while loop
        diff = last - num # the built-in min and max functions are slow.
        if diff > k:
            n = k
        elif diff < -k:
            n = -k
        else:
            n = diff

        current = num + n
        if n < k and current == last:
            current += 1
        if current > last:
            count += 1

        last = current
    return count

# this should make the optimizations better.

# it is not as fast as the fast solution from the internet due to few lookups.
# it just computes the highest and lowest possible value and check if it is in range of the current lowest value. It then just increases the current lowest value by 1.
# that is a way faster approach where it just checks the range instead of finding the specific number.
# It is still the same time complexity, since it doesn't scale differently, but I have more steps, which slows down the algorithm.