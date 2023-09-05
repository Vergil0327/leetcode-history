"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = p = Node(-1)
        clone = {}
        cur = head
        while cur:
            clone[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            p.next = clone[cur]
            if cur.random:
                p.next.random = clone[cur.random]
            cur = cur.next
            p = p.next
        return dummy.next

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # make clone of each node and link them side by side
        # Node1 -> Node1_Clone -> Node2 -> Node2_Clone -> ...
        cur = head
        while cur:
            nxt = cur.next

            clone = Node(cur.val)
            cur.next = clone
            clone.next = nxt

            cur = nxt

        # assign random pointer
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # restore linked-list
        dummy = Node(0)
        p = dummy

        cur = head
        while cur:
            nxt = cur.next.next

            clone = cur.next
            p.next = clone
            p = p.next

            cur.next = nxt
            cur = cur.next

        return dummy.next
