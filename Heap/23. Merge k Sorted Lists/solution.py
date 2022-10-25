# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# nlogk
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        minH = [] # [node.val, index in lists]
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minH, [node.val, i])
            
        dummy = ListNode()
        curr = dummy
        while minH:
            _, idx = heapq.heappop(minH)
            
            curr.next = lists[idx]
            curr = curr.next
            if lists[idx].next:
                heapq.heappush(minH, [lists[idx].next.val, idx])
                lists[idx] = lists[idx].next
            
        return dummy.next


class SolutionMergeSort:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        if not lists or len(lists) == 0:
            return None
        
        # O(1) merge sort
        # N = len(lists)
        # interval = 1
        # while interval < N:
        #     for i in range(0, N-interval, interval*2):
        #         lists[i] = self.merge(lists[i], lists[i+interval])
        #     interval *= 2

        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None
                mergedList.append(self.merge(l1, l2))
            lists = mergedList
        return lists[0]
    
    def merge(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
                
        if l1: curr.next = l1
        if l2: curr.next = l2
            
        return dummy.next
            