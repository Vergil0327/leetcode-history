# Intuition

總共`n-1`輪，每一輪都可以是0-9這幾個位置
由於騎士只能走`L`形，所以我們可以把每個位置可以從哪幾個位置跳過來先列出來

```py
adjacencyList = {
    0: [4, 6],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [0, 3, 9],
    5: [],
    6: [0, 1, 7],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4],
}
```

再來就簡單了，每一輪都可以是0-9的位置，都可以從前一輪狀態的方法數轉移過來

所以我們可以定義dp[i][j]: the number of distinct phone numbers of length `i` we can dial when we ended at phone pad `j` where `j` from 0 to 9.

**base case**

0-9每個按鍵位置都是合法的，所以0次jump時的 number of distinct phone numbers是1

```py
dp = [[0] * 10 for _ in range(n)]

for num in range(10): # phonepad: 0-9
    dp[0][num] = 1
```

狀態轉移也像前面所述，每個狀態都從前個狀態的方法數轉移過來

dp用1-indexed, 然後外層循環從`1` jumps遍歷到總共 `n-1` jumps
每個phone pad number position都可以透過adjacencyList知道他們的前一個狀態的方法數
把他們全加起來就是當前這個按鍵的方法數

```py
for i in range(1, n): # n-1 jumps
    for num in range(10):
        for prev in adjacencyList[num]:
            dp[i][num] += dp[i-1][prev]
```