# Intuition

首先想到的是我們可以用dynamic programming來找出這個極值
我們限定用兩個手指，每次在按的時候，只跟哪根手指以及這根手指的前一個位置有關
所以我們首先用`i`紀錄現在是第幾個字母, 然後再用另外兩個狀態分別紀錄當前兩個手指停止在哪個按鍵上

狀態轉移很顯然的就是:

```py
dp[i][finger1][finger2] = min(dp[i-1][prev_finger1][finger2] + dist(finger1, prev_finger1),
                              dp[i-1][finger1][prev_finger2] + dist(finger2, prev_finger2))
```

那對於當前第i個字母 word[i] 我們可以選擇用finger1按也可以用finger2按, 所以我們外層循環遍歷現在是第幾個字母
裡面兩層循環遍歷前一個手指的位置以及另外一個手指的位置

由於有兩個手指，所以我們用兩個內層循環來找最小值:
```py
for i in range(n):
    curr = ord(word[i]) - ord("A")
    for prev in range(26):
        for otherFinger in range(26):
            dp[i][curr][otherFinger] = min(dp[i][curr][otherFinger], (dp[i-1][prev][otherFinger] if i-1 >= 0 else 0)+ dist(prev, curr))
    for prev in range(26):
        for otherFinger in range(26):
            dp[i][otherFinger][curr] = min(dp[i][otherFinger][curr], (dp[i-1][otherFinger][prev] if i-1 >= 0 else 0) + dist(prev, curr))
```

但觀察一下可發現，其實內層循環可以合併
對於當前的按鍵來說，我們可以選擇用finger1 或 finger2
合併後為:

```py
for i in range(n):
    curr = ord(word[i]) - ord("A")
    for prev in range(26):
        for otherFinger in range(26):
            dp[i][curr][otherFinger] = min(dp[i][curr][otherFinger], (dp[i-1][prev][otherFinger] if i-1 >= 0 else 0)+ dist(prev, curr))
            dp[i][otherFinger][curr] = min(dp[i][otherFinger][curr], (dp[i-1][otherFinger][prev] if i-1 >= 0 else 0) + dist(prev, curr))
```

要注意的是i=0時沒有前一個狀態，所以前一個狀態的距離應為0:

```py
dp[i-1][prev][otherFinger] if i-1 >= 0 else 0
dp[i-1][otherFinger][prev] if i-1 >= 0 else 0
```

那最後就是我們的helper fn: `dist`
我們可以先把每個字母的位置建立起來, 那`dist`就單純查表然後位置相減取絕對值即可

```py
grid = dict()
for i in range(26): # A-Z -> 0-25
    grid[i] = (i//6, i%6)
```

# space optimization

因為dp[i]只依賴於dp[i-1]
我們可以用2個array來紀錄兩個手指的位置

```py
prevdp = [[0] * 26 for _ in range(26)]
dp = [[inf] * 26 for _ in range(26)]

for i in range(n):
    curr = ord(word[i]) - ord("A")            
    for prev in range(26):
        for otherFinger in range(26):
            dp[curr][otherFinger] = min(dp[curr][otherFinger], prevdp[prev][otherFinger]+ distance[prev][curr])
            dp[otherFinger][curr] = min(dp[otherFinger][curr], prevdp[otherFinger][prev] + distance[prev][curr])
    prevdp = dp
    dp = [[inf] * 26 for _ in range(26)]
return min(map(min, prevdp))
```


# Optimization

因為dp[i]只依賴於dp[i-1], 反過來說dp[i]能更新dp[i+1]
我們可以也能用2個集合來紀錄兩個手指的位置, 並且從當前位置轉移到下個位置
透過使用hashmap, 可以僅遍歷所有轉移的狀態，而非全部可能狀態遍歷一遍

前面的方式是當前的狀態可以從任何一種狀態轉移過來，至於前一個狀態是什麼並不知道，所以才全部搜索一遍取最小的
但這個作法是從當前的狀態轉移到下個狀態，因此其中一個狀態一定是word[i]

```py
class Solution:
    def minimumDistance(self, word: str) -> int:
        def dis(a, b):
            if a == 27: return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)
        
        prev = {(27, 27): 0}
        cur = {}

        for x in word:
            c = ord(x) - ord('A')
            for a, b in prev:
                cur[a, c] = min(cur.get((a, c), inf), prev[a, b] + dis(b, c))
                cur[c, b] = min(cur.get((c, b), inf), prev[a, b] + dis(a, c))
            prev, cur = cur, {}

        return min(prev.values())
```