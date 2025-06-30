# Intuition

對於words[i]來說, 我們要求出words[:i]跟words[i+1:]的LCP of each adjacent pair, 以及words[i-1], words[i+1]這對pair的LCP

*note. LCP = Longest Common Prefix*

所以很簡單
1. 我們先預處理前半段(prefix)到words[:i]為止的每個位置的max adjacent lcp length
   - 定義prefixLCP[i]: the longest common prefix lcp length of each adjacent pair within words[:i]
2. 以及後半段(suffix)到words[i+1:]為止的每個位置的max adjacent lcp length
   - 定義suffixLCP[i]: the longest common suffix lcp length of each adjacent pair within words[i+1:]

然後在遍歷一遍去比較prefixLCP[i-1], suffixLCP[i+1]以及(words[i-1], words[i+1]) pair的longest common prefix length, 求出三者最大值即為答案answer[i]

主框架:

```py
res = [0] * n
if n == 1: return res

res[0] = suffixLCP[1]
res[n-1] = prefixLCP[-2]

for i in range(1, n-1):
    res[i] = max(findLCP(words[i-1], words[i+1]), prefixLCP[i-1], suffixLCP[i+1])
return res
```

而求`prefixLCP`, `suffixLCP`前, 我們先求每個相鄰pair的LCP length:

```py
def findLCP(s, t):
    lcp = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            lcp += 1
        else:
            break
    return lcp

adjacentLcp = [] # List to store LCP between adjacent words
for i in range(1, n):
    adjacentLcp.append(findLCP(words[i-1], words[i]))
```

然後再分別求出**longest prefix**及**longest suffix**

```py

prefixLCP = [0] # longest common prefix of adjacent words
for i in range(len(adjacentLcp)):
    prefixLCP.append(max(prefixLCP[-1], adjacentLcp[i]))

suffixLCP = [0] * (len(adjacentLcp)+1) # longest common prefix of adjacent words
for i in range(len(adjacentLcp)-1, -1, -1):
    suffixLCP[i] = max(suffixLCP[i+1], adjacentLcp[i])
```