# Intuition

Input: s = "DID"
Output: 5
Explanation: The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)
(3, 2, X)

問多少種構造方法, 首先想到利用dynamic programming
首先第一個下標首先會想到是利用前**i**個元素, 而我們又必須滿足s的DI序列, 所以我們在紀錄i-th element我們選了什麼, 紀錄為`j`

這樣下來, 比較直覺能想到的定義是:

dp[i][j]: the number of valid permutations considering [0:i] and i-th element is `j`

```
XXXXXXX prev j
        i-1  i
```

- if s[i] == "I"

i-th element is `j`, 我們看前面i-1的最後一位`prev`
由於s[i]=="I", 所以prev可以是[0,j-1]

- if s[i] == "D"

i-th element is `j`, 我們看前面i-1的最後一位`prev`
由於s[i]=="D", 所以prev可以是[j+1, i-1] => 前i-1個element, 最大到i

但這題最tricky的地方就是, 我們的前驅狀態漏了dp[i-1][j]的轉移
如果前面i-1的最後一位就已經是`j`了, 那這狀態還要考慮嗎?

有點不好想到, 但其實是要考慮的

我們這邊用[0:i]定義, 但其實數字對我們並不重要, 我們真正關心的是s的序列條件
也就是我們用**1~n**來找valid permutations跟**0~n-1**或**5~n+4**都沒差
因為我們並不關心我們用了哪些數, 我們關心的是這些數的排列是否符合s這個DI序列
定義[0:i]只是為了比較好計算valid permutations的狀態

所以回到上面, 如果`prev`已經是`j`了的這個dp[i-1][j]狀態, 還能轉移嗎?
答案是要考慮進來的, 因為她代表的是`i`在前面perm[:i-1]的情況
不然我們所有狀態轉移, 前面i-1個元素的狀態永遠都不包含`i`
但其實元素範圍[0:i], 最大的`i`是可以排在前面的

看下面這例子
```
ex. s[i] = "D", perm[:i-1] = 102
  i-1  i
10 2   2
```

這時由於我們決定i-th element是2, 為了讓前面[0:i-1]滿足DI, 但又不能使用到2的情況的話
可以想成前面的perm[:i-1]裡的所有**大於等於2**的元素都抬升1位, 都+1
所以"perm[:i-1] = 102" 變成 "perm[:i-1] = 103"
這時我們i-th element就可以是2了, "perm[:i]=1032", 一樣滿足s序列

仔細想想會發現**dp[i-1][j]**所代表的其實是**dp[i-1][i]**這狀態

所以如果當s[i]=="D"時, 如果不考慮前一位`prev`是`j`時的狀態, 那我們就相當於少考慮了**prev=i時的狀態**

因此根據討論, 我們能寫出整個狀態轉移如下
最終答案則為考慮全部n個數, 但結尾可能是任意數, 所以為**sum(dp[n])**

```py
n = len(s)
s = "#" + s # to 1-indexed
mod = 10**9 + 7
for i in range(1, n+1):
    for j in range(i+1):
        if s[i] == "I":
            for prev in range(j):
                dp[i][j] += dp[i-1][prev]
        else:
            for prev in range(j, i):
                dp[i][j] += dp[i-1][prev]
        dp[i][j] %= mod

return sum(dp[n]) % mod
```

至於base case:

根據定義, [0:0]裡, 最後一位是0, 這根據定義也是合法狀態, 而且只有這麼一個
=> **dp[0][0] = 1**

如有疑惑, [@HuifengGuan](https://www.youtube.com/watch?v=WL-w3dbOOYw&ab_channel=HuifengGuan) 有影片詳述