# [Intuition](https://leetcode.com/problems/find-all-duplicates-in-an-array/solutions/4921307/o-1-without-extra-space-mar-day-25-2024-dailychallenge/)

nums[i]範圍在[1,n], 代表nums[i]剛好可跟 `i+1` 一一對應
從左到右遍歷一遍, 持續將nums[i]放置到相對應的index `nums[i]-1`位置, index sort, 直到nums[i] == i+1
如果過程中nums[i]已出現在該位置代表有重複, 那就放到nums尾端, 跟尾端交換

也就是我們還需要另一個pointer `j`指向nums[n-1]
每當找到重複, 我們就將nums[i]跟nums[j]互換, 持續將重複的數從後往前放在j位置上
放置後持續將j往前移動到下個不在正確位置的數

如此一來, 最後nums[i]應都放在i+1位置上
而最終答案就是所有nums[i]不等於i+1的所有數

```
index:    0, 1, 2, 3, 4, ...
nums[i]:  2, 3. 4. 5, 1, ...

index:    0, 1, 2, 3, 4, ...
nums[i]:  3, 2. 4. 5, 1, ...

index:    0, 1, 2, 3, 4, ...
nums[i]:  4, 2. 3. 5, 1, ...

index:    0, 1, 2, 3, 4, ...
nums[i]:  5, 2. 3. 4, 1, ...

index:    0, 1, 2, 3, 4, ...
nums[i]:  1, 2. 3. 4, 5, ...

index:    0, 1, 2, 3, 4, 5 ... j
nums[i]:  1, 2. 3. 4, 5, 1 ... nums[j]

index:    0, 1, 2, 3, 4, 5, ...,       j
nums[i]:  1, 2. 3. 4, 5, nums[j], ..., 1

then move nums[j] to nums[j]-1
```

time: O(n)
space: O(1)

