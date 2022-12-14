# https://www.youtube.com/watch?v=oOWb_CQU5xo
# 根據解析，這題並不適用二分搜尋法，數值不具備單調性
# we're just lucky to solve this by binary search

class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)

        # <BBB/BBB>, 3 + length*2 < limit
        for length in range(1, int(1e4)):
            if 3+length*2 >= limit: break
            
            parts = 10 ** length - 1 # try 9, 99, 999, ... to find upperbound of parts
            cost = (3+length)*parts # fixed cost, </length> * parts
            for i in range(1, length+1):
                # 1-9, 10-99, 100-999
                cost += i * ((10**i-1) - (10**(i-1)-1))
            
            if parts * limit - cost >= n:
                return self.get(message, limit, length)
        return [] # solution not found
    
    
    def get(self, message: str, limit: int, l: int):
        res = []
        wordCount = 0
        idx = 0
        while wordCount < len(message):
            idx += 1
            
            cost = 3+l+len(str(idx)) # <idx/>
            add = min(limit-cost, len(message)-wordCount)
            res.append(f"{message[wordCount:wordCount+add]}<{idx}/@>")
            wordCount += add
        
        res = [s.replace("@", str(idx)) for s in res]
        return res


# time: O(nlog(n))
class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)
        
        if limit < 5: return [] # <a/b>, we need 5 length at least
            
        res = []
        l, r = 1, n # try to split from 1 to n parts
        while l <= r:
            mid = l + (r-l)//2 # number of parts
            
            # check
            candidate = []
            idx = 0
            a = 1
            suffix = ""
            while a <= mid:
                suffix = f"<{a}/{mid}>"
                length = limit-len(suffix)
                candidate.append(f"{message[idx:idx+length]}{suffix}")
                idx += length
                a += 1

            # shrink search space
            if idx < n: # split not enough parts
                l = mid+1

            # ex. "ymm", 8; "short message", 15
            # since we check last two elements to move `r` pointer, we need to handle edge case of split len == 1
            elif len(candidate) == 1:
                if candidate[0][:-len(suffix)] != "":
                    return candidate
                else:
                    return []
            elif len(candidate[-2]) != limit or candidate[-1][:-len(suffix)] == "": # split too many parts
                r = mid-1
            else:
                res = candidate
                l+=1

        return res


# https://leetcode.com/problems/split-message-based-on-limit/discuss/2807533/Python-Find-the-number-of-substrings
# https://leetcode.com/problems/split-message-based-on-limit/discuss/2807759/Python-binary-search-is-redundant-just-brute-force-it-(explained)
"""
Analysis:
1. lower bound: if 3 + size(b)*2 >= limit, 3 means </> (3 digits)
    it means <b/b> already take up all the digits, we can't break message, this is lowerbound of breaking message
    ex.
        b=2,  <2/2>
        b=15, <15/15>

2. maximum digits: b * limit
    b * limit is total maximum digits because length of each resulting part should be equal to limit

3. not enough digits to break
    if b*(3+size(b)) + a + len(message) > b * limit

time: O(n)
space: O(n)
"""
class SolutionOptimized:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        def size(num):
            return len(str(num))
        
        # find valid parts to break
        # we can try b from 1 until we found valid b
        a, b = 1, 1
        while b * (3+size(b)) + a + len(message) > b * limit: # 第三點
            if 3+size(b)*2 >= limit:
                break
            b += 1
            a += size(b)
            
        res = []
        if 3+size(b)*2 >= limit: return res
        
        idx = 0
        for j in range(1, b+1):
            suffix = f"<{j}/{b}>"
            length = limit-len(suffix)
            part = message[idx:idx+length]
            res.append(f"{part}{suffix}")
            idx += length
        return res
