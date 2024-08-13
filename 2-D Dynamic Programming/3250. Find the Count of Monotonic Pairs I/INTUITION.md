# Intuition

題意: 找出有多少合法monotonic pairs(arr1, arr2), 其中

arr1 = X X X
arr2 = Y Y Y

需滿足:
arr1[0] <= arr1[1] <= ...
arr2[0] >= arr2[1] >= ...

arr1[0] + arr2[0] == nums[0]
arr1[1] + arr2[1] == nums[1]
...

求合法數目 => dynamic programming => 先試著定義dp state

先試著定義 dp[i][num]: the count of monotonic pairs considering arr1[:i] (1-indexed) and ended at num
由於arr1[i] + arr2[i] == nums[i] => 所以我們遍歷所有可能arr1[i]時, 也會同時確定arr2[i]
dp[i][num] += dp[i-1][j] where 1 <= j <= num and num2 = nums[i] - num and num2 <= nums[i-1]-j

所以整體框架就是遍歷`i`, `num1`, `prev_num1`

```py
n = len(nums)

dp = [[0]*51 for _ in range(n)]

for i in range(1, n):
    # arr1
    for num1 in range(51):
        num2 = nums[i]-num1
        if num2 < 0: continue

        for prev_num1 in range(num1+1):
            pre_num2 = nums[i-1]-prev_num1
            # arr2 non-increasing and non-negative
            if num2 > pre_num2 or pre_num2 < 0: continue
            dp[i][num1] += dp[i-1][prev_num1]
return sum(dp[n-1])
```

base case: arr1, arr2 必須是non-negative array

```py
for num1 in range(51):
    num2 = nums[0] - num1
    if num2 >= 0:
        dp[0][num1] = 1
```

this line: `if num2 > pre_num2 or pre_num2 < 0: continue`
it means `prev_num1 <= min(nums[i-1]-num2, num1)`

we can further make code more concise
