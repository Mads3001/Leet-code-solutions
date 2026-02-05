

# the functions has a list and an integer as input. All instances of the integer needs to be removed from the list.
# the amount of remaining values gets returned as k.
# the function modifies the input array and does not output a list.


def removeElement(self, nums: list[int], val: int) -> int:
    
    while val in nums:
        nums.remove(val)

    return len(nums)



numbers = [0,1,2,2,3,0,4,2] 
val = 2
print(removeElement(0, numbers, val))
print(numbers)