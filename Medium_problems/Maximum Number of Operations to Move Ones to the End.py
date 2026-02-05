# the function should take a string of 1's and 0's.
# this is a problem where you take the "1" furthest to the left and move it right until it hits another 1.
# this calculates the maximum amount of operations that are possible.

class Solution:
    def maxOperations(self, s: str) -> int:
        # the amount of operations the leftmost element needs to take is equivalent to the amount of 0 gaps to the right of it.
        # then we actually just need to count the gaps for each element.
        # we should start out by counting the amount of gaps after the first occurence of 1.
        ops = 0
        i_gap = []
        gaps = 0
        for i, n in enumerate(s[s.find("1"):-1],s.find("1")): # the first elements are not counted
            if n == "1":
                i_gap.append(-gaps)
                if s[i + 1] == "0":
                    print(i, n)
                    gaps += 1
        for gap in i_gap:
            ops += gap + gaps
        return ops
        
            
        # maybe we can find a way to pass this at once
        # another list is not that effecient. We need to store it better



#j = "1001101"
j = "00111"
inp = Solution()

print(inp.maxOperations(j))


class Solution:
    def maxOperations(self, s: str) -> int:

        ops = 0
        count = 0
        gaps = 0
        start = s.find("1")
        for i, n in enumerate(s[start:-1],start): # the first elements are not counted
            if n == "1":
                ops -= gaps
                count += 1
                if s[i + 1] == "0":
                    gaps += 1
        ops += gaps * count
        return ops

# this is even slower. About half speed. And it only uses a bit less memory. This is a bad solution even though it is O(N)
# since it will be symmetrical we could try to just add the current gaps to the ops


class Solution:
    def maxOperations(self, s: str) -> int:
        ops = 0
        gaps = 0
        start = s.find("1")
        for i, n in enumerate(s[start:-1],start): # the first elements are not counted
            if n == "1":
                gaps += 1
            elif i > 0 and s[i - 1] == '1':
                ops += gaps
                    
        return ops


# the faster solutions is:
class Solution:
    def maxOperations(self, s: str) -> int:
        ones = [len(i) for i in s.split('0') if i] # this splits at all the zeroes. After that, it adds the length of each string of remainding ones
        if not ones:
            return 0
        tot = 0
        ans = 0
        for f in ones[:-1]: # this has the same logic of how it accumulates the total as the one above.
            tot += f
            ans += tot
        if s[-1] == '1': # if the last one is not a zero. It needs to add again, if the last is zero.
            return ans
        return ans + tot + ones[-1]
