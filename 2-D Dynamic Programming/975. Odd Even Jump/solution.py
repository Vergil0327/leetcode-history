from sortedcontainers import SortedList
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)

        l = SortedList()
        nextGreater = list(range(n))
        for i in range(n-1, -1, -1):
            j = l.bisect_left((arr[i], -inf))
            if j != len(l):
                nextGreater[i] = l[j][1]
            l.add((arr[i], i))

        l = SortedList()
        nextSmaller = list(range(n))
        for i in range(n-1, -1, -1):
            j = l.bisect_left((-arr[i], -inf))
            if j != len(l):
                nextSmaller[i] = l[j][1]
            l.add((-arr[i], i))
        
        @lru_cache(None)
        def dfs(i, isOddJump):
            if i == n-1: return True
            if i >= n: return False

            if isOddJump:
                oddIdx = nextGreater[i]
                if oddIdx != i and dfs(oddIdx, 1-isOddJump): return True

            if not isOddJump:
                evenIdx = nextSmaller[i]
                if evenIdx != i:
                    if dfs(evenIdx, 1-isOddJump): return True

            return False
        
        res = 0
        for i in range(n):
            if dfs(i, 1): res += 1
        return res

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        nextGreater, nextSmaller = list(range(n)), list(range(n))

        # 由小到大排列
        increasingArr = sorted([[v, i] for i, v in enumerate(arr)])
        stack = []
        for num, idx in increasingArr:
            while stack and stack[-1] < idx:
                nextGreater[stack.pop()] = idx
            stack.append(idx)

        # 數值由大到小排列，當stack[-1] < idx 代表找到下一個小的位置
        decreasingArr = sorted([[-v, i] for i, v in enumerate(arr)])
        stack.clear()
        for num, idx in decreasingArr:
            while stack and stack[-1] < idx:
                nextSmaller[stack.pop()] = idx
            stack.append(idx)

        @lru_cache(None)
        def dfs(i, isOddJump):
            if i == n-1: return True
            if i >= n: return False

            if isOddJump:
                oddIdx = nextGreater[i]
                if oddIdx != i and dfs(oddIdx, 1-isOddJump): return True

            if not isOddJump:
                evenIdx = nextSmaller[i]
                if evenIdx != i:
                    if dfs(evenIdx, 1-isOddJump): return True

            return False
        
        res = 0
        for i in range(n):
            if dfs(i, 1): res += 1
        return res