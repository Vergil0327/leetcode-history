# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        grid = [[-1]*n for _ in range(m)]

        i = j = 0
        left = 0
        right = n
        top = 0
        bottom = m

        cur = head
        # both of `while cur:` and `while left < right and top < bottom:` work
        while cur: # or while left < right and top < bottom:
            while j < right:
                if cur:
                    grid[i][j] = cur.val
                    cur = cur.next
                else:
                    return grid
                j += 1
            right -= 1
            top += 1
            i = top
            j = right

            while i < bottom:
                if cur:
                    grid[i][j] = cur.val
                    cur = cur.next
                else:
                    return grid
                i += 1
            i -= 1
            j -= 1
            bottom -= 1

            while j >= left:
                if cur:
                    grid[i][j] = cur.val
                    cur = cur.next
                else:
                    return grid
                j -= 1
            j = left
            i -= 1
            left += 1

            while i >= top:
                if cur:
                    grid[i][j] = cur.val
                    cur = cur.next
                else:
                    return grid
                i -= 1
            i = top
            j += 1

                
        return grid