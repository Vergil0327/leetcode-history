# Intuition

```
nums = S S S S SUM OUT S S S => sum1 = sum(nums) = special_sum + special_sum + outlier

nums' = S S S S SUM ___ S S S => sum2 = sum(nums) - OUT = 2 * sum_special_nums
```

腦力激盪時間:

直覺上我們可以去遍歷猜測每個nums[i]是不是outlier

那麼special_sum = (sum(nums) - nums[i])//2
因此如果nums[i]是possible outlier, 必須符合:
- (sum(nums)-nums[i]) % 2 == 0
- 再來看, 整個nums是由 special_num1, special_num2, ... , sum(special_num[i]), outlier組成, 所以:
    1. 如果outlier == special_sum: 那麼代表count[special_sum]必須至少為2
    2. 如果outlier != special_sum: 那麼代表count[special_sum]必須至少為1