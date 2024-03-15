from itertools import combinations, permutations
from collections import Counter

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        count = Counter(s)
        subseq = "".join(ch*(freq//k) for ch, freq in count.items() if freq >= k)

        possible = set()
        for size in range(len(subseq)+1):
            for candidate in combinations(subseq, size):
                for ss in permutations(candidate):
                    possible.add("".join(ss))

        def greedy_find(t):
            if not t: return 0
            cnt = j = 0
            for ch in s:
                if ch == t[j]:
                    j += 1
                if j == len(t):
                    cnt += 1
                    j = 0
            return cnt

        for ss in sorted(possible, key=lambda x:(len(x), x), reverse=True):
            cnt = greedy_find(ss)
            if cnt >= k:
                return ss
        return ""
        
