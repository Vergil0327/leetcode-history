# Intuition

其實這題就延續`3621. Number of Integers With Popcount-Depth Equal to K I`的概念

其實depth只跟nums[i]的1-bit數目有關, 以python來說就是`nums[i].bit_count()`
所以雖然`nums[i] <= 10^15`, 但我們只需從binary format來看depth
log2(10^15) 也就50, 所以我們可以預先計算出所有可能nums[i]的depth

```py
m = ceil(log2(10**15))+1
depth = [0] * m
for i in range(2, m):
    depth[i] = depth[i.bit_count()]+1
```

再來由於我們query要算出有多少nums[i]的index落在[l,r]這範圍, 直覺想到就是我們可以用depth[popcount(nums[i])]來做分組
用position[depth[popcount(nums[i])]] = [index1, index2, ...]來記錄每個相同深度的nums[i]的位址

那這樣我們後續query就可以直接挑出`depth==k`的所有index來, 再透過binary search找出lowerbound及upperbound算出有多少合法的nums[i]

```py
position = defaultdict(SortedList) # position[depth] = [index1, index2, ...]

for query in queries:
    if query[0] == 1:
        l, r, k = query[1], query[2], query[3]

        i = position[k-1].bisect_left(l)
        j = position[k-1].bisect_right(r)
        res.append(j-i)
```

但這邊要特別注意:
因為depth[popcount(nums[i])]記錄的其實是step, ex. depth[1] = 0, depth[2] = 1
以`nums[i]=2`來說, depth[2]=1, 但此時k=2
所以後續query的k, 要用depth[k-1]去帶入才會是我們binary search的數

note. 也因為我們在記錄時, 是記錄depth[popcount(nums[i])], popcount(nums[i])已經先多前進了一層depth

所以如果`nums[i]==1`, 要視為特例, 因為depth[1] = 0, 並且query要用到`k-1`的關係(如果num的k=X, 那麼depth[num] = X-1)
所以在一開始, 我們得記錄成`1`的位置為 position[-1].add(i)

```py
position = defaultdict(SortedList)
for i, num in enumerate(nums):
    if num == 1:
        position[-1].add(i)
    else:
        position[depth[num.bit_count()]].add(i)
```

那這樣後續邏輯就清晰了, 對於第二種queries[i], 更新nums[idx] = val
我們僅需要維護好position[depth[popcount(nums[idx])]]即可 (Index Mapping)


# Intuition - Popcount-Depth Solution Analysis

## Problem Understanding

This problem extends the concept from "3621. Number of Integers With Popcount-Depth Equal to K I". We need to:
1. Handle range queries to count elements with specific popcount-depth
2. Support dynamic updates to array elements

## Key Insights

### 1. Depth Only Depends on Bit Count
The popcount-depth of a number depends solely on the number of 1-bits in its binary representation, not the actual value. For any number `x`, its depth is determined by `x.bit_count()`.

### 2. Precompute All Possible Depths
Since `nums[i] ≤ 10^15`, we only need to consider up to `⌈log₂(10^15)⌉ ≈ 50` bits. We can precompute the depth for all possible bit counts:

```python
m = ceil(log2(10**15)) + 1
depth = [0] * m
for i in range(2, m):
    depth[i] = depth[i.bit_count()] + 1
```

### 3. Group Indices by Depth
To efficiently answer range queries, we group array indices by their popcount-depth using sorted data structures:

```python
position = defaultdict(SortedList)  # position[depth] = [index1, index2, ...]
```

## Implementation Strategy

### Initialization
For each element `nums[i]`, we calculate its popcount-depth and store its index in the corresponding group:
- Special case: If `nums[i] == 1`, depth = 1, but we store it as `position[-1]` (explained below)
- General case: Store index in `position[depth[nums[i].bit_count()]]`

### Query Processing

#### Type 1: Range Query `[1, l, r, k]`
Use binary search to count indices in range `[l, r]` with popcount-depth `k`:
```python
i = position[k-1].bisect_left(l)   # First index ≥ l
j = position[k-1].bisect_right(r)  # First index > r
count = j - i
```

#### Type 2: Update Query `[2, idx, val]`
1. Remove `idx` from its current depth group
2. Update `nums[idx] = val`
3. Add `idx` to its new depth group

## Critical Detail: Index Mapping

There's an important offset between query parameter `k` and our internal depth representation:
- When querying for popcount-depth `k`, we need to look up `position[k-1]`
- This is because our `depth` array represents the number of steps, while the query `k` represents the final depth level

### Special Case for nums[i] = 1
- `nums[i] = 1` has popcount-depth = 1 (it's already at the target)
- Our `depth[1] = 0` (0 steps needed)
- To handle the `k-1` mapping correctly, we store indices of value 1 in `position[-1]`
- This way, when `k = 1`, we look up `position[1-1] = position[0]`, but for the special case of value 1, we use `position[-1]`

## Time Complexity
- Preprocessing: O(n log n) for sorting indices
- Query Type 1: O(log n) per query using binary search
- Query Type 2: O(log n) per query for SortedList operations

## Space Complexity
- O(n) for storing indices in sorted lists
- O(log(max_value)) for precomputed depths