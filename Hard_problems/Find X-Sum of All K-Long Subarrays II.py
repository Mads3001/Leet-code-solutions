


# this is similar to the medium one, but this has different constraints.


# this is the solution to the medium question:

from typing import List
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        ans = [] 

        def XSum(arr: List[int], l: int) -> int: # function each subarray needs to go through
            count = 0 # X-sum of an array

            if len(arr) <= l: # edge case with length needed exceeding actual length
                return sum(arr)
            
            unique = list(set(arr))

            if len(unique) <= l: # edge case with length needed exceeding unique elements
                return sum(arr)
            
            for i, value in enumerate(unique):
                unique[i] = (arr.count(value), value) # (frequency, value)
            
            unique.sort(reverse=True) # sort by frequency first. value if tied. (trick with tuples)
            
            for _ in range(l):
                count += unique[_][0] * unique[_][1] # frequency * value
            return count
        
        for _ in range(len(nums) - k + 1): # the answer need to be of length "n - k + 1", since that amount of subarrays exist.
            ans.append(XSum(nums[_:k + _], x)) # every subarray is fed to the Xsum function
        
        return ans
    



# this time we must utilize, that we can reuse the array, since only one element changes from the first to the next subarray.

# we can keep track of the elements by using a heap and a frequency map
# the frequency map pushes updates to the heap.


import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        ans = []
        

        def update_heap(heap, freq_map, value):
        # When frequency changes, remove old and add (frequency, value) tuple
            heapq.heappush(heap, (-freq_map[value], value)) # negative for max-heap
        def xsum(heap, x): # this takes the x elements with the highest frequency and sums all the occurences.
            if len(heap) <= x:
                return sum(-heap[i][0] * heap[i][1] for i in range(len(heap))) # takes all elements, if x is over the length of elements.
            return sum(-heap[i][0] * heap[i][1] for i in range(x))

        

        frequencies = {}# this just creates the frequency map
        for element in nums[:k]:
            frequencies[element] = (1 + frequencies.get(element, 0))

        heap = [(-freq, val) for val, freq in frequencies.items()] # This creates a list with the tuple of (frequecy, value) from the dictionary
        heapq.heapify(heap) # makes the list into a heap

        # the heap is ready to create the first xsum of the subarray.
        ans.append(xsum(heap, x))

        for _ in range(0, len(nums) - k + 1):
            pass
        return ans
    # there is a problem, since it is difficult to update a heap. This won't work.

# there is not a structure that makes this problem easy





import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)

        cnt = {}
        chosen = set()

        hot: list[tuple[int, int]] = []
        pool: list[tuple[int, int]] = []

        total = 0

        def clean():
            while hot and (hot[0][1] not in chosen or cnt.get(hot[0][1], 0) != hot[0][0]):
                heapq.heappop(hot)
            while pool and ((-pool[0][1]) in chosen or cnt.get(-pool[0][1], 0) != -pool[0][0] or -pool[0][0] == 0):
                heapq.heappop(pool)

        def demote_if_chosen(v: int):
            nonlocal total
            if v in chosen:
                chosen.remove(v)
                total -= v * cnt.get(v, 0)

        def promote_if_needed():
            nonlocal total
            clean()
            while len(chosen) < x and pool:
                f, v = -pool[0][0], -pool[0][1]
                if cnt.get(v, 0) != f or v in chosen or f == 0:
                    heapq.heappop(pool)
                    continue
                heapq.heappop(pool)
                chosen.add(v)
                total += v * f
                heapq.heappush(hot, (f, v))
            clean()

        def add_one(v: int):
            nonlocal total
            demote_if_chosen(v)
            f = cnt.get(v, 0) + 1
            cnt[v] = f
            heapq.heappush(pool, (-f, -v))

            if len(chosen) < x:
                promote_if_needed()
            else:
                clean()
                if pool and hot:
                    bf, bv = -pool[0][0], -pool[0][1]
                    wf, wv = hot[0]
                    if bf > wf or (bf == wf and bv > wv):
                        heapq.heappop(pool)
                        chosen.add(bv)
                        total += bv * bf
                        heapq.heappush(hot, (bf, bv))

                        heapq.heappop(hot)
                        if wv in chosen:
                            chosen.remove(wv)
                            total -= wv * wf
                        heapq.heappush(pool, (-wf, -wv))
                clean()

        def remove_one(v: int):
            nonlocal total
            demote_if_chosen(v)
            f = cnt.get(v, 0) - 1
            if f <= 0:
                cnt.pop(v, None)
            else:
                cnt[v] = f
                heapq.heappush(pool, (-f, -v))
            promote_if_needed()

        for i in range(k):
            add_one(nums[i])
        ans[0] = total

        for i in range(k, n):
            remove_one(nums[i - k])
            add_one(nums[i])
            ans[i - k + 1] = total

        return ans