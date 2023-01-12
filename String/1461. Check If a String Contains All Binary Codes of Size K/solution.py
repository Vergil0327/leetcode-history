class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = set()
        n = len(s)
        for i in range(0, n-k+1):
            codes.add(s[i:i+k])
        return len(codes) == (2**k)

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = set()
        
        total = 1<<k # = 2**k
        allOneMask = total-1
        bitmask = 0
        for i in range(len(s)):
          bitmask = ((bitmask << 1) | int(s[i])) & allOneMask
          if i >= k-1:
              codes.add(bitmask)
        return len(codes) == total