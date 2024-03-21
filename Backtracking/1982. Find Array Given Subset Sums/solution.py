from sortedcontainers import SortedList
class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        sums.sort()
        self.res = []
        def dfs(sums, n):
            if n == 0: return True

            smallPos = sums[-1]-sums[-2]
            sl1 = SortedList(sums)
            if smallPos in sl1:
                nxt = []
                valid = True
                while sl1:
                    maxSum = sl1[-1]
                    if (v:=maxSum-smallPos) in sl1:
                        nxt.append(v)
                        sl1.remove(maxSum)
                        sl1.remove(v)
                    else:
                        valid = False
                        break
                if valid:
                    self.res.append(smallPos)
                    if dfs(list(sorted(nxt)), n-1): return True
                    self.res.pop()
            
            largeNeg = sums[-2]-sums[-1]
            sl2 = SortedList(sums)
            if largeNeg in sl2:
                nxt = []
                valid = True
                while sl2:
                    minSum = sl2[0]
                    if (v:=minSum-largeNeg) in sl2:
                        nxt.append(v)
                        sl2.remove(minSum)
                        sl2.remove(v)
                    else:
                        valid = False
                        break
                if valid:
                    self.res.append(largeNeg)
                    if dfs(list(sorted(nxt)), n-1): return True
                    self.res.pop()
            return False
            

        dfs(sums, n)
        return self.res