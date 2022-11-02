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

# O(n)
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/discuss/457728/O(n)-Python-and-C%2B%2B
class SolutionOptimized:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k != 0: return False
        if k == 1: return True
        
        # counter = collections.Counter(nums)
        counter = defaultdict(lambda: 0)
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for num in nums:
            start = num
            while counter[start-1]:
                start -= 1
            while start <= num:
                while counter[start]:
                    for nextNum in range(start, start+k):
                        if counter[nextNum] == 0:
                            return False
                        counter[nextNum] -= 1
                start += 1
        return True