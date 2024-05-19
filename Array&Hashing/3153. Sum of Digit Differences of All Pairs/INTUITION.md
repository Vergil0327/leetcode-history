# Intuition

ex.1 nums=[13,23,12]

digit[0] = [2,3,3] => {2: 1, 3: 2}
digit[1] = [1,1,2] => {1: 2, 2: 1}
digit: 0~9

看了一下我們目的是希望找出每個pair [nums[i], nums[j]]裡, 每個位數有多少個不同的digit, 最後全部加總

所以首先就想, 我們應該每個位數單獨拆開, 縱向來看
nums[0] = 13
nums[1] = 23
nums[2] = 12

我們分成:
個位數:[3,3,2]
十位數:[1,2,1]

由於nums[i] <= 10^9 => 最多分出9個長度為len(nums)的array
那再來我們要算的是不同digit的個數 => 直覺想到用hashmap存{digit: count}
那這樣我們就知道該位數, 每個digit有多少個數

由於digit範圍: 0~9, 所以我們每個array都遍歷digit去算有多少個不同digit, 最後總和即可


首先先求出count[i][j]: 第i位數有多少個`j`, 0 <= j <= 9
```py
m, n = len(str(nums[0])), len(nums)
digits = [[0]*n for _ in range(m)]

for i in range(n):
    for j in range(m):
        digits[j][i] = nums[i]%10
        nums[i] //= 10

count = [defaultdict(int) for _ in range(m)]
for i in range(m):
    for j in range(n):
        count[i][digits[i][j]] += 1
```

那再來我們就在各個位數上, 遍歷兩個不同digit, `num1`, `num2`並看他們的個數即可知道有多少個不同digit pair

遍歷num1, num2 from 0 to 9, 只要**num1 != num2**, 就代表有個pair提供了一個
然後該位數上, 有count[i][num1]個num1, 有count[i][num2]個num2
所以總共有`count[i][num1] * count[i][num2]`個(num1, num2)pair

```py
res = 0
for i in range(m):
    for num1 in range(10):
        for num2 in range(num1+1, 10):
            numDiff = count[i][num1] * count[i][num2]
            res += numDiff
return res
```