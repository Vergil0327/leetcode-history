# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []

        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        n = len(nodes)
        nodes[k-1], nodes[n-k] = nodes[n-k], nodes[k-1]

        nodes.append(None)
        for i in range(n):
            nodes[i].next = nodes[i+1]
        return nodes[0]