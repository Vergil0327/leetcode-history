# Intuition

if sum(nums[0:pivot]) == sum(nums[pivot:n]): found 1 valid partition

**nums[i] unchanged (no operation):**
=> res += 1 if presum[pivot-1] == presum[n-1]-presum[pivot-1] # 0-indexed prefix sum

**nums[i] changed (1 operation):**
=> we want `presum[pivot] == presum[n]-presum[pivot]` with nums[i] replaced by k

```
X X X X X X | X X X X X X X
            p i

X X X X X X X X | X X X X X X
            <-i p
```
1. 更改nums[i]為k
2. 如果pivot < i:
    - 我們希望presum[p] == presum[n]-presum[p]+k-nums[i]
    - => presum[p] = (presum[n]+k-nums[i])//2
    - 用個hashmap `count`紀錄`i`之前的prefix sum的個數, res += count[presum[p]]
3. 如果pivot > i:
    - sufsum[p] == sufsum[0]-sufsum[p]+k-nums[i]
    - sufsum[p] = (sufsum[0]+k-nums[i])//2
    - 用個hashmap `count`紀錄`i`之前的suffix sum的個數, res += count[sufsum[p]]

所以用2-pass可以求出我們改變任一nums[i]為k後會有多少個合法pivot
取最大值後, 再跟不改變nums[i]為k的結果比, 取全局最大即可