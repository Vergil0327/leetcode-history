# Intuition

num = X X X X X {X} [X]
                j-1  i
                 k   j
num = X X X {X X} [X X]
              j-1  j i
             k   
num = X {X X X} [X X X]
         k  j-1  j   i

num = {X X X} [X X X X]
       k  j-1  j     i

我們需要知道的是以第`i`個元素結尾, 往前找一段num[j:i]
有多少方法能接在num[:j-1]後面

如果最後一段是num[j:i], 那我們僅需要關注前一個substring即可
看前一個有多少種可能方法可以接在後面

前一個區間在沒有**leading zeros**的情況下, 最長長度至多能跟num[j:i]相等
但要注意的是，由於必須是non decreasing, 所以在長度相等時:
nums[k:j-1]必須小於num[j:i]

所以如果前一個區段的長度為 1, 2, 3, ..., len(num[j:i])-1時都是筆num[j:i]小的
惟獨前一個區段長度與len(num[j:i])相等時，我們必須判斷下有沒有non decreasing order
當前的方法數就是前面區段的全部可能方法數加總

所以一開始會想到我們可以紀錄 dp[i][len]: the number of ways considering first `i` characters in num with `len` length

那麼dp[i][len] += dp[j-1][len2] where len2 = 1, 2, 3, ..., len-1 and (len if non decreasing)
```py
for i in range(n):
    for length in range(1, (i+1)+1):
        j = i-length+1

        # leading zero
        if nums[j] == "0": continue
        
        if length == i+1: # j = 0
            dp[i][length] = 1
        else:
            length2 = min(length, j)
            if num[j:i] < num[j-length:j]: # O(n)
                length2 -= 1

            # leading zero
            while length2 >= 1 and num[j-length2] == "0":
                length2 -= 1

            for l in range(1, length2): # O(n)
                dp[i][length] += dp[j-1][l]
return sum(dp[n-1])
```

那這樣會是個O(n^3)的解法

由於我們會需要將dp[j-1][l] where l from 1 to length2 全加總起來
所以其實我們真正需要的是prefix sum dp

所以如果改為presum_dp的話變成:

從j-1開始累加length2長度
`dp[i][length] = presum_dp[j-1][length2]`

然後我們也需要更新presum_dp
`presum_dp[i][length] = presum_dp[i][length-1] + dp[i][length]`

```py
for i in range(n):
    for length in range(1, (i+1)+1):
        j = i-length+1

        # leading zero
        if nums[j] == "0": continue
        
        if length == i+1: # j = 0
            dp[i][length] = 1
        else:
            length2 = min(length, j)
            if num[j:i] < num[j-length:j]: # O(n)
                length2 -= 1

            # leading zero
            while length2 >= 1 and num[j-length2] == "0":
                length2 -= 1
            
            # for l in range(1, length2): # O(n)
            #     dp[i][length] += dp[j-1][l]
            dp[i][length] = presum_dp[j-1][length2]
        presum_dp[i][length] = presum_dp[i][length-1] + dp[i][length]
return sum(dp[n-1])
```

這時會發現dp[i][length]只是個臨時變量
所以我們其實僅需要presum_dp

```py
for i in range(n):
    for length in range(1, (i+1)+1):
        j = i-length+1

        # leading zero
        if nums[j] == "0": continue
        
        if length == i+1: # j = 0
            dp = 1
        else:
            length2 = min(length, j)
            if num[j:i] < num[j-length:j]: # O(n)
                length2 -= 1

            # leading zero
            while length2 >= 1 and num[j-length2] == "0":
                length2 -= 1
            
            dp = presum_dp[j-1][length2]
        presum_dp[i][length] = presum_dp[i][length-1] + dp
return presum_dp[n-1][n]
```

由於python對於slice的判斷很快，所以可以通過
但實際上`if num[j:i] < num[j-length:j]:`這個判斷仍是個O(n)的判斷

# Optimization

對於兩個substring比大小, 其實要比的是第一個不同的num[i]

如果num[j:i] = XXXXX6
nums[j-length:j] = XXXXX9

如果前面都相同，那就看第一個不同的字符即知道兩個誰大誰小

所以這邊可以預處理的是先求出Longest Common Substring的長度

例如:
s = X X X X [X X X X X X] X [X X X X X X]
             p         q     j         i

分別以p跟j為起點的最長公共substring長度如果為6
lcs[p][j] = 6
那我們就看`s[p+lcs[p][j]]`跟`s[j+lcs[p][j]]`誰大誰小
即可判斷出num[p:q]的跟num[j:i]誰大誰小

```py
for i in range(len(s)-1, -1, -1):
    for j in range(len(s)-1, -1, -1):
        if s[i] == s[j]:
            lcs[i][j] = lcs[i+1][j+1] + 1
```