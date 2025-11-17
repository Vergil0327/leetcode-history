# Intuition

1. stable subarray => non-decreasing array
2. 對於任意valid subarray, 合法subarray數目為: length * (length+1) / 2

- 所以首先將nums分成多段non-decreasing subarrays: nums = [X X X X X] [O O O] [A A A A A] [B B] [C] ...
- 對應每個 [l,r] = queries[i] 找出所在的subarray => 利用hashmap
- 中間完整的subarray部分: sum(length_i * (length_i+1) / 2), 最左最右兩個subarray可能不是完整valid subarray, 分開計算
"""

"""
# Intuition

1. stable subarray => non-decreasing array
2. 對於任意valid subarray, 合法subarray數目為: length * (length+1) / 2

- 所以首先將nums分成多段non-decreasing subarrays: nums = [X X X X X] [O O O] [A A A A A] [B B] [C] ...
- 對應每個 [l,r] = queries[i] 找出所在的subarray => 利用hashmap
- 中間完整的subarray部分: sum(length_i * (length_i+1) / 2), 最左最右兩個subarray可能不是完整valid subarray, 分開計算`[l, ...]`, `[..., r]`

```py
class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        valid_interval = [[]]
        for i in range(n):
            if not valid_interval[-1]:
                valid_interval[-1].append(i)
            elif nums[i] >= nums[valid_interval[-1][-1]]:
                valid_interval[-1].append(i)
            else:
                valid_interval.append([i])

        index_to_position = {}
        for i in range(len(valid_interval)):
            for j in valid_interval[i]:
                index_to_position[j] = i
        
        res = []
        for l, r in queries:
            ll, rr = index_to_position[l], index_to_position[r]
            if ll == rr:
                L = r-l+1
                res.append(L * (L+1) // 2)
                continue

            L1 = valid_interval[ll][-1] - l + 1
            L2 = r - valid_interval[rr][0] + 1

            count = L1 * (L1+1)//2 + L2 * (L2+1)//2
            for i in range(ll+1, rr):
                L = len(valid_interval[i])
                count += L * (L+1) // 2
            res.append(count)
        return res
```

但這樣會TLE, 顯而易見可優化的地方是:

我們能預先計算每個valid subarray的prefix sum of valid count
那這樣就能將這段:

```py
for i in range(ll+1, rr):
    L = len(valid_interval[i])
    count += L * (L+1) // 2
```

轉化成: `prefix_sum[rr] - prefix_sum[ll+1]` (1-indexed)