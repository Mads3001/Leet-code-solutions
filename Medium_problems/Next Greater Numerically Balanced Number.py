
# the input is an integer n.
# the output needs to be the smallest number greater than n, which is numerically balanced. Being balanced means having the same frequency of the value as the value itself.
# eg. if the number contains 2, then it is appearing 2 times. If 3, then it appears three times and so forth.

# a basic solution is taking the number eg. "3000" and adding 3 to the first digit. That is done, so the final number become as small as possible.
# the max of the number should then be used as the lowest digit.
# the algorithm could keep track of the pre-existing numbers in the original.

# we can also just create a lookup list, since there is a limited amount of balanced numbers. The maximum balanced number with the given constraints is "666666"
# If the upper limit is bigger, then an optimised approach could be useful, with no upper limit. Since the amount of numbers is so limited, then a lookup table can --
# -- significantly speed up the time and be useful in real world applications instead of recomputing for each instance.

"""
[1, 22, 122, 212, 221, 333, 1333, 3133, 3313, 3331, 4444, 14444, 
22333, 23233, 23323, 23332, 32233, 32323, 32332, 33223, 33232, 33322, 
41444, 44144, 44414, 44441, 55555, 122333, 123233, 123323, 123332, 132233, 
132323, 132332, 133223, 133232, 133322, 155555, 212333, 213233, 213323, 213332, 
221333, 223133, 223313, 223331, 224444, 231233, 231323, 231332, 232133, 232313, 
232331, 233123, 233132, 233213, 233231, 233312, 233321, 242444, 244244, 244424, 244442, 
312233, 312323, 312332, 313223, 313232, 313322, 321233, 321323, 321332, 322133, 322313, 
322331, 323123, 323132, 323213, 323231, 323312, 323321, 331223, 331232, 331322, 332123, 
332132, 332213, 332231, 332312, 332321, 333122, 333212, 333221, 422444, 424244, 424424, 
424442, 442244, 442424, 442442, 444224, 444242, 444422, 515555, 551555, 555155, 555515, 
555551, 666666, 1224444]
"""


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        beautiful_numbers = [1, 22, 122, 212, 221, 333, 1333, 3133, 3313, 3331, 4444, 14444, 
22333, 23233, 23323, 23332, 32233, 32323, 32332, 33223, 33232, 33322, 
41444, 44144, 44414, 44441, 55555, 122333, 123233, 123323, 123332, 132233, 
132323, 132332, 133223, 133232, 133322, 155555, 212333, 213233, 213323, 213332, 
221333, 223133, 223313, 223331, 224444, 231233, 231323, 231332, 232133, 232313, 
232331, 233123, 233132, 233213, 233231, 233312, 233321, 242444, 244244, 244424, 244442, 
312233, 312323, 312332, 313223, 313232, 313322, 321233, 321323, 321332, 322133, 322313, 
322331, 323123, 323132, 323213, 323231, 323312, 323321, 331223, 331232, 331322, 332123, 
332132, 332213, 332231, 332312, 332321, 333122, 333212, 333221, 422444, 424244, 424424, 
424442, 442244, 442424, 442442, 444224, 444242, 444422, 515555, 551555, 555155, 555515, 
555551, 666666, 1224444]
        
        for number in beautiful_numbers:
            if number > n:
                return number
            
# that is a solution where the values are precomputed.

# this following solution has the code for precomputation:

from itertools import permutations

class Solution:
    balanced_numbers = None

    @staticmethod
    def init_balanced_numbers():
        s = set()
        bases = [
            "1", "22", "122", "333", "1333", "4444", "14444", "22333", "55555",
            "122333", "155555", "224444", "666666", "1224444", "1666666",
            "2255555", "3334444", "7777777", "12255555" # the bases add up to all the possible balanced numbers. They have d occurences of the digit d, so all other perfect numbers --
            # -- in the range given is just a permution of these.
        ]

        for base in bases:
            for p in set(permutations(sorted(base))): 
                s.add(int("".join(p)))
        return sorted(s)

    def __init__(self):
        if Solution.balanced_numbers is None:
            Solution.balanced_numbers = Solution.init_balanced_numbers()

    def nextBeautifulNumber(self, n: int) -> int:
        for x in Solution.balanced_numbers:
            if x > n:
                return x
        return -1

# the way leetcode executes code, it is in rapid successsion, so the lookup table can be conserved between calls.