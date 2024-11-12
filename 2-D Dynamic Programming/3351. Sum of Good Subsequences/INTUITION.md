# Intuition

nums[i] 可接在`nums[i]-1`跟`nums[i]+1`後面, 也可自立門戶

如果定義`total[nums[i]]: the sum of good subsequences ended at nums[i] `
那麼狀態轉移:

> total[nums[i]] += (total[nums[i]-1] + nums[i] * number of good subseq. ended at `nums[i]-1`) + (total[nums[i]+1] + nums[i] * number of good subseq. ended at `nums[i]+1`) + nums[i]

所以我們這邊還得再定義一個`count[nums[i]]: the number of good subseq. ended at nums[i]`
狀態轉移也很直覺, 如前面所述: nums[i] 可接在`nums[i]-1`跟`nums[i]+1`後面, 也能自立門戶:

> count[nums[i]] += count[nums[i]-1] + count[nums[i]+1] + 1

結合上述兩個式子, 可得到:

```py
count[nums[i]] += count[nums[i]-1] + count[nums[i]+1] + 1

total[nums[i]] += (total[nums[i]-1] + nums[i] * count[nums[i]-1] + 
                  total[nums[i]+1] + nums[i] * count[nums[i]+1] + 
                  nums[i])
                = total[nums[i]-1] + total[nums[i]+1] + nums[i] * (count[nums[i]-1] + count[nums[i]+1] + 1)
```

最終答案就是`sum(total.values()) % 1_000_000_007`

# Complexity

- time: O(n)
- space: O(nums[i])