# Rabin-Karp Algorithm (sliding hash)
# explanation: https://labuladong.github.io/algo/2/20/28/
# O(n)
class RabinKarpSolution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        nums = []
        for ch in s:
            match ch:
                case "A":
                    nums.append(0)
                case "G":
                    nums.append(1)
                case "C":
                    nums.append(2)
                case "T":
                    nums.append(3)
        
        # 10-letter-long
        L = 10
        
        # carry system
        R = 4
        
        windowHash = 0
        
        l, r = 0, 0
        seen = set()
        res = {}
        while r < len(nums):
            windowHash = windowHash * R + nums[r]
            r += 1
            
            if r-l == L:
                if windowHash in seen:
                    res[s[l:r]] = True
                else:
                    seen.add(windowHash)
                
                windowHash = windowHash - nums[l] * R ** (L-1)
                l += 1
        return res.keys()

# O(N*L), L = 10
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dna = defaultdict(lambda: 0)
        
        l, r = 0, 0
        while r < len(s):
            r+=1
            
            while r-l > 10:
                l+=1
            
            if r-l == 10:
                dna[s[l:r]] += 1
        return [s for s, cnt in dna.items() if cnt > 1]

class OptimizedSolution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dna = defaultdict(lambda: 0)
        
        res = {}
        l, r = 0, 0
        while r < len(s):
            r+=1
            
            if r-l == 10:
                candidate = s[l:r]
                dna[candidate] += 1
                if dna[candidate] > 1:
                    res[candidate] = True
                l+=1
        return res.keys()