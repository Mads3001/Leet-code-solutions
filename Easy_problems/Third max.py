
# there will be 3 ocassions where the max is looked for in an array. The first 2 values of max will be discarded. Then the third is returned.
# if the third does not exist, then the first max will be returned


def thirdMax(self, nums: list[int]) -> int:
    numbers = set(nums) # a set can be easier, when there are many duplicates.
    if len(numbers) < 3:
        return max(numbers)
    
    max_number = max(numbers) # the first max will be discarded
    numbers.discard(max_number)

    max_number = max(numbers) # the second max will be discarded
    numbers.discard(max_number)

    return max(numbers) # the third max will be returned, if there are any elements left.

# a better solution, when there are many numbers and finding the max can be ineffecient.


def thirdMax(self, nums: list[int]) -> int:
    
    numbers = list(set(nums)) # a set can be easier, when there are many duplicates.
    # this sequence eliminates dupes
    numbers.sort(reverse=True)

    if len(numbers) >= 3: # The third max is returned, if there's 3 or more elements
        return numbers[2]
    
    return numbers[0] # This is the max, if there's not enough elements for a third max.



input = [3,2,1]

print(thirdMax(0, input))

# the more memory