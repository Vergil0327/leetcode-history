# top-down

## Intuition

first count every stick's character and store in a list.
we use DFS to explore the minimum sticker we need to spell target

in each decision:

1. try stick with first character is needed to spell target's first character
2. explore if any rest of target's character can be spelled by current stick
3. recursive explore remain character subseq. of target
4. choose minimum used stickers

## Complexity

- time complexity

since there are $2^n$ possible subsequence of target string, it will be $2^n$ subproblem

we take O(n) to search in each subproblem

thus, time complexity should be $O(n*2^n)$

- space complexity

$$O(2^n)$$

# bottom-up

## Intuition

由於`target` string不長於15，因此我們可以用bitmask來表示我們目前已經用sticker處理了哪幾位character

將DP這樣定義: `dp[remain_state]: the minimum number of stickers for remain state`

ex. target = "target"
initially, remain_state = 111111 -> means current remain state = "target"
remain_state = 111000 -> means current remain state = "tar"

再來dp的狀態轉移可以有兩種方式:
1. 用過去已知的狀態來更新未來狀態，例如 dp[i] = dp[i-1] ...
2. 用現在狀態更新未來狀態，例如 dp[i] = dp[j] + 1 where i > j

這題如果用第一種的方式的話，會變成要找出`現在的state扣掉sticker後的狀態`，使得dp[i] = min(dp[i], dp[current_state-sticker]+1)
但過去的狀態並不好找，因為我們並無法判斷當前這位字符 `target[i]` 是不是由當前sticker提供

但next state相對好找，只要當前的狀態加上sticker即可推出當前sticker能轉換出的下個狀態，所以我們才採用第二種方式來更新DP

採取第一種方式會像這樣 (TLE) :

定義dp[i][state]: the minimum number of stickers for remain state by using first `i` stickers, stickers[0:i]

```py
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:        
        # dp[i][state]: the minimum number of stickers for remain state by using stickers[0:i]
        m = len(stickers)
        n = len(target)
        dp = [[inf] * (1<<n) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 0

        counters = [Counter(sticker) for sticker in stickers]
        counters = [{}] + counters # shift to 1-based index

        for i in range(1, m+1):
            for state in range(1, 1<<n):
                count = counters[i].copy()
                dp[i][state] = dp[i-1][state]

                submask = state
                for j in range(n):
                    if (submask>>j)&1 and count[target[j]] > 0:
                        count[target[j]] -= 1
                        submask ^= (1<<j)
                
                dp[i][state] = min(dp[i][state], dp[i][submask]+1)
                
        return dp[m][(1<<n)-1] if dp[m][(1<<n)-1] != inf else -1
```