# Intuition

## Brute Force

iterate all subarray and see if it's valid or not
if valid, store in hashset to prune duplicate

```py
def countDistinct(self, nums: List[int], k: int, p: int) -> int:
    n = len(nums)
    distinct = set()
    for i in range(n):
        subarr = []
        divisible = 0
        for j in range(i, -1, -1):
            subarr.append(nums[j])
            if nums[j]%p == 0:
                divisible += 1

            if divisible > k: break
            distinct.add(tuple(subarr))
    return len(distinct)
```

## rolling hash

遍歷所有可能subarray長度
然後對每個長度的subarray進行rolling hash

我們用`N`進制, 其中`N = max(nums)`
那這樣:
1. rolling hash = rolling hash - nums[i-length]*pow(N, length-1)
2. rolling hash = rolling hash * N + nums[i]

同時我們用個hashset來紀錄所有rolling hash
- 如果已紀錄過, 那就跳過
- 如果沒紀錄過
    - 如果divisible <= k, 那`res += 1`
    - divisible > k的話則不符合條件

time: $$O(N^2)$$