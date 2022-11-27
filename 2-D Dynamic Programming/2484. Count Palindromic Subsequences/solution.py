# 4-D DP (count1, count2, count3, count4)
# keep tracks of every valid subsequence
# same idea: https://leetcode.com/problems/count-palindromic-subsequences/discuss/2850557/C%2B%2BorJavaorPython3-short-DP
class Solution:
    def countPalindromes(self, s: str) -> int:
        MOD = int(1e9+7)
    
        count1 = defaultdict(int) # len 1 subsequence
        count2 = defaultdict(int) # len 2 subsequence
        count3 = defaultdict(int) # len 3 subsequence
        count4 = defaultdict(int) # len 4 subsequence
        
        res = 0
        for ch in s:
            for subseq, cnt in count4.items():
                if ch == subseq[0]:
                    res += cnt
            for subseq, cnt in count3.items():
                if ch == subseq[1]:
                    count4[subseq+ch] += cnt
            for subseq, cnt in count2.items():
                count3[subseq+ch] += cnt
            for subseq, cnt in count1.items():
                count2[subseq+ch] += cnt
            count1[ch] += 1
        return res % MOD

# math: count = # (of left valid seq.) * (# of right valid sequence)
class Solution:
    def countPalindromes(self, s: str) -> int:
        MOD = int(1e9+7)
        n = len(s)
        
        prefix = [[[0] * 10 for _ in range(10)] for _ in range(n)]
        count = [0] * 10
        for i in range(n):
            ch = ord(s[i]) - ord("0")

            if i: # [X Y] _ Y X
                for x in range(10):
                    for y in range(10):
                        prefix[i][x][y] = prefix[i-1][x][y]
                        if y == ch:
                            prefix[i][x][y] += count[x]
            count[ch] += 1 # store how many ch in X position
            
        suffix = [[[0] * 10 for _ in range(10)] for _ in range(n)]
        count = [0] * 10
        for i in range(n-1, -1, -1):
            ch = ord(s[i]) - ord("0")
            
            if i < n-1: # X Y _ [Y X] 
                for x in range(10):
                    for y in range(10):
                        suffix[i][x][y] = suffix[i+1][x][y]
                        if y == ch:
                            suffix[i][x][y] += count[x]
            count[ch] += 1
            
        # iterate through each middle
        res = 0
        for mid in range(2, n-2):
            for x in range(10):
                for y in range(10):
                    res += prefix[mid-1][x][y] * suffix[mid+1][x][y]
                    res %= MOD
        return res % MOD