# Intuition

最初的想法是，首先我們可以對digits排序，一定是由左往右由大到小挑選，才能組出3的倍數的最大string

再來有個數學特性是，如果該數是3的倍數，其每個位數的加總，最後必定能被3整除
那麼這問題就能聯想到[1262. Greatest Sum Divisible by Three](../1262.%20Greatest%20Sum%20Divisible%20by%20Three/)這題了

我們這麼定義dp: dp[i][j] is the maximum string value where mod 3 is `j` considering digits[:i]

所以如果 `digits = [X X X X X X X digits[i]]`

對於digits[i]來說，如果 mod = digits[i]%3

1. 如果我們選digits[i]
如果mod = 0
如果j = 0, 那我們可以將digits[i]接在dp[i-1][0]後面，這樣就會組成%3餘0的最大string value
如果j = 1, 那我們可以將digits[i]接在dp[i-1][1]後面，這樣就會組成%3餘1的最大string value
如果j = 2, 那我們可以將digits[i]接在dp[i-1][2]後面，這樣就會組成%3餘2的最大string value

如果mod = 1
如果j = 0, 那我們可以將digits[i]接在dp[i-1][2]後面
如果j = 1, 那我們可以將digits[i]接在dp[i-1][0]後面
如果j = 2, 那我們可以將digits[i]接在dp[i-1][1]後面

同理mod = 2也是一樣

所以對於`j`從0到2來說，可以整理成

```py
mod = digits[i] % 3
for j in range(3):
    dp[i][j] = dp[i-1][(j-mod+3)%3] + str(digits[i])
```

2. 如果我們不選digits[i], 那麼`dp[i][j] = dp[i-1][j]`

所以我們兩種決策選較好的一個 dp[i][j] = better(dp[i-1][j], dp[i-1][(j-mod+3)%3] + str(digits[i]))

那我們該如何選較好的一個?

如果string長度越長，代表數值越大，所以選他
如果長度一樣，我們在看哪個數值較大，選他

```py
def better(s1, s2):
    if len(s1) > len(s2):
        return True
    elif len(s1) < len(s2):
        return False
    else:
        return float(s1)>float(s2)
```

那base case就要特別注意了，只有狀態合法的時候才能把digits[i]接在後面
所以我們初始值可以設成`"inf"`，此時`dp[0][0] = ""` (0個數字拼出餘數為0的合法string為"")
但dp[0][1], dp[0][2]都得是 `"inf"`，因為兩個都是不合法的string，不可以把digits[i]接在後面

所以在狀態轉移方面，我們還得考慮dp[i][j]的轉移是不是從合法的狀態轉移過來的
只要s1和s2都是`"inf"`那就跳過
如果有任一為`"inf"`, 那就選另外一個合法的狀態
如果兩個都不是`"inf"`, 那我們再用`better` helper function的邏輯去選較佳的一個

```py
for i in range(1, n+1):
    mod = digits[i] % 3
    for j in range(3):
        dp[i][j] = dp[i-1][j] # not choose ditis[i]
        if dp[i-1][(j-mod+3)%3] == "inf": continue

        if better(dp[i-1][(j-mod+3)%3] + str(digits[i]), dp[i-1][j]):
            dp[i][j] = dp[i-1][(j-mod+3)%3] + str(digits[i])
```

那最後答案就是dp[n][0], 考慮n個數然後對3取餘數為0的最大string value

但要注意不可以有leading zeros，所以我們記得在對string value處理一下
最後返回
```py
i = 0
while i < len(dp[n][0])-1 and dp[n][0][i] == "0":
    i += 1
return dp[n][0][i:]
```

# Optimized

上面的方法會重複儲存很多相同string
例如dp[i][j] = "XXXXX", dp[i+1][j]可能為"XXXXXY"
前面的`XXXXX`都是重複的元素

所以其實我們可以用`1262.`的概念定義dp:
dp[i][j] is the maximum length of possible value where mod 3 is `j` considering digits[:i]

然後我們再另外用pick[i][j]來紀錄我們每一步的選擇, pick[i][j] = [我們有沒有選digits[i], 我們從哪個狀態轉移過來]

這樣我們就能從最後的dp[n][0]回頭重構出我們的每一步決策

```py
res = ""
i, j = n, 0
while i > 0:
    if pick[i][j][0]:
        res += str(digits[i])
    j = pick[i][j][1]
    i -= 1
res = res[::-1]
```

最後一樣記得移除leading zeros
```py
i = 0
while i < len(res)-1 and res[i] == "0":
    i += 1
return res[i:]
```