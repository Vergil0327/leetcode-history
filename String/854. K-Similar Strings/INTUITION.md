# Intuition

首先`1 <= s1, s2 <= 20`, 並且裡面只會有六種字母{'a', 'b', 'c', 'd', 'e', 'f'}

首先, 先想想暴力解法該怎辦, 我們就i-th letter逐個看:
1. s1[0] == s2[0]: 看下一位`i+1`
2. s1[0] != s2[0]: 搜索s1裡所有等於s2[0]然後swap看看, 取最小次數

```py
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        @cache
        def dfs(s1, s2):
            if not s1: return 0

            if s1[0] == s2[0]:
                return dfs(s1[1:], s2[1:])
            else:
                return min(dfs(s1[1:j]+s1[0]+s1[j+1:], s2[1:]) + 1 for j in range(1, len(s1)) if s1[j] == s2[0])

        return dfs(s1, s2)
```

由於python 的slicing效率很高, leetcode能直接過

同理也能用BFS求最短步數

```py
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        queue = deque([s1])
        visited = set([s1])
        step = 0
        while queue:
            for _ in range(len(queue)):
                s = queue.popleft()
                if s == s2: return step

                i=0
                while s[i] == s2[i]:
                    i += 1

                for j in range(i+1, len(s1)):
                    if s[j] != s2[i]: continue
                    swap = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                    
                    if swap in visited: continue
                    visited.add(swap)

                    queue.append(swap)
            step += 1
        return step
```
