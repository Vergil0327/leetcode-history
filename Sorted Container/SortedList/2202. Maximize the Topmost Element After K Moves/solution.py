from sortedcontainers import SortedList

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums) < 2 and k%2: return -1
        
        queue = deque(nums)
        sl = SortedList()
        last = None
        while queue and k:
            last = queue.popleft()
            sl.add(last)
            k -= 1

        if k == 0:
            if queue:
                if last:
                    sl.remove(last)
                return max(sl[-1] if sl else -1, queue[0])
            if last:
                sl.remove(last)
            return sl[-1] if sl else -1
        
        return sl[-1]


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k == 0: return nums[0] if nums else -1
        if k == 1: return -1 if n == 1 else nums[1]
        if n == 1: return -1 if k%2 else nums[0]

        mx = max(nums[:min(k-1, n)]) # we can take k-1 elements and put largest one back to top
        if k < n:
            return max(mx, nums[k]) # 最後一次操作選擇: max(放最大元素置頂, 取走k-th element後的topmost element)
        return mx # 放置最大元素回去
