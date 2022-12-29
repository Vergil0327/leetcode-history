# DFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def connectNext(root):
            if not root: return root
            if root.left: return root.left
            if root.right: return root.right
            return connectNext(root.next)

        def conn(root):
            if not root: return root
            
            if root.left:
                if root.right:
                    root.left.next = root.right
                else:
                    root.left.next = connectNext(root.next)
            if root.right:
                root.right.next = connectNext(root.next)

            conn(root.right)
            conn(root.left)

            return root
        return conn(root)


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root
        head = tail = None # head of the next level, the leading node on the next level
        
        while curr:
            while curr: # iterate current level
                # left node
                if curr.left:
                    if tail:
                        tail.next = curr.left
                    else:
                        head = curr.left
                    tail = curr.left
                
                # right node
                if curr.right:
                    if tail:
                        tail.next = curr.right
                    else:
                        head = curr.right
                    tail = curr.right
                
                # move to next node horizontally    
                curr = curr.next
            
            # move to next level & reset head and tail to repeat process iteratively
            curr = head
            head = tail = None

        return root
