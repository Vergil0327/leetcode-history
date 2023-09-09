"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node()

        cur = dummy
        stack = [head]
        while stack:
            node = stack.pop()
            while node:
                cur.next = node
                cur.next.prev = cur
                cur = cur.next

                if node.child:
                    child = node.child
                    node.child = None
                    stack.append(node.next)
                    node = child
                else:
                    node = node.next
        
        res = dummy.next
        if res:
            res.prev = None 
        return res