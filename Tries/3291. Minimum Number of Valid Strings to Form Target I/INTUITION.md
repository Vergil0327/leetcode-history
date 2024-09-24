# Intuition

首先想到的是top-down dp, 用dfs遍歷可能的prefix of target去檢查看看words有沒有相對應的prefix

大體框架為:

```py

def dfs(i):
    if i >= len(target): return 0

    res = inf
    root = tri
    for j in range(i, len(target)):
        for word in words:
            if target[i:j+1] == word[:j-i+1]:
                res = min(res, dfs(j+1, tri)+1)

    return res

res = dfs(0)
return res if res < inf else -1
```

但每次都遍歷words肯定是會TLE的, 所以這邊我們可以用Trie來檢查prefix of word
我們就逐步檢查prefix of target是否存在於Trie里

```py
@cache
def dfs(i, tri):
    if i >= len(target): return 0

    res = inf
    root = tri
    for j in range(i, len(target)):
        if target[j] in root.next:
            root = root.next[target[j]]
            res = min(res, dfs(j+1, tri)+1)
        else:
            break

    return res

res = dfs(0, tri.root)
return res if res < inf else -1
```

## Trie Implementation

Trie有兩種建構方式:
1. defaultdict

```py
Trie = lambda: defaultdict(Trie)
IS_END = "ISEND"
```

2. class

```py
class TrieNode:
    def __init__(self):
            self.next = {}
            self.isEnd = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word) -> None:
        root = self.root
        for i in range(len(word)):
            if word[i] not in root.next:
                root.next[word[i]] = TrieNode()
            root = root.next[word[i]]
        root.isEnd = True
```

由於第一種方式無法配合top-down dp進行memorize, 所以我們選用第二種方式


# Other Approach

dp[i]: the minimum number of valid strings that can be concatenated to form target[:i]

```py
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)

        dp = [inf] * (n + 1)
        dp[0] = 0

        def exist(w):
            for word in words:
                if word.startswith(w):
                    return True
            return False

        l = 0
        for r in range(1, n + 1):
            while l < r and not exist(target[l:r]):
                l += 1

            if l == r: return -1

            dp[r] = dp[l] + 1
        
        return dp[n]
```