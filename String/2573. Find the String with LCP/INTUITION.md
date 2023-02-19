# Intuition

if lcp[i][j] > 0, it means words[i:i+lcp[i][j]] == words[j:j+lcp[i][j]]
thus, we can know that words[i] == words[j] if lcp[i][j] > 0

since we want alphabetically smallest string, we can iterate i from `0 to n-1` and assign from `a to z` one by one **if lcp[i][j] > 0**

if we already assigned character before, we skip it because it's already possible alphabetically smallest character

after we construct possible solution to alphabetically smallest string, we still need to check if lcp matrix is valid or not.

the conditions are the same as we construct string:

1. if `i+lcp[i][j] > n` or `j+lcp[i][j]`, it's **invalid**. (see example 3)
2. if **words[i] == words[j]**:
    - lcp[i][j] should be greater than 0
    - lcp[i][j] should equals lcp[i+1][j+1]+1
3. if **words[i] != words[j]**:
    - it's opposite from second condition
    - lcp[i][j] should be 0
    - lcp[i][j] should **NOT** equal lcp[i+1][j+1]+1
4. length of final words we constructed should equal `n`

    ```py
    ans = "".join(words)
    if len(ans) != n: return ""
    ```

# Complexity
- Time complexity:
$$O(n^2)$$

- Space complexity:
$$O(n)$$

# Code
```py
class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        # lcp[i][j]: length of common prefix word[i:] and word[j]
        n = len(lcp)
        words = [""]*n
        shift = 0
        for i in range(n):
            if words[i]: continue
            for j in range(n):
                if words[j]: continue
                # words[i:i+lcp[i][j]] == words[j:j+lcp[i][j]]
                # -> words[i] == words[j]
                if lcp[i][j] > 0:
                    words[i] = chr(ord('a')+shift) if shift < 26 else ""
                    words[j] = words[i]
            shift += 1

        for i in range(n):
            for j in range(n):
                # example 3
                if i+lcp[i][j] > n or j+lcp[i][j] > n: return ""
                
                if words[i] == words[j]:
                    # case: [[2,1],[0,1]]
                    if lcp[i][j] == 0: return ""
                    # case: [[4,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
                    if i<n-1 and j<n-1 and lcp[i][j] != lcp[i+1][j+1]+1:
                        return ""
                else:
                    if lcp[i][j] != 0: return ""
                    if i<n-1 and j<n-1 and lcp[i][j] == lcp[i+1][j+1]+1:
                        return ""
        
        # last test case
        ans = "".join(words)
        if len(ans) != n: return ""
        return ans
```

```
# last test case:
# [[27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,23,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,21,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,19,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,18,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,14,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,13,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,12,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]
# expected: ""
```