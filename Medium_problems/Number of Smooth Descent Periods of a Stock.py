
# a smooth descent is when a stock decreases by exactly 1 the following day.
# each singular instance of a value is apparently counted as a smooth descent.
# each length in a sequence of smooth descents with length n, another element added adds n more variations of a smooth descent
# 2 1 has [2], [1], [2,1]. Originally only [2]
# 3 2 1 has [3], [2], [1], [3,2], [3,2,1], [2,1]
# I at least think that's the pattern.

from typing import List
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 0
        n = 1
        last = 0
        for price in prices:
            if last - 1 == price:
                n += 1
            else:
                n = 1
            last = price
            count += n
        return count

            
        
        
