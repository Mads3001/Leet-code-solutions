

# in this problem you'll get two linked lists.
# The value in a node is one digit of the real number.
# the numbers in the linked list needs to be reversed and then added.
"""""
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

"""

# they kind of behave like a list, so I'll start by writing a solution for a list.


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def addTwoNumbers(self, l1, l2):
        
        node1 = l1
        num1_str = "" 
        node2 = l2
        num2_str = ""



        while node1: # this loop is active until it reaches the last node in that list
            num1_str += str(node1.val)
            node1 = node1.next

        while node2:
            num2_str += str(node2.val)
            node2 = node2.next

        reverse_num1_str = str(num1_str)[::-1] # the values added need to be reversed before added
        reverse_num2_str = str(num2_str)[::-1]

        total = int(reverse_num1_str) + int(reverse_num2_str)
        # now we have the total as an integer.
        # that needs to be a string, so we can subscribt and reverse it.
        reverse_total = str(total)[::-1]
        # in this case the total also needs to be reversed again when written to a new listnode.
        # we now need to assemble the string to a listnode

        return_node = ListNode() # this initializes a dummy empty node containing .val=0 for the first node.
        node = return_node
        for n in str(reverse_total):
            node.next = ListNode(int(n))
            node = node.next
        return return_node.next # because of the dummy node it returns the .next version

input1 = [ListNode(val=2, next=4), ListNode(val=4, next=3)]
input2 = ListNode()
[2,4,3]
print(str(input1[0].val))


