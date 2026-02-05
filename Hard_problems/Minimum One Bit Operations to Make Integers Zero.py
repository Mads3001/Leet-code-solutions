

"""
Reworded Description:

Transform the given integer n into 0.

For any given operation you perform, you may only modify:

    The rightmost bit
    The bit to the left of the rightmost 1 bit.

    Example:
    In the binary string 011010 you may only modify bits with indices 0 and 2 (0-indexed from the right of binary representation).
    NOTE: Bit with index 0 may be modified as it is the rightmost bit, bit with index 2 may be modified as it is the bit to the left of the rightmost 1 bit
    [0, 1, 1, 0, 1, 0]= BITS
    [5, 4, 3, 2, 1, 0]= INDICES

Return the minimum number of operations that are required to transform n into 0
"""

# we need to turn the string into an all set bitstring (all consisting of 1) and then convert all into 0's.


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ops = 0
        b = bin(n)
        l = len(str(b)) - 2
        s = str(b)
        zeroes = s.count("0")
        ops += zeroes
        ops += l
        return ops - 1
    

# that solution is wrong. It was different than i thought. That is because flipping the bit to the left makes all bits under that bit also flip to zero, hence we need to
# build up the stack of 1's again until we can flip another one of the higher bits.

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = 0
        while n: # that is because res is how many numbers that differ by just 1 bit.
            res ^= n
            n >>= 1
        return res
# in here is hidden some principles from gray code. The way the number scales is a mathematical identity.
