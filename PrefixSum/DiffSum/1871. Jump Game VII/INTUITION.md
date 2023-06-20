# Diff Array

## Intuition

首先可以很容易想到Brute Force解法為:

```python
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True

        for i in range(1, n):
            for j in range(minJump, maxJump+1):
                if s[i] == "0" and i-j >= 0:
                    dp[i] = dp[i] or dp[i-j]
        return dp[n-1]
```

複雜度為`O(N*(maxJump-minJump+1))`

因此我們可以看到我們效率最低的地方其實是反覆地以線性方式去標記可抵達的區間
這時我們可以思考一下，在區間上有沒有什麼方式是可以用`O(1)`方式來標記的?

前綴和, 後綴和, 差分...這時我們可以試著想到`差分數組`或許是個不錯的選擇
我們在每個`"0"`的位置可以抵達的區間為`[i+minJump, i+maxJump]`，
- 因此我們可以透過在差分數組上的 `i+minJump` 位置標記 `+=1`, 來代表區間開始
- 在差分數組上的 `i+maxJump+1` 位置標記 `-=1`, 來代表區間結束
- 即使我們標記的區間有重疊也沒差，因為我們只關係能不能抵達，只要差分數組上的位置最後的和是`>0`的，就代表可以從某個位置抵達該位置

因此我們用一個變數`canReach`從0開始記錄變化,

1. canReach += diff後等於0，代表抵達不了該位置
2. canReach += diff後>0，代表可以抵達
3. 別忘記最初的base case，不然差分數組上都會為`0`

這樣當我們走到最後的`n-1`位置後，觀察`canReach`是否大於0即可得到答案

## Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(n)$$