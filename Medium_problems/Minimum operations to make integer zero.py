

# A functions is given two integers as input.
# The first integer needs to be turned into 0.
# it can be done by subtracting 2 ** i + num2 from num1
# i can be choosen for each iteration of the operation
# if it cannot be turned to 0, then the function must return -1
# if it can, then the integer returned is the number of operations needed to turn it into zero
# since we have 2 as a base in the subtracting, then it can make sense to use binary

# I reckon the problem can be solved by finding out what can't be removed by 2 ** i and must be removed by num2.
# I don't know, if it is the minimum amount of steps though.


# another approach could be to how many operations are needed to construct num1 out of only adding 2 ** i + num2

def makeTheIntegerZero(self, num1: int, num2: int) -> int:
    # we can maybe start by represinting the numbers with bits
    # from the looks of it, num2 must be present in num1 bitwise for it to reach zero.
    # by minimum 2 ** i can be a minimum of 1. It is just taking a bit from i place.
    num1 = bin(num1)
    num2 = bin(num2)
    # converting the numbers to binary
    # the target = num1 and target = sum(2 ** i_j) + k * num2. j can be any number.

    # I don't know enough about the math and how to use binary to solve this question. I will instead look at a submission and learn from the code.



# notes to the real solution "https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/solutions/7156791/beats-100-0ms-bit-manipulation-full-explanation/?envType=daily-question&envId=2025-09-05"
#:
# Since the upper limit for i in this case is 60, then we know the maximum number 1 can be is 60 binary ones and a num2 as 0. the number of operations, when we work backwards is:
# s = num1 - t * num2. s should then be zero at last.
# On the way down s must be greater than num2 for the next step to happen.
# this needs to be true "popcount(s) <= t <= s" popcount is how many "1" bits are needed to represent s.
# we can now iterate over every value of t range(0, 60).
# because both s = num1 - t * num2 and popcount(s) <= t <= s, then t = popcount(s), if it's valid. That is because s is the amount of bits being "1" in binary representation ---
# --- left after num1- t * num2. They can be romved by the "- 2 ** i" step, since it can remove one binary digit per iteration.
# the code iterates from 0 to 60 and just returns the first valid value of t.
# if a valid value isn't found, then the code returns 1.
"""
The edge cases and how they interact:
Use a wider integer type (e.g., long long / long) for s = num1 - t * num2 because intermediate multiplication may overflow 32-bit.
(only for languages with set integer lengths)

If num1 == 0, the answer is 0 (no operations needed).

If num2 is negative, s may grow with t, so exploring up to 60 is still necessary.

If s is extremely large, popcount still works, but t <= s check prevents impossible small t values.

"""

"""
counting bits in python can be done with:
Python: bin(x).count('1') or use x.bit_count() in Python 3.8+

bit_count() counts 1 and 
bit_length() counts every digit
"""
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        if num1 == 0:
            return 0

        for t in range(0, 61):  # 0..60
            s = num1 - t * num2
            if s < 0:
                continue # if it doesn't reach this, then the for loop terminates.
            if s < t:
                continue
            # Python 3.8+: bit_count gives number of set bits
            ones = s.bit_count() # bit count was only needed for other purposes than i originally thought.
            if ones <= t:
                return t
        return -1
    
