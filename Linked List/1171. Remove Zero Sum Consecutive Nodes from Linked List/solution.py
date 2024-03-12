# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # linked list to array
        nodes = []
        cur = head
        while cur:
            if cur.val == 0:
                cur = cur.next
                continue
            nodes.append(cur)
            cur = cur.next

        presum = 0
        seen = {0: 0}
        res = []
        for node in nodes:
            presum += node.val
            if presum in seen:
                size = seen[presum]
                presum -= node.val
                while res and len(res) > size:
                    del seen[presum]
                    presum -= res.pop().val
            else:
                res.append(node)
            seen[presum] = len(res)

        # array to linked list
        dummy = ListNode()
        cur = dummy
        for node in res:
            cur.next = node
            cur = cur.next
        cur.next = None
        return dummy.next
