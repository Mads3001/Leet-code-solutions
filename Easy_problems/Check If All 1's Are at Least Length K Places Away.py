

from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        dist = k
        for num in nums:
            if num == 0:
                dist += 1
            else:
                if dist < k:
                    return False
                dist = 0
        return True

def kLengthApart(nums: List[int], k: int) -> bool:   
    dist = k
    for num in nums:
        if num == 0:
            dist += 1
        else:
            if dist < k:
                return False
            dist = 0
    return True

# Feel free to write your own test cases and see, if you get the expected behaviour.
# If you are in doubt, if your function returns the correct answer, then try to check against my posted solution.
# The test cases are: [nums, k, expected_answer]
test_cases = [
    [[1,0,0,0,1,0,0,1], 2, True],
    [[1,0,0,1,0,1], 2, False],
    [[0,1,0,0,1,0,0,1], 2, True],
    [[0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0], 1, False],
    [[1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1], 0, True],
    [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0], 3, True],
    [[0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], 3, True],
    [[0,0,0], 2, True]
]

# This loop just iterates over the supplied test cases and assess, if it is expected behaviour.
for n, test_case in enumerate(test_cases, 1):
    result = kLengthApart(test_case[0], test_case[1])
    if  result == test_case[2]:
        print(f"Test case {n} succeeded ({test_case[2]}).")
    else:
        print(f"Something went wrong with test case {n}. Got {result}, but expected {test_case[2]}.")