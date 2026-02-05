

# we need to find the traversal order you traverse through a binary tree with depth first search.

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

from typing import Optional
from typing import List

# I can start out by trying to find a recursive solution.
# it seems like inorder traversal is trying always to progress through the left node until there is no left node. Then go back to the last node also with a right.
# the right node is chosen and we again try to reach the most left node again, where we mark the bottom.


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        def InOrder(iroot: Optional[TreeNode]):
            if iroot != None:
                InOrder(iroot.left) # it passes down the left until it reaches the left end.
                result.append(iroot.val) # when it has reached the end, then a value is added.
                InOrder(iroot.right) # the right is then explored after a left end has been met.

                
                
                
        InOrder(root)

        return result
            
            # if no roots exist for the current root, then it should be added as traversed.

# this was a recursive solution. Now it is time to try and write an iterative solutution with an actual stack instead of just using the call stack.

# postorder
"""
PostOrder(root.left)
PostOrder(root.right)
result.append(root.val) 
"""

# inorder
"""
InOrder(root.left)
result.append(root.val) 
InOrder(root.right)
"""

# preorder
"""
result.append(root.val)
PreOrder(root.left)
PreOrder(root.right)
"""



class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        
        stack = [root]
        head = root
        
        while stack:
            while head.left:
                stack.append(head.left)
                head = head.left # reassigns the head to the new node.
            # all the lefts are now exhausted, so now we make our way up the stack until we can go right.
            while stack: # while there is no right root, then we should just add the value.
                result.append(stack[-1].val)
                curr = stack.pop()
                if curr.right:
                    head = curr.right
                    stack.append(head)
                    break
                # the loop breaks, when it finds a tree with a right value.
        return result
        

    # this is the iterative solution

# a cleaner version


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        
        stack = [root]
        head = root
        
        while head or stack:
            while head:
                stack.append(head)
                head = head.left # reassigns the head to the new node.
            # all the lefts are now exhausted, so now we make our way up the stack until we can go right.
            head = stack.pop()
            result.append(head.val)
            head = head.right # if there is no right value, then a new one from the stack will be taken.
        return result