# 4-D DP (count1, count2, count3, count4)
# keep tracks of every valid subsequence
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