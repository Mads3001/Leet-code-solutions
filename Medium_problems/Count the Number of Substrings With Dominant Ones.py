

# the input is a string of 1s and 0s. We need to count the amount of dominant substrings, where the 1 is dominant. 
# 1 is dominant, if there are less or equal occurences of sqrt(n) where n is the amount of 1s.

# the problem is the substrings can also be really large.
# the sliding window approach i flawed. The substrings can get really large, so to catch all the substrings we need to check almost all substrings.
# that makes the sliding window approach very inefficient.

# instead we can create an array with tuples. The tuples should contain the amount of 1s and 0s to the left of the current index (inclusive the index).

class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        dp = [] # this is some form of dynamic programming (I think)

        if s[0] == "1":
            dp.append((0,1))
        else:
            dp.append((1,0))
        for i, c in enumerate(s[1:]):
            if c == "1":
                dp.append((dp[i][0], dp[i][1] + 1))
            else:
                dp.append((dp[i][0] + 1, dp[i][1]))
        # this loop should construct something we can do the window search on.
# this doesn't really work. It still becomes wayyy too much, when it is over 40k length

from numpy import sqrt
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        pref = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref[i+1] = pref[i] + (ch == '1')

        Z = [i for i, ch in enumerate(s) if ch == '0']
        m = len(Z)

        ans = 0

        i = 0
        while i < n:
            if s[i] == '0':
                i += 1
                continue
            j = i
            while j < n and s[j] == '1':
                j += 1
            L = j - i
            ans += L * (L + 1) // 2
            i = j

        B = sqrt(n) + 2

        def ones(l, r):
            return pref[r+1] - pref[l]

        for a in range(m):
            Lmin = 0 if a == 0 else Z[a-1] + 1
            Lmax = Z[a]
            if Lmin > Lmax:
                continue

            for z in range(1, B + 1):
                b = a + z - 1
                if b >= m:
                    break

                Rmin = Z[b]
                Rmax = Z[b + 1] - 1 if b + 1 < m else n - 1
                if Rmin > Rmax:
                    continue

                need = z * z
                r = Rmin

                for l in range(Lmin, Lmax + 1):
                    if pref[Rmax + 1] - pref[l] < need:
                        continue
                    while r <= Rmax and ones(l, r) < need:
                        r += 1
                    if r > Rmax:
                        break
                    ans += (Rmax - r + 1)

        return ans

# This takes all the blocks of consecutive 1s and creates all possible substrings of these blocks.
# Then it takes all the blocks and goes with a two-pointer approach to the sides, where the substrings can include zeroes. 



