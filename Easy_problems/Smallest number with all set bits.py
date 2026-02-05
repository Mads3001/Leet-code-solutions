

# this code needs to return the smallest number with all set bits (consisting only of either 1 or only 0)
# since it needs to be bigger, then it must be only 1.


class Solution:
    def smallestNumber(self, n: int) -> int:
        # we should start by counting the amount of bits in n.
        # we should then compare to an all 1 bits with the same length as n. If n is bigger or equal we add another 1 bit.
        b = bin(n)
        l = len(str(b)) - 2
        a = ""
        for i in range(l):
            a += "1"
        if int(a, 2) < n:
            a += "1"
        return int(a, 2)


inp = Solution()

print(inp.smallestNumber(5))
#x = 5
#z = str(bin(x))
#print(z, len(z))
