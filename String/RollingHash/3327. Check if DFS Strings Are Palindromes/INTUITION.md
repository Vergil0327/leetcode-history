# Intuition

brute force很直覺, 但會TLE:

```py
class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)

        graph = defaultdict(list)
        for child, p in enumerate(parent):
            if p > -1:
                graph[p].append(child)
        
        ans = [True] * n
        def dfs(i):
            res = ""
            for nxt in graph[i]:
                res += dfs(nxt)
            res += s[i]
            ans[i] = res == res[::-1]
            return res
        dfs(0)
        return ans
```

## Key Idea:

Using hashing to check whether a DFS traversal of each subtree is a palindrome or not. Instead of constructing strings and comparing them (which is expensive in terms of time complexity), we compute hashes for both the forward and reverse traversals of each subtree. By comparing these hashes, we can determine if the subtree's DFS string is a palindrome.

see example 1:
Input: parent = [-1,0,0,1,1,2], s = "aababa"

```
    "a"
"aba"  "ab"
```

如果要判斷是否為palindrome, 代表`dfsStr[i] == reversed(dfsStr[i])`
所以我們可以順序跟逆序各進行一次dfsStr的操作:

forwardDfsStr[i] = "aba" + "ab" + "a"
reverseDfsStr[i] = "a" + "ba" + "aba"

那這樣後續answer[i]就只需要O(n)遍歷判斷`fordward[i] == reverse[i]`即可:

`answer = [forward[i] == reverse[i] for i in range(n)]`

但這樣進行字串比對的話, 最終還是O(n^2)
所以我們必須對str進行hash, 也就是在dfs過程中對`forwardDfsStr`跟`reverseDfsStr`進行rolling hash
然後再進行比對

```py
forwardHash = [0] * n
reverseHash = [0] * n
length = [0] * n

def dfs(i):
    length[i] = 1
    forwardHash[i] = 0

    cur = ord(s[i]) - ord("a") + 1 # hash characters into range [1,27]
    for nxt in graph[i]:
        dfs(nxt)
        forwardHash[i] = (forwardHash[i] * pow(base, length[nxt], mod) + forwardHash[nxt]) % mod
        length[i] += length[nxt]
    forwardHash[i] = (forwardHash[i]*base + cur) % mod

    reverseHash[i] = cur
    for j in range(len(graph[i])-1, -1, -1):
        nxt = graph[i][j]
        reverseHash[i] = (reverseHash[i] * pow(base, length[nxt], mod) + reverseHash[nxt]) % mod

# tree rooted at node 0
dfs(0)

return [forwardHash[i] == reverseHash[i] for i in range(n)]
```

如果要進一步優化的話, 我們可以預處理`pow(base, length[nxt], mod)`的部分, 改成`power[length[nxt]]`

```py
power = [1] * (n+1)
for i in range(1, n+1):
    power[i] = (power[i-1] * base) % mod
```

# Complexity

time:O(n)

Time Complexity:
DFS Time: Each node is visited exactly once in a single DFS traversal, and at each node, we process all its children. Thus, the time complexity of the DFS is 
𝑂(𝑛), where 𝑛 is the number of nodes in the tree.

Hashing Time: Each hash calculation (forward and reverse) takes constant time due to the precomputed powers of the base.
Therefore, the overall time complexity is 𝑂(𝑛), which is optimal for this problem.

space:O(n)