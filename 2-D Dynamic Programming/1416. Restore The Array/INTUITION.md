# Intuition

首先從Example 3觀察可發現
對於第i個元素來說，如果他本身 `1 <= s[i] <= k` 那就加上之前的每個合法組成array的方法數
然後他還可以跟前一個元素組成integer，如果`1 <= s[j:i] <= k`的話那麼就可以加上j-1前的所有方法數

1317
1 -> 1 = [1]
13 -> 2 = [(1, 3), (13)]
131 -> 4 = [(1,3,1), (13,1), (1,31), (131)]
1317 -> 8 = [[(1,3,1,7), (1,3,17)], [(1,31,7), (1,317)] [(13,1,7), (13,17)], [(131, 7), (1317)]]

所以更general來看的話，我們只要看最後組成的整數即可
所以我們可以這麼定義 dp[i]: the number of the possible arrays that can be printed as s[:i] using the mentioned program

XXXXXXXXXXXX{X}
            j/i
XXXXXXXXXXX{XX}
            ji
XXXXXXXX{XXXXX}
         j   i

所以我們可以回頭找`j`, 使得`s[j:i]`是合法的:
1. 1 <= int(s[j:i]) <= k
2. 沒有leading zero

那麼我們就可以從dp[j-1]轉移過來, 由於每個方法數都是合法的，所以是加法原理
```py
for j in range(i, -1, -1):
    dp[i] += dp[j-1]
    dp[i] %= int(1e9+7)
```

由於dp會有個`j-1`的key存在
因此我們可以用**1-indexed**來讓0當base case使得合法區間為`[1, n]`
所以我們的dp跟s都移成**1-indexed**, 然後進行狀態轉移

由於我們每次都會增加一個位數，所以當`num > k`後就可以break

```py
n = len(s)
dp = [0] * (n+1)

s = "$" + s # 1-indexed
for i in range(1, n+1): # [1,n]
    for j in range(i, 0, -1): # [1,i]
        substr = s[j:i+1]
        num = int(substr)
        if num > k: break
        if len(substr) > 1 and substr[0] == '0': continue # leading zeros
        if 1 <= num <= k:
            dp[i] += dp[j-1]
            dp[i] %= MOD
return dp[n]%MOD
```

然後別忘了 **Base Case**

`dp[0] = 1`

但上面程式碼實際上會TLE, 一但有個`s=100000000..........00000`的話
我們內層循環會一直的找下去，這樣會變成一個$O(N^2)$的解法

但實際上我們並不需要一直找下去，就像前面提的，一但位數 > k的位數的話，那數值肯定就超過了
所以我們還可以透過目前位數來判斷要不要break

```py
for j in range(i, 0, -1): # [1,i]
    substr = s[j:i+1]
    if len(substr) > len(str(k)): break
```

並且觀察一下`k`的數據範圍, `1 <= k <= 10^9`
k最多就1後面9個0，最多就十位數
所以實際上內層循環只會跑十次

# Complexity

- time complexity

$$O(10n)$$