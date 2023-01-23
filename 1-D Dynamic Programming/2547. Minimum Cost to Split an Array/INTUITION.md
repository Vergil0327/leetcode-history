# Intuition

我們嘗試在每個位置split，把nums[i]加入到counter裡
然後持續遞歸

[X | XXX]
[XX | XX]
[XXX | X]
[XXXX| []]

```py
for j in range(i, n):
    counter[nums[j]] += 1
    trimmed = sum(cnt for cnt in counter.values() if cnt > 1)
    score = k + trimmed + dfs(j+1)
```

這樣會是個O(n^3)的解法，但實際上trimmed不用每次都重新加總計算一遍

我們可以維護一個`trimmed`變數
當`counter[nums[j]] = 2`時，此時有兩個duplicate nums[j]，因此trimmed += 2
而當`counter[nums[j]] > 2`後，每多一個nums[j]多一個duplicate，因此trimmed += 1

如此一來，上方核心程式碼可轉為，並將$O(n^3)$降為$O(n^2)$

```py
trimmed = 0
for j in range(i, n):
    counter[nums[j]] += 1
    if counter[nums[j]] == 2:
        trimmed += 2
    elif counter[nums[j]] > 2:
        trimmed += 1
    score = k + trimmed + dfs(j+1)
```

# Approach

define `dp[i]: the minimum possible cost of a split of nums[0:i]`

```
scores is an interval, therefore, it's interval-type DP
```

for every position `i`, we need to find a j where `0 <= j <= i` and its importance score is `scores[j:i]`

nums = [XXXXXXX [j XXXXXX i]]
               <-j
`dp[i] = dp[j-1] + scores[j:i]`

# Complexity

- time complexity
$$O(n^2)$$

- space complexity
$$O(n)$$