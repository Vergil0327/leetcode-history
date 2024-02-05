# Intuition

abacaba
aba | caba + bac
cab | abac + aba
abacaba

for i in range(k, n, k):
    word[i:] + ANY_SUFFIX

t=1, prefix = word[k:]
t=2, prefix = word[k*2:]
at time = t, prefix = word[k*t:]
一但prefix == word[:len(prefix)], 我們就能停止
如果一直都沒找到, 由於suffix可以任意組成, 最終也肯定能組成一開始的word
那這樣會是個O(n^2)

所以重點在於我們能不能快速在word裡找到一段word[k*t:] == word[:n-k*t]
=> 也就是找到一段prefix == suffix 且長度為k的倍數

那這樣肯定得先對word進行預處理, 好讓我們能在O(1)時間確認`word[k*t:] == word[:n-k*t]`

Z-function for a string returns an array z of the same size.
z[i] tells us how many characters, starting from the position i, match with the first characters of the string.

那這樣我們只要確認從position `k*t`開始`z[k*t]`有沒有至少`n-k*t`個letters即可, 有的話代表suffix word[k*t:]與prefix word[:n-k*t]相等

# Intuition2 KMP

我們要找的, 其實就是能被k整除的longest prefix suffix
而這其實就是KMP的預處理

[leetcode 1392 longest happy prefix](../1392.%20Longest%20Happy%20Prefix/solution2.py)

```py
def longestPrefixSuffix(s: str) -> str:
    n = len(s)
    
    # KMP preprocess
    # dp[i]: longest common prefix-suffix length of s[0:i)
    dp = [0]*n
    # dp[0] = 0

    for i in range(1, n):
        j = dp[i-1]
        while j >= 1 and s[j] != s[i]:
            j = dp[j-1]
        dp[i] = j + int(s[i] == s[j])
    
    length = dp[n-1]
    return s[:length]

kmp = longestPrefixSuffix(word)
length = kmp[n-1]

# 持續從最長prefix-suffix開始找, 找出可以被k整除的長度
while length > 0 and (n-length)%k != 0:
    length = kmp[length-1]

# 如果length==0, 代表與prefix相等的suffix的長度為0, 就是要全部切分完才行
# 如果能被k整除, 就需要切n//k刀
# 如果不能被k整除, 就需要切n//k + 1刀才能回到initial word
if length == 0:
    return n//k if n%k == 0 else n//k + 1
else:
    # 如果longet prefix-suffix長度為length
    # 那麼代表前面切分的長度為(n-length)
    # (n-length)//k 就知道我們需要切幾刀才能回到intial word
    return (n-length)//k
```