# optimal solution: https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/discuss/2758216/JavaC%2B%2BPython-Straight-Forward-Solution

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        n0 = n
        
        mul = 0
        while sum(map(int, str(n))) > target:
            n = n//10 + 1 # 12457 -> 12460 (1+2+4+6) -> 12500 (1+2+5) -> 13000 (1+3) -> 20000 (2)
            mul += 1
        
        return n * (10 ** mul) - n0

class SolutionFirstTry:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        arr = list(map(int, list(str(n))))

        i = len(arr)-1
        
        deq = deque()
        while i >= 0 and sum(arr) > target:
            deq.appendleft(10-arr[i])
            arr[i] = 0
            i -= 1
            arr[i] += 1
            
        total = 0
        mul = 1
        while deq:
            total += deq.pop() * mul
            mul *= 10

        return total
            