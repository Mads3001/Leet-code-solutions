



# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Optional:
   list[ListNode]

from typing import List
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
       
        # we get the head of the listnode.
        # we can start by putting nums into a set.
        n = set(nums) # this makes the lookup faster.
        dummy = ListNode(0) # in case the head node gets removed, then we initialize a dummy node.
        dummy.next = head 
        # we get a linked list set and needs to keep track of the last valid value and next.
        current = dummy
        while current.next:
           
            if current.next.val in n: # if the next nodes value needs to be skipped, then the pointer will get reassigned.
                current.next = current.next.next
            else:
               current = current.next

        return dummy.next
              
# the code works, but is ineffecient, since it cal lead to many reassignments, if multiple values in a row needs to be skipped. Instead a loop that can check forward would be better.

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        prev=head
        sety=set(nums)
        while head.val in sety:
            head=head.next
        prev=head
        temp=head
        if head.next:
            head=head.next
            while head: # this extra loop skips many redundant reassignments.
                if head.val not in sety:
                    prev.next=head
                    prev=head
                head=head.next
            if prev.next and  prev.next.val in sety:
                prev.next=None
        return temp   
        

    
       
