class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        m = 2*n-1

        arr = [-1] * m
        usedNum = set()

        def dfs(i):
            if i == m: return True
            if arr[i] > 0: return dfs(i+1)

            for num in range(n, 0, -1):
                if num in usedNum: continue
                if num > 1:
                    if i+num >= m or arr[i+num] > 0: continue

                arr[i] = num
                if num > 1:
                    arr[i+num] = num
                usedNum.add(num)
                if dfs(i+1): return True
                arr[i] = -1
                if num > 1:
                    arr[i+num] = -1
                usedNum.remove(num)
                
            return False
        dfs(0)
        return arr
