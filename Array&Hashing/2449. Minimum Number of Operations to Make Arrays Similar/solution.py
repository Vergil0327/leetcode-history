# https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/discuss/2734189/C%2B%2BPython-Sort-odds-and-evens
class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        curr = set(nums)
        if len(curr) == 1 and nums[0] == target[0]:
            return 0
        
        numsOdd = []
        numsEven = []
        targetOdd = []
        targetEven = []
        for num, tgt in zip(sorted(nums), sorted(target)):
            if num&1:
                numsOdd.append(num)
            else:
                numsEven.append(num)
            if tgt&1:
                targetOdd.append(tgt)
            else:
                targetEven.append(tgt)
                
        # since guarentee answer always exists
        # total ops // 2 should be answer
        ops = 0

        # or ops += sum(abs(num1-num2)//2 for num1, num2 in zip(numsOdd, targetOdd))
        for num1, num2 in zip(numsOdd, targetOdd):
            ops += abs(num1-num2)//2
        
        # or ops += sum(abs(num1-num2)//2 for num1, num2 in zip(numsEven, targetEven))
        for num1, num2 in zip(numsEven, targetEven):
            ops += abs(num1-num2)//2

        return ops // 2

class ConciseSolution:
  def makeSimilar(self, N: List[int], T: List[int]) -> int:
        N.sort(key=lambda x: [x % 2, x]) # even comes first than odd, then sort by second comparator
        T.sort(key=lambda x: [x % 2, x])
        
        # return sum(abs(n - t)//2 for n, t in zip(N, T)) // 2
        return sum(abs(n - t) for n, t in zip(N, T)) // 4
