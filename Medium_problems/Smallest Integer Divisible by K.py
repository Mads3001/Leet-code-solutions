

# the input is a number "k", where we need to find a number n, that is divisible by k. is a number where every digit is 1.
# this is a problem of repeating remainders. If we spot the same remainder twice, then there is no improvement and the answer does not exist.

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n = 0
        seen = set()
        l = 0

        while 0 not in seen:
            n = (10 * n + 1) % k
            l += 1
            if n in seen:
                break
            seen.add(n)
        print(seen)
        if 0 in seen:
            return l
        return -1
        

            

inp = Solution()
k = 3

print(inp.smallestRepunitDivByK(k))


