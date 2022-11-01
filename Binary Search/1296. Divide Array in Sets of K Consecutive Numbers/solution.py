class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k != 0: return False
        if k == 1: return True
        
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        sortedList = []
        for num in sorted(nums):
            if not sortedList:
                sortedList.append([num, 1])
                continue

            idx = bisect.bisect_right(sortedList, [num, 1])

            if sortedList[idx-1][0] == num-1:
                if sortedList[idx-1][1] == k-1:
                    sortedList.pop(idx-1)
                else:
                    sortedList[idx-1][0] = num # tail num
                    sortedList[idx-1][1] += 1 # set size
            else:
                sortedList.append([num, 1])

        return len(sortedList) == 0

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        for num in sorted(nums):
            availableSets = counter[num]
            if availableSets > 0:
                for i in range(num, num+k):
                    if i not in counter:
                        return False

                    counter[i] -= availableSets
                    if counter[i] < 0:
                        return False
        return True

class SolutionOptimized:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        start = deque()
        tailNum, currOpened = -1, 0
        for num in sorted(counter):
            if currOpened > counter[num]: return False
            if currOpened > 0 and num != tailNum+1: return False
            
            start.append((counter[num] - currOpened)) # store count of current opened sets which first value in set is num
            tailNum = num
            currOpened = counter[num]
            if len(start) == k:
                currOpened -= start.popleft()

        return currOpened == 0