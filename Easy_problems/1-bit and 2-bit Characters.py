
# A binary string is given. Some characters are encoded with two bits and some with only 1 bit.
# We need to check if the string is ending with some 1-bit encoding. The 1-bit encoding can only be "0", while the 2-bit encoding can be either "11" or "10".

from typing import List
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # each time the code hits a one, then it can only be a part of 2-bit encoding.
        # then it should claim the next digit. And skip forward.
        # 
        two_bit = False
        l = len(bits)
        i = 0
        while i < l:
            if bits[i] == 1:
                two_bit = True
                i += 2
            else:
                two_bit = False
                i += 1
        if two_bit:
            return False
        return True


b = [1,1,1,0]

inp = Solution()
print(inp.isOneBitCharacter(b))