class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k != 0: return False
        if k == 1: return True
        
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        minH = sorted(counter.keys())
        heapq.heapify(minH)
        
        while minH:
            root = minH[0]
            setsCnt = counter[root]
            for num in range(root, root+k):
                if num not in counter:
                    return False
                
                counter[num] -= setsCnt
                if counter[num] < 0:
                    return False
                if counter[num] == 0:
                    heapq.heappop(minH)
        return True