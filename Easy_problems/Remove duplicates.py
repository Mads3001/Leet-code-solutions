
# The function receives a sorted array
# it needs to return the sorted array, but just without duplicates.

"""
def removeDuplicates(self, nums: list[int]) -> int:
    # we can remove the duplicates by shifting the index and overwriting values, when finding duplicates.

    i = 0
    
    while len(nums) - 1  > i: # the problem consisted of i being less than the length. that would have i reaching the length of the array, which would lead to an error.

        if nums[i] == nums[i + 1]:
            nums.pop(i)
        else:
            i += 1
    return len(nums)
""" 




# that solution is slow and memory intensive.
# this solution is the same. Sigh, time to make a new one.
"""
def removeDuplicates(self, nums: list[int]) -> int:
    new_list = []
    for number in nums:
        if number not in new_list:
            new_list.append(number)
    nums [:] = new_list
    return len(nums)

numbers = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(0, numbers))

print(numbers)
"""
# maybe a dictionary is the better solution?

def removeDuplicates(self, nums: list[int]) -> int:
    
    numberchecker = {}

    for number in nums:
        numberchecker[number] = number

    nums [:] = list(numberchecker)

    return len(numberchecker)


numbers = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(0, numbers))

print(numbers)

# this makes the time only 1 ms for the tests. Still pretty memory intensive.


# the best solution form the internet is:

def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(i, len(nums)):
            if nums[j] != nums[i]: # i is the place to insert the unique number. It iterates ahead of duplicates and just keeps remark of where to insert a unique number, if found.
                i += 1
                nums[i] = nums[j]
        return i + 1
# it also overwrites the numbers, like my first solution, but does so in a faster manner and with less checks.