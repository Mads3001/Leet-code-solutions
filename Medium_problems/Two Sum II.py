
# this time the array is sorted.
# all tests are made, so there is exactly one solution.
# Since the input is sorted we can use binary search to find if the corresponding number exists.
# for some ungodly reason it is 1-indexed, so it starts with 1 instead of 0.



def twoSum(self, numbers: list[int], target: int) -> list[int]:

    length = len(numbers)
    for i in range(numbers): # this will yield the index.
        number2 = target - numbers[i] # this is what needs to be found in the array.
        
        # now the binary search should begin until number2 is hit
        left = 0
        right = length - 1 # the last index
        idx = 0 # this is the index of the value we need to find. default, if it can't be found

        while left <= right:
            mid = (left + right) // 2 # this is the middle of the currently searched part.

            if numbers[mid] >= number2:
                idx = mid # idx is now the middle.
                right = mid - 1 # this now sets the new rightmost bound.
            else:
                left = mid + 1 # this shifts the search over the right half, if the value is too small.
        if idx != i and numbers[idx] + numbers[i] == target:
            return [i + 1, idx + 1].sort()
        # there is only one solution, so we need to make a failsafe, when it failed to find the correct number.
        # the loop will get stuck on the same place and 

    # the returned indices needs to be increased by 1, since the array is 1-indexed.


# i can also try a solution with a hashmap.
# binary search is honestly not the way to solve this

def twoSum(self, numbers: list[int], target: int) -> list[int]:

    needed = {}

    for i, number in enumerate(numbers): # since this creates a new "number" for each step, but it doesn't need to be changed, then it can maybe be better to just range(len())
        if target - number in needed:
            return [needed[target - number] + 1, i + 1]
        needed[number] = i

# this was much faster. 3 ms (beat 80,97 %) and 18,47 mb memory (beat 90,13 %).
# the first solution was much slower. 38 ms and 18,77 mb memory

def twoSum(self, numbers: list[int], target: int) -> list[int]:

    needed = {}

    for i in range(len(numbers)): 
        if target - numbers[i] in needed:
            return [needed[target - numbers[i]] + 1, i + 1]
        needed[numbers[i]] = i

