# Intuition

一開始想法是先固定出所有"T"條件下的substring in word
然後再在剩下的空位上試著填入字母

ex. str2.size = 4
一但我們先將str1[i] = "T"的情況填入後, `O`代表已經確定的字母
那這樣剩下的空格需滿足: 填入`a-z`後前後substring不可以滿足"T"

```
[O, O, O, O, '', O, O, O]
   [O  O  O  *]
      [O  O  *  O]
         [O  *  O   O]
            [*  O   O  O]
```

i=0: T
i=1,2,3,4: F (不然的話該空格就會被填入字母以符合T)
從上面字符來看, `*`不可以**同時**是str2裡的`str2[j] for j in range(len(str2))`
不然就會使得"T"條件不滿足

那既然是同時, 代表`''`只可能是字典序最小的兩個字母`a`, `b`之一就夠了, 因為`''`不可能同時是`a`又同時是`b`
這樣就代表任一一定能滿足相連"T"條件的substring

### brute force - back tracking (TLE)
```py
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        word = ["*"] * (n+m-1)

        # fix "T" condition first
        for i, s in enumerate(str1):
            if s == 'T':
                for j in range(i, i+m):
                    word[j] = str2[j-i]
        
        self.res = ""
        def dfs(i, state):
            if i == n+m-1:
                for j in range(n):
                    if str1[j] == "T" and state[j:j+m] != str2: return False
                    if str1[j] == "F" and state[j:j+m] == str2: return False
                self.res = state
                return True

            if i-m+1 >= 0:
                if str1[i-m+1] == "T" and state[i-m+1:i+1] != str2: return False
                if str1[i-m+1] == "F" and state[i-m+1:i+1] == str2: return False

            if word[i] != "*":
                return dfs(i+1, state)
            pre, suf = state[:i], state[i+1:]
            if dfs(i+1, pre+"a"+suf): return True
            if dfs(i+1, pre+"b"+suf): return True

            return False
        dfs(0, "".join(word))
        return self.res
```

延續前面, 由於我們歸納出所有未定位置的字母不是`"a"`就是`"b"`
那我們就先全部填`"a"`, 並用`T[i]=False`標記該位置仍未真正確定後 (如下)

```py
n, m = len(str1), len(str2)
word = [""] * (n + m - 1)
T = [False] * (n + m - 1)

# 1. fill all the `T`s
for i in range(n):
    if str1[i] == "T":
        for j in range(m):
            if word[i + j] and word[i + j] != str2[j]:
                return ""
            word[i + j] = str2[j]
            T[i + j] = True

# 2. fill all the `F`s with 'a' first
for i in range(n + m - 1):
    if not word[i]:
        word[i] = "a"
```

接下來就在遍歷一遍檢查即可
遍歷過程, 一但str1[i] == "F", 代表該位置未定
這時我們先確認該位置word[i+j]是否已滿足**不等於**str2[j]
如果已滿足, 那就直接跳過, 繼續遍歷下去

但如果word[i+j] == str[j], 代表我們要變換word[i+j]

這時:
1. 如果T[i+j]標示為`False`, 那我們就把word[i+j]改成"b". (因為先前歸納不是"a"就是"b", 任一必定能符合)
2. 如果T[i+j]標示為`True`, 那代表沒有我們能操作的空間, 因此可直接返回False (無解)

```py
for i in range(n):
    if str1[i] == "F":
        # 3. check if aleady different
        diff = False
        for j in range(m):
            if word[i + j] != str2[j]:
                diff = True
                break
        if diff:
            continue

        # 4. find a char to change from the end to the begin
        change = False
        for j in range(m - 1, -1, -1):
            # if cur is `T`, it cannot be changed, continue
            if T[i + j]: continue
            
            if word[i+j] == "a":
                word[i + j] = "b"

            change = True
            break

        # once we can't change and still not satisfy `F` condition, directly return 
        if not change: return ""

return "".join(word)

```