# Intuition

由於每個queries[i]都只能在[l,r]範圍內最多`-1`, 直覺想到是盡可能挑queries[i]涵蓋範圍大的

而且在沒有想法的情況下, 對queries排序並不影響結果, 所以試著排序看看
看有沒有什麼幫助

```py
queries.sort()
```

在試著對queries排序後, 我們逐個nums[i]來看
對於nums[i]來說, 所有queries[j][0] <= i的我們都可以選用來減少nums[i]
那延續我們一開始**Greedy**的想法, 我們挑選的依據是從這些合法的queries[j]當中
挑出nums[i]個queries[j][1]涵蓋最遠的

因此我們需要個有序容器, `candidates`, 來儲存合法queries[j], 也就是有涵蓋到nums[i]的queres[j]

```py
j = 0
candidates = SortedList()
for i, num in enumerate(nums):
    while j < len(queries) and queries[j][0] <= i:
        candidates.add(queries[j][1])
        j += 1
```

然後我們再從`candidates`中挑出`nums[i]`個涵蓋最遠範圍的出來, 這樣才能將zero nums[i]
所以我們在另外用個容器儲存當前挑選的queries[j]

> 這邊記得注意如果我們**合法**的candidates不夠, 那代表我們無法成功zero nums[i]
> 這時我們直接返回`-1`

```py
current = SortedList()
for i, num in enumerate(nums):
    # ...

    while len(current) < num:
        if not candidates or candidates[-1] < i:
            return -1
        current.add(candidates.pop())
```

再來別忘記, 隨著我們`i`往後遍歷, 我們當前的`current`也要逐步淘汰掉不再涵蓋到`i`的queries, 記得將他們從`current`中移除掉

而且這邊會發現, 由於我們必須要判斷當前挑選的queries是否還有涵蓋到`i`
所以我們`current`也必須是個有序容器

```py
for i, num in enumerate(nums):
    # ...

    while current and current[0] < i:
        current.pop(0)

    while len(current) < num:
        if not candidates or candidates[-1] < i:
            return -1
        current.add(candidates.pop())
```

那最終答案就是那些沒有使用到的`candidates`

```py
return len(candidates)
```