# Intuition

最簡單的brute force就是由大到小檢查所有長度的substring => O(n^3)

更好一些的brute force solution是從前個合法prefix去持續建構可能substring, 並查看是不是valid substring, 但這至少也是O(26*n^2)解法

兩種想法皆會TLE

```py
def preprocess(s):
    n = len(s)
    lps = [0]*n

    for i in range(1, n):
        j = lps[i-1]
        while j >= 1 and s[i]!=s[j]:
            j = lps[j-1]
        lps[i] = j + int(s[i] == s[j])
    return lps

def kmp_search(target, s):
    n = len(s)
    lps = preprocess(target)

    j = repeated = 0
    for i in range(n):
        while j > 0 and s[i] != target[j]:
            j = lps[j-1]

        j = j+(s[i] == target[j])
        if j == len(target):
            j = lps[j-1]
            repeated += 1
    return repeated

class Solution: # O(n^3)
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        res = ""

        for length in range(n-1, 0, -1):
            for i in range(n-length+1):
                j = i+length
                target = s[i:j]
                repeated = kmp_search(target, s)
                if repeated > 1:
                    return target
        return ""

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        res = ""
        prefix = {""}
        while len(prefix) > 0:
            nxtPrefix = set()
            for pre in prefix:
                for i in range(26):
                    ch = chr(ord("a")+i)

                    # KMP
                    target = pre+ch
                    repeated = kmp_search(target, s)

                    if repeated > 1:
                        nxtPrefix.add(target)
                        if len(target) > len(res):
                            res = target
            prefix = nxtPrefix

        return res
```

目前看來能優化的, 從O(n^3) brute force來看, 首先是從substring長度這點來下手

能線性搜索的東西, 我們試著看看能不能用binary search
假設當前搜索substring長度為`mid`:
- 如果`mid`沒有合法解, 那`mid+1`當然也不會有合法解
- 如果`mid`有合法解, 那肯定也存在`mid-1`長度的合法substring
既然符合單調性質, 代表binary search substring長度是可行的
因此我們試著加入binary search + kmp search試試

```py
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        res = ""

        l, r = 0, n
        while l < r:
            mid = r - (r-l)//2
            found = False
            for i in range(n-mid+1):
                j = i+mid
                target = s[i:j]
                repeated = kmp_search(target, s)
                if repeated > 1 and mid > len(res):
                    found = True
                    res = target
            if found:
                l = mid
            else:
                r = mid-1
            
        return res
```

會發現遍歷長度 + kmp搜索這個O(n^2)實在太慢
這邊要檢查相同長度下, 有沒有重複substring => 首先想到的是固定長度的滑窗
而檢查substring則可以用string rolling hashing (Rabin-Karp 's algorithm)來快速查找

因此kmp search那部分我們應當改成rolling hash來達到O(n), 這樣整體時間複雜度就降為O(nlogn)
框架如下:

這邊要多試幾次的就是base 跟 mod兩個數值
為了避免hash collision, 必須多試幾次數值

一開始嘗試: base=26, mod=10**9+7 發現不行
後續試錯了幾次才找到base=31, mod=10**11+7可通過test cases

```py
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        len2start = {}

        n = len(s)
        base = 31
        mod = 10**11 + 7
        nums = [ord(ch)-ord("a") for ch in s]
        
        # RABIN-KARP, Rolling Hash
        # sliding window, [i-len+1, i]
        def check_rolling_hash(s: str, length: int) -> bool:
            
            visited = set()
            rolling_hash = 0
            pow_base_len = pow(base, length, mod)
            for i in range(n):
                rolling_hash = rolling_hash*base + nums[i]
                if i >= length:
                    rolling_hash -= pow_base_len*nums[i-length]
                rolling_hash = (rolling_hash+mod) % mod
                
                if i-length+1 >= 0:
                    if rolling_hash in visited:
                        len2start[length] = i-length+1
                        return True
                    visited.add(rolling_hash)
            return False
        
        # binary search length of duplicate substring
        l, r = 0, n-1
        while l < r:
            mid = r - (r-l)//2
            if check_rolling_hash(s, mid):
                l = mid
            else:
                r = mid-1
        
        return s[len2start[l]:len2start[l]+l] if l > 0 else ""
```