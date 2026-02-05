

from collections import deque

class Router:

    def __init__(self, memoryLimit: int): # this should initialize a router with an assigned amount of memory.
        self.memory = memoryLimit
        self.packets = deque([]) # this list is a deque, which can efficiently add and subtract elements from both the front and end. This keeps account of the order of packets.
        # we store all the information in a nested list in packets.
        self.seen = set([])
        self.receivers = {}
        
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool: 
        # this adds a packet to the router. If the amount of packets exceed the memory limit, then the oldest is deleted
        # there cannot be added duplicates. It needs to be a new one. True is returned, if added. False, if its a duplicate.
        # packets are always added with ascending timestamp, so the first element of the list is always removed, when running out of memory.
        
        packet = [source, destination, timestamp]
        string_packet = str(packet) # lists can't be added to a set, so it will be converted to a string
        if string_packet in self.seen: # check for duplicate
            return False
        # if it isn't a duplicate, then the memory is checked.

        if len(self.packets) == self.memory: # if the memory is full, then the first packet is removed.
            removed_packet = self.packets.popleft()
            self.seen.remove(str(removed_packet)) # (OPTIONAL) the removed packet is now a valid packet.
            # it doesn't actually need to be removed from the seen, since it the timestamp can't show up again in normal use
            # the code would cover an edge case, if all the packets have the same timestamp and the next packet is the same as the first one.
            self.receivers[removed_packet[1]].remove(removed_packet[2]) # the timestamp is also removed from the recipient, when the packet is removed
            # the code also needs to remove the packet from self.receivers
             
        # this creates a destination list, if it doesn't exist yet
        if destination not in self.receivers:
            self.receivers[destination] = []
        

        self.seen.add(string_packet) # if it isn't seen before it is added to the seen set.
        self.packets.append(packet) # it then adds the packet to the list
        self.receivers[destination].append(timestamp) # the timestamp to that destination is noted, so it can get counted later.
        return True # if everything suceeds, then it returns true.

    def forwardPacket(self) -> list[int]:
        # this returns the FIFO (first in first out: the lowest timestamp) packet as an array. If there's no packets, then it is an empty array. 
        # the packet is also removed.
        packet = [] # it starts out as empty

        if self.packets: # if there are any packets
            packet = self.packets.popleft() # removes the leftmost element
        # now it also needs to be removed from seen and receivers.
            self.seen.remove(str(packet))
            self.receivers[packet[1]].remove(packet[2])
        return packet     

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        # returns the amount of packets to a certain destination within starttime to endtime.
        # this can be done fast by also keeping a list of destinations where each destination has a list of the packets with their times noted.
        dest_list = self.receivers[destination]
        count = sum(1 for x in dest_list if startTime <= x <= endTime)
        return count
        # we now only need to count the elements in the list that fits the criteria.
# this should work

# because keeping track of who is currently getting sent packets are stored in a normal list, it is very slow, when it is called repeatedly.
# a more efficient data structure is needed.

# the more efficient version is now coded down here with comments where it is changed

from sortedcontainers import SortedList # this makes all the lists sorted, which makes the time complexity of removing to O(log n) instead of O(n)
# the counting in an interval is also vastly improved.

class Router:

    def __init__(self, memoryLimit: int): 
        self.memory = memoryLimit
        self.packets = deque([]) 
        self.seen = set([])
        self.receivers = {}
        
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool: 
        
        packet = [source, destination, timestamp]
        string_packet = str(packet) 
        if string_packet in self.seen: 
            return False
        
        if len(self.packets) == self.memory:
            removed_packet = self.packets.popleft()
            self.seen.remove(str(removed_packet)) 
            self.receivers[removed_packet[1]].remove(removed_packet[2])              
        
        if destination not in self.receivers: # if the list from the destination isn't existing, then it instead creates a sorted list.
            self.receivers[destination] = SortedList()
            # the sorted list makes it much faster to count out intervals and remove values.

        self.seen.add(string_packet) 
        self.packets.append(packet) 
        self.receivers[destination].add(timestamp) # you just add to a sorted list. It doesn't end up at the end.
        return True 

    def forwardPacket(self) -> list[int]:

        if not self.packets: # for clarity's sake it is better to write a return for the exception.
            return []

        packet = self.packets.popleft() 
        self.seen.remove(str(packet))
        self.receivers[packet[1]].remove(packet[2])
        return packet
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        
        # a check if the destination checked doesn't exist
        if destination not in self.receivers:
            return 0 # if it doesn't exist, then there is zero packets to that destination
        
        dest_list = self.receivers[destination] 
        # because the list is sorted, then you can bisect the list much faster.
        left = dest_list.bisect_left(startTime)
        right = dest_list.bisect_right(endTime)

        return right - left
        # I don't know if it is inclusive.


# the seen is actually basically useless. it ends up being nearly as big as the memory without having any reason to exist.


# let's try with just checking in the normal self.packets instead of creating a self.seen
class Router:

    def __init__(self, memoryLimit: int): 
        self.memory = memoryLimit
        self.packets = deque([]) 
        self.receivers = {}
        
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool: 
        
        
        packet = [source, destination, timestamp]
        if packet in self.packets: 
            return False
        


        if len(self.packets) == self.memory:
            removed_packet = self.packets.popleft()
            self.receivers[removed_packet[1]].remove(removed_packet[2]) 
             
        
        if destination not in self.receivers: # if the list from the destination isn't existing, then it instead creates a sorted list.
            self.receivers[destination] = SortedList()
            # the sorted list makes it much faster to count out intervals and remove values.

        self.packets.append(packet) 
        self.receivers[destination].add(timestamp) # you just add to a sorted list. It doesn't end up at the end.
        return True 

    def forwardPacket(self) -> list[int]:

        if not self.packets: # for clarity's sake it is better to write a return for the exception.
            return []

        packet = self.packets.popleft() 
        self.receivers[packet[1]].remove(packet[2])
        return packet
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        
        # a check if the destination checked doesn't exist
        if destination not in self.receivers:
            return 0 # if it doesn't exist, then there is zero packets to that destination
        
        dest_list = self.receivers[destination] 
        # because the list is sorted, then you can bisect the list much faster.
        left = dest_list.bisect_left(startTime)
        right = dest_list.bisect_right(endTime)

        return right - left
        # I don't know if it is inclusive.

# nope, it is very much needed apparently.