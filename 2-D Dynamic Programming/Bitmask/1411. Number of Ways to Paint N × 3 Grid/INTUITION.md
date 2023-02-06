# Intuition

很明顯的是這一行能塗的顏色選擇僅取決於上一行，那3個column每個有3種顏色選擇
所以可以很快想到的是 dp[i][color1][color2][color3] += dp[i-1][color1'][color2'][color3']
那這樣大致上會是三層循環:

```
遍歷 ROWS:
    遍歷當前這行的所有選擇:3x3:
        遍歷前一行的所有選擇:3x3:
時間複雜度會是 n * 3^3 * 3^3, n <= 5000，算是可接受的範圍，因此我們可以繼續下去
```

**DP Definition**

`dp[i][color1][color2][color3]: 使用前 `i` 行必且當前color選擇為 color1, color2, color3`

那狀態轉移則為:

`dp[i][color1][color2][color3] += dp[i-1][color1'][color2'][color3']`

那最後答案就是所有可能的解的總和

另外，由於第一行並不依賴任何東西，不用判斷有沒有跟上行的顏色有衝突，因此我們單獨處理
```py
for i in range(3):
    for j in range(3):
        for k in range(3):
            if valid(i, j, k):
                dp[0][i][j][k] = 1
```

另外這題也可以用bitmask的概念，將3*3總顏色狀態壓縮到range(0, 27)

這樣`valid` helper fn，可寫成
```py
def valid(state): # state: [0,27]
    bit3 = []
    for i in range(3):
        bit3.append(state%3)
        state //= 3
    return bit3[0] != bit3[1] and bit3[1] != bit3[2]
```