
# the input is a string of 1's and 0's. The output should be the amount of substrings strictly consisting of 1's.
# an all 1 string has L * (L + 1) // 2 substrings with only 1.
# since there are many, then the final output should be modulo 10^9 + 7



class Solution:
    def numSub(self, s: str) -> int:
        # there should just be a loop that finds the length of a given segment of ones and the adding it to the count.
        count = 0
        l = 0
        for c in s:
            if c == "1":
                l += 1
            else:
                count += l * (l + 1) // 2
                l = 0
        return count % (10**9 + 7)