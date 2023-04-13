# Intuition - bottom-up dp solution

s = X X X X X X X X X X X [X X X X X X]
                           j         i, i-j+1 >= k

首先我們能很直覺想到的是
假如s[j:i]是個valid palindrome, 那他就能接在s[:j-1]後面

所以我們定義dp[i]: the maximum number of palindrome whose length is k at least considering s[:i]

那我們就需要兩層循環，外層遍歷i、內層遍歷j
更新dp即可

```py
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        @lru_cache(None)
        def isPal(l, r):
            while l < r:
                if s[l] != s[r]: return False
                l, r = l+1, r-1
            return True

        dp = [0] * n
        for i in range(n):
            for j in range(i, -1, -1):
                dp[i] = max(dp[i], (dp[j-1] if j-1 >= 0 else 0) + (1 if isPal(j, i) and i-j+1 >= k else 0))

        return dp[n-1]
```

但實際上這會是個O(n^3)的解法
所以我們在判斷是不是palindrome這邊，我們可以把雙指針的判斷改掉
用一個O(n^2)的時間複雜度，預處理s[i:j]是不是palindrome

```py
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        ispal = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, -1, -1):
                if s[i] == s[j]:
                    if i-j+1 <= 3 or ispal[j+1][i-1]:
                        ispal[j][i] = True

        dp = [0] * n
        for i in range(n):
            for j in range(i, -1, -1):
                dp[i] = max(dp[i], (dp[j-1] if j-1 >= 0 else 0) + (1 if ispal[j][i] and i-j+1 >= k else 0))

        return dp[n-1]
```

實際上O(n^2 + n^2)還能再進一步優化成(n^2 + n)
觀察可發現內層在遍歷j更新dp時, dp[i]的更新其實是一段前綴和(prefix sum)
只要s[j:]是長度至少為k的palindrome, dp[0], dp[1], ..., dp[j-k-1], dp[j-k]都能更新dp[i]

由於palindrome可以是even-length或odd-length
所以我們就看presum_dp[i-k]跟presum[i-k+1]即可

- presum_dp[i] = max(presum_dp[i], (presum_dp[i-k] if i-k>=0 else 0)+1)
- presum_dp[i] = max(presum_dp[i], (presum_dp[i-k-1] if i-k-1>=0 else 0)+1)

```py
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        ispal = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, -1, -1):
                if s[i] == s[j]:
                    if i-j+1 <= 3 or ispal[j+1][i-1]:
                        ispal[j][i] = True
                        
        presum_dp = [0] * n
        for i in range(k-1, n):
            if i > 0:
                presum_dp[i] = presum_dp[i-1] # prefix sum
            
            # even-length palindrome or odd-length palindrome
            if i-k+1 >= 0 and ispal[i-k+1][i]:
                presum_dp[i] = max(presum_dp[i], (presum_dp[i-k] if i-k>=0 else 0)+1)
            if i-k >= 0 and ispal[i-k][i]:
                presum_dp[i] = max(presum_dp[i], (presum_dp[i-k-1] if i-k-1>=0 else 0)+1)

        return presum_dp[n-1]
```