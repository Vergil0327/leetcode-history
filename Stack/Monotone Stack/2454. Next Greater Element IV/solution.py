# explanation: https://leetcode.com/problems/next-greater-element-iv/discuss/2756341/C%2B%2B-Java-Python3-Monotonic-Stack-%2B-Priority-Queue
# 1. found every j-th elements whose next greater is num at i-th position. push into nextGreaterAt
# 2. iterate through nums array again and use min heap to nextGreater's nextGreater element
class MaxHeapSolution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]: 
        nextGreaterAt = [[] for _ in range(len(nums))]
        stack = []
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                nextGreaterAt[i].append(stack.pop())
            stack.append(i)
            
        minHeap = [] # [num, index]
        res = [-1] * len(nums)
        for i, num in enumerate(nums):
            # found 2nd greater element
            while minHeap and minHeap[0][0] < num:
                _, idx = heapq.heappop(minHeap)
                res[idx] = num
            
            # i is next greater element's index of j-th element
            for j in nextGreaterAt[i]:
                heapq.heappush(minHeap, [nums[j], j])
        
        return res


# explanation: https://leetcode.com/problems/next-greater-element-iv/discuss/2756668/JavaC%2B%2BPython-One-Pass-Stack-Solution-O(n)
# 1. found next greater elements first
# 2. use next greater element to find next next greater again => 2nd greater element
class OnePassSolution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        nextGreater = []
        stack = []
        for i, num in enumerate(nums):
            # found next second greater element
            while nextGreater and nums[nextGreater[-1]] < num:
                res[nextGreater.pop()] = num
            
            tmp = []
            # found next greater element
            while stack and nums[stack[-1]] < num:
                tmp.append(stack.pop())
            while tmp:
                nextGreater.append(tmp.pop())
            
            stack.append(i)
        return res