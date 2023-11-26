# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

首先絕對值比較麻煩, 先想到由小到大排個序
nums[i]能跟所有`nums[j] where nums[j] <= nums[i]+limit`的互換
同理, nums[j]又能跟所有`nums[k] where nums[k] <= nums[j]+limit`互換
所以nums[i], nums[j], nums[k]都是同個group的, 對於同個group, 我們就找出他們的所有index位置
然後就由小到大的將nums[i], nums[j], nums[k], 由小到大地依序擺上每個index位置

所以首先將distinct nums[i]排個序, 然後就開始找出每個可以互換的group
由於已經排序我們就用2 pointers找出所有nums[i], nums[j], nums[k], ...
```py
arr = sorted(set(nums))
counter = Counter(nums)
res = [-1]*n

i = 0
while i < len(arr):
    indices = [] # all the indices in swap group
    num = [] # all the distinct num in swap group
    j = i
    while j < len(arr) and (not num or arr[j] <= num[-1]+limit):
        num.append(arr[j])
        indices.extend(v2idx[arr[j]])
        j += 1

        # process swap group here
        
    i = j
```

等找到swap group後, 由於可以自由互換, 剩下的就是將所有index排序然後再將每個num由小大到依序放置即可
```py
indices.sort()
k = 0
for x in num:
    while counter[x]:
        res[indices[k]] = x
        k += 1
        counter[x] -= 1
```

**English Explanation**

1. if nums[i] and nums[j] can swap, we can find all the nums[i]'s indices and nums[j]'s indices and put nums[i] and nums[j] in non-decreasing order.

ex. v2idx = {nums[i]: [idx1, idx2, idx3, ...], nums[j]: [idxA, idxB, idxC, ...]}

if nums[i] < nums[j], we can sort indices (v2idx[nums[i]]+v2idx[nums[j]]) and put nums[i] in order first, then nums[j]

```
sorted indices: idx1,   idxA,   idx2,  , ..., idxB,    idxC, ...
num           : nums[i] nums[i] nums[i], ..., nums[j], nums[j], ...
```


2. find swap groups
    - since we can swap nums[i] with nums[j] if |nums[i]-nums[j| <= limit, we sort distinct nums[i] first, then start from nums[i], keep exploring nums[j] where nums[j] <= nums[i]+limit. once we finish exploring nums[i], we change to explore nums[j] and find nums[k] where nums[k] <= nums[j]+limit, ...
    - after exploring all, nums[i] can swap with nums[j], nums[j] can swap nums[k], thus, nums[i], nums[j] and nums[k] can swap each other. we can take this group and apply **1.**, sort all the indices and put in order.

3. after sorting every swap groups, we can get our desired answer

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
$$O(nlogn)$$ for sorting every index onces

- Space complexity:
$$O(n)$$

# Intuition 2

另外這題也能用union-find
想法一樣, 先將nums排序後找出所有可以自由互換的index, 把他們union在一起

然後找出每個groups後, 把該groups裡的所有數值找出來, 數值由小到大依序擺置在該group的index即可

[@votrubac](https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/solutions/4330378/union-find-1202-smallest-string-with-swaps/)
```c++
int find(vector<int> &ds, int i) {
    return ds[i] < 0 ? i : ds[i] = find(ds, ds[i]);
}
vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
    vector<int> ds(nums.size(), -1), ids(nums.size()), res(nums.size());
    iota(begin(ids), end(ids), 0);
    sort(begin(ids), end(ids), [&](int i, int j){ return nums[i] < nums[j]; });
    for (int i = 1; i < nums.size(); ++i)
        if (nums[ids[i]] - nums[ids[i - 1]] <= limit)
            if (int a = find(ds, ids[i]), b = find(ds, ids[i - 1]); a != b)
                ds[b] = a;
    unordered_map<int, vector<int>> groups;
    for (int i = 0; i < nums.size(); ++i)
        groups[find(ds, i)].push_back(i);
    for (auto &[g, ids] : groups) {
        vector<int> sorted = ids;
        sort(begin(sorted), end(sorted), [&](int i, int j){ return nums[i] < nums[j]; });
        for (int i = 0; i < ids.size(); ++i) {
            res[ids[i]] = nums[sorted[i]];
        }
    }
    return res;
}
```