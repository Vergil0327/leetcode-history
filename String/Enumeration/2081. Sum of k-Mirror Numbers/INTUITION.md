# Intuition

**Brute Force**
```py
def kMirror(self, k: int, n: int) -> int:
    def ispal(s: str):
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]: return False
            l, r = l+1, r-1
        return True

    def isKmirror(num: int):
        s = ""
        while num:
            s = str(num%k) + s
            num //= k

        return ispal(s)

    num = 1
    res = cnt = 0
    while cnt < n:
        if ispal(str(num)) and isKmirror(num):
            res += num
            cnt += 1
        num += 1
    return res
```

再來想到的是我們由小到大產生palindrome, 這些數會遠小於遍歷每個自然數
然後在看他是不是k-mirror number, 但還是TLE
```py
from sortedcontainers import SortedList
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def kMirror(num: int):
            s = ""
            while num:
                s = str(num%k) + s
                num //= k

            l, r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]: return False
                l, r = l+1, r-1

            return True

        odd = SortedList(key=lambda x:int(x))
        even = SortedList(key=lambda x:int(x))
        for d in "0123456789":
            odd.add(d)
            even.add(d+d)

        res = cnt = 0
        while cnt < n:
            nxt = SortedList(key=lambda x:int(x))
            for s in odd:
                v = int(s)
                
                if s[0] != "0" and kMirror(v):
                    if cnt >= n: return res
                    res += v
                    cnt += 1

                for d in "0123456789":
                    nxt.add(d+s+d)
            odd = nxt

            nxt = SortedList(key=lambda x:int(x))
            for s in even:
                v = int(s)
                if s[0] != "0" and kMirror(v):
                    if cnt >= n: return res
                    res += v
                    cnt += 1

                for d in "0123456789":
                    nxt.add(d+s+d)
            even = nxt

        return res
```

使用SortedList他背後還會做排序, 效率還是太差
最終還是希望能不排序, 直接由小到大構造出1-based palindrome

如下,
AB => ABA, ABBA, ex. 13 => 131, 1331
ABC => ABCBA, ABCCBA, ex. 123 => 12321, 123321

對於任意自然數, 我們把它翻轉並組合, 以及翻轉去除後一位再組和, 各能得到2*length-1以及2*length的palindrome
所以我們可以遍歷自然數來組出所有合法palindrome

所以首先從長度為1的自然數開始, 那麼我們遍歷的值域範圍就是[10^0,10^1]
所以一個長度為**length**的自然數, 遍歷範圍就是**[pow(10, length-1), pow(10, length)]**
再來就產生odd-length palindrome以及even-length palindrome並判斷是不是k-mirror即可

```py
length = 1
res = cnt = 0
while cnt < n:
    start = pow(10, length-1)
    end = pow(10, length)
    for num in range(start, end):
        val = genOddPalindrome(num)
        if kMirror(val):
            cnt += 1
            res += val
            if cnt == n: return res

    for num in range(start, end):
        val = genEvenPalindrome(num)
        if kMirror(val):
            cnt += 1
            res += val
            if cnt == n: return res
    length += 1
```

# Other Solution

Elegant solution from [@ye15](https://leetcode.com/problems/sum-of-k-mirror-numbers/solutions/1589048/python3-enumerate-k-symmetric-numbers/)

```py
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        
        def fn(x):
            """Return next k-symmetric number."""
            n = len(x)//2
            for i in range(n, len(x)): 
                if int(x[i])+1 < k: 
                    x[i] = x[~i] = str(int(x[i])+1)
                    for ii in range(n, i): x[ii] = x[~ii] = '0'
                    return x
            return ["1"] + ["0"]*(len(x)-1) + ["1"]
                
        x = ["0"]
        ans = 0
        for _ in range(n): 
            while True: 
                x = fn(x)
                val = int("".join(x), k)
                if str(val)[::-1] == str(val): break
            ans += val
        return ans 
```
