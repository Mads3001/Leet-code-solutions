

# the input is a list of nodes.
# the output should be a copy, but not the same node



# Definition for a Node.

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        seen = set() # to store the values that have already been seen
        stack = []
        dummy = Node() # the dummy is the new system that will be filled in.
        dummy.val = node.val
        curr = dummy

        head = node # this is the original node
        while curr.val not in seen:
            for neighbor in curr.neighbors: # this adds the neighbors of the current value.
                stack.append(neighbor)

from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        q = deque([node]) # we can apparently make the nodes into a listlike structure, so we can iterate.
        clones = {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft() # this takes the node and creates a clone out of that.
            cur_clone = clones[cur.val]            

            for ngbr in cur.neighbors: # then it takes the popped node and extracts the neighbors.
                if ngbr.val not in clones: # check, if the value already has a clone.
                    clones[ngbr.val] = Node(ngbr.val, []) # creates the value for a node, if it doesn't exist yet.
                    q.append(ngbr)
                    
                cur_clone.neighbors.append(clones[ngbr.val]) # this appends the neighbors to the neighbor
                
        return clones[node.val]

# a dfs solution:
# it just utilizes, that it is another scope, so it can more easily transfer properties as a deep copy.
def cloneGraph(self, node: 'Node') -> 'Node':
        old_to_new = {}
        
        def clone(node):
            if node in old_to_new:
                return old_to_new[node]
            
            copy = Node(node.val)
            old_to_new[node] = copy
            
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy 
        
        return clone(node) if node else None