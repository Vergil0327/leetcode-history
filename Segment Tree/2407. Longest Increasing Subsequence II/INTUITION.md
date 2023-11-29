# Intuition

```
{X X X X X} X
            i
```

對於nums[i]來說, 我們要在前面找個nums[j]其中讓nums[i]可以接在nums[j]後面的條件是:
1. nums[i] > nums[j]
2. nums[i]-nums[j] <= k

所以就是在前面nums[:i-1]裡, 所有最後一個數值落在[nums[i]-k, nums[i]-1]範圍中的subseq.都可以接在nums[i]前
所以我們肯定是挑最長的一個subseq.來將nums[i]接在後面

由於要再任意區間找出長度最長的subseq., 這時就需要用到segment tree
用segment tree來搜尋這區間**[nums[i]-k, nums[i-1]]**中, max subsequence.length
那麼res = max(res, segment_tree.query(nums[i]-k, nums[i]-1)+1)

同時並持續更新segment_tree.update(nums[i], segment_tree.query(nums[i]-k, nums[i]-1)+1)

所以整體框架如下, 把num作為segment tree的index:
而且segment tree 的size就是nums的數值範圍: n = max(nums)
另外這邊要特別注意的是 n=max(nums), 所以在query跟update的時候, 實際上num必須`-= 1`才會是segment tree的index
轉為0-indexed的意思

```py
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        st = SegmentTree()

        res = 1
        for num in nums:
            num -= 1 # to 0-indexed
            length = st.query(max(0, num-k), num-1)
            res = max(res, length+1)
            st.update(num, length+1)
        return res
```