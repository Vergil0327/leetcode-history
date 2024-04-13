# Intuition

很簡單的一題, 只花30分就迅速解掉

首先是觀察到: `1 <= nums.length <= 10^5`

所以想到大概是O(n)或O(nlogn)的解法

再來看了一下example發現, 我們可以每個nums[i]分別處理：

利用hashmap `v2idx` 記錄每個nums[i]的位置後, v2idx[nums[i]] = [idx1, idx2, idx3, ...]

那對於位於idx1的nums[i]來說, 如果他作為左端點, 那麼會有哪些其他位置的nums[i]是可以作為右端點的?
而合法的subarray的定義是啥?
合法的subarray必須是以nums[i]作為最大element, [nums[idx1]:nums[idx2]]這範圍內沒有大於nums[i]的

所以我們關心的, 是下個大於nums[idx1]的數的位置在哪裡? 
也就是nextGreater[idx1] = j的話, 所有小於`j`的idx2, idx3, ...都可以作為右端點
而這個我們可以用`r = bisect_left(v2idx[nums[i]], nextGreater[idx1])`來找出有多少個合法右端點
那麼idx1就可以組出**r-idx1**個合法subarray

而nextGreater element可以利用monotonic stack以O(n)時間找出

所以整理一下:

1. 首先先找出每個nums[i]的位置

```py
v2idx = defaultdict(list)
for i in range(n):
    v2idx[nums[i]].append(i)
```

2. 再來找出每個nums[i]的nextGreater element

```py
nextGreater = [n]*n
stack = []
for i in range(n):
    while stack and nums[stack[-1]] < nums[i]:
        nextGreater[stack.pop()] = i
    stack.append(i)
```

3. 那最後整體框架就是遍歷每個nums[i], 然後在遍歷每個index作為左端點, 在用binary search找出合法右端點的個數

```py
res = 0
for indices in v2idx.values():
    for i in range(len(indices)):
        k = nextGreater[indices[i]]
        j = bisect_left(indices, k)
        res += j-i
return res
```

這樣分析一下, 每個位置的nums[i]只會遍歷一遍, 並且利用O(logn)時間找出能貢獻的合法subarray個數

整體時間複雜度為O(nlogn)

# Optimized O(n) solution

[@lee215](https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/solutions/5017056/java-c-python-stack-o-n/)

想法一樣是透過monotonic stack去找出next greater element

```py
def numberOfSubarrays(self, nums: List[int]) -> int:
    stack = []
    res = 0
    for num in nums:
        while stack and stack[-1][0] < num:
            stack.pop()
        if not stack or stack[-1][0] > num:
            stack.append([num, 0])
        stack[-1][1] += 1
        res += stack[-1][1]
    return res
```