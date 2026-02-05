
# there is a long input with all the actions that have been taken. There are timestamps, so you can retroactively find out, 

from typing import List
from collections import deque
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # the "here" is the most problematic. The easiest solution is probably to have a here counter that gets added to each element returned.
        # then, if an user is offline we just subtract one from their mentions, so it all adds up in the end.
        users = [0]*numberOfUsers # keep track of mentions. The user is their own index.
        offline = deque() # It's a first in first out scenario, so a deque is better. (user, active_again) where active_again is the time it must be over for the user to be active
        # we just make a loop that checks if the first user should be online again.
        uni_count = 0 # affects all users
        pings = set(['HERE', 'ALL'])

        events.sort(key=lambda x: (-int(x[1]), x[0]), reverse=True)
        # the events are not sorted by time when given the input. The time is very important to sort by, since the offline dictates the amount of pings.
        # When both messages and offline has the same timestamp, then we need to prioritize the offline query first.
        # We make the timestamps be sorted in ascending order, by reversing, but sorting with the negative value (kind of like a min/max heap with just negatives to flip)
        # The string is then the secondary determining factor. String sorting is alphabetical, so by reversing we get the offline queries first. 

        for type, time, receiver in events:
            
    
            if type == "MESSAGE":
                if receiver not in pings:
                    receivers = receiver.split()
                    for user in receivers:
                        users[int(user.strip("id"))] += 1
                elif receiver == "HERE":
                    uni_count += 1
                    while offline and offline[0][1] <= int(time): # removes people who become online again.
                        offline.popleft()
                    for user, back in offline:
                        users[user] -= 1 # offline users are not affected by "HERE"
                elif receiver == "ALL":
                    uni_count += 1
                

            else:
                offline.append((int(receiver), int(time) + 60))

        return [x + uni_count for x in users]

e = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]
n = 2

inp = Solution()
print(inp.countMentions(n,e))

                


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:

        users = [0]*numberOfUsers 
        offline = deque() # It's a first in first out scenario, so a deque is better. (user, active_again).
        uni_count = 0 # pings that can affect all users.
        pings = set(['HERE', 'ALL'])

        events.sort(key=lambda x: (-int(x[1]), x[0]), reverse=True)
        # the input is not sorted, so it primarily sorts by timestamp (ascending) and secondarily by action (offline queries first and works due to string sorting)

        for type, time, receiver in events:
            
    
            if type == "MESSAGE":
                if receiver not in pings:
                    receivers = receiver.split()
                    for user in receivers:
                        users[int(user.strip("id"))] += 1
                
                elif receiver == "HERE":
                    uni_count += 1
                    while offline and offline[0][1] <= int(time): # removes people who become online again
                        offline.popleft()
                    for user, back in offline:
                        users[user] -= 1 # offline users not affected by "HERE", so we subtract one of their mentions against the uni count
                
                elif receiver == "ALL":
                    uni_count += 1
                

            else:
                offline.append((int(receiver), int(time) + 60)) # adds offline people to a queue

        return [x + uni_count for x in users] # add "here" + "all" pings before returning all mentions