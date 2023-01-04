# Greedy

## Intuition

如果將`nums`圖形化表示，/\/\/\/\__/\/\__/\/\/\
可以看到最長的wiggle seq.就是所有的turning point個數，turning points之間不管多少點，
抑或是前後點相等(斜率為0)時，都對wiggle seq.的增加沒有幫助

因此可以應用Greedy Algorithm去找出所有turning points即可

base case: 當只有一個點的時候，wiggle seq. 為 1
並且由於第二個點只要不與第一個點相同(nums[1] != nums[0])，無論斜率正負，皆為一個合法的wiggle seq.，因此`prevSlope`的初始值可以設為任意不與`slope`即可

因此初始長度設值為1，並且我們`i`從1到n開始遍歷，
- 如果**nums[i]-nums[i-1] > 0**，代表nums[i]會使得斜率變正，因此如果前一個斜率為負的話，代表`nums[i]`為turning point
- 反之如果**nums[i]-nums[i-1] < 0**，代表當前斜率為負，因此如果前一個斜率為正的話，代表`nums[i]`為turning point，從圖形上來看也可發現此時wiggle seq.長度增加了

由於

## Complexity

- time complexity

$$O(n)$$

- space complexity

$$O(1)$$

# Dynamic Programming

## Intuition

長度為`i`的wiggle seq必定來自長度`i-1`的wiggle seq.
並且wiggle seq[i]的斜率必定與wiggle seq.[i-1]不同

因此我們必須記錄兩種state，一個是wiggle seq.結尾斜率為正，另一為結尾斜率為負

所以:
dp[0] = [longest length of wiggle seqeunce which ends with positive slope]
dp[1] = [longest length of wiggle seqeunce which ends with negative slope]

並且 base case 為: `dp = [1,1]`

狀態轉移方程為如上所述，wiggle seq[i]的斜率必定與`i-1`相反，因此:

```
dp[i][0] = dp[i-1][1] + 1 if nums[i] - nums[i-1] > 0
dp[i][1] = dp[i-1][0] + 1 if nums[i] - nums[i-1] < 0
```

最後從兩種狀態取最大即可`max(dp[i])`

## Complexity

- time complexity

$$O(n)$$

- space complexity

$$O(1)$$