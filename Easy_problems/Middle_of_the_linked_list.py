
# there will be a list of intergers from 1 to n. The function needs to return the end half of the list. If there's an uneven amount of values (two middle values) 
# it will need to be the value closest to the end
from dataclasses import dataclass


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def middleNode(self, head: ListNode) -> ListNode:
    middle_node = head
    end_node = head
    while end_node and end_node.next:
        middle_node = middle_node.next
        end_node = end_node.next.next
    return middle_node

def build_linked_list(values):
    head = ListNode(values)
    node = head
    for v in values[1:]:
        node.next = ListNode(v)
        node = node.next
    return head

head = build_linked_list([1,2,3,4,5])
result = middleNode(0, head)
print(result)

