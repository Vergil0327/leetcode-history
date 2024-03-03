# Intuition

直覺想到我們可以用個有序容器配合binary seach來輕易算出greater(arr1, v)
=> 因此想到我們可以用SortedList來作為arr1及arr2, 那這樣就能很輕易的模擬出整個過程

```py
n = len(nums)
arr1 = SortedList([(nums[0], 0)])
arr2 = SortedList([(nums[1], 1)])
for i in range(2, n):
    x = len(arr1) - arr1.bisect_right((nums[i], i))
    y = len(arr2) - arr2.bisect_right((nums[i], i))

    if x > y:
        arr1.add((nums[i], i))
    elif x < y:
        arr2.add((nums[i], i))
    else:
        if len(arr1) <= len(arr2):
            arr1.add((nums[i], i))
        else:
            arr2.add((nums[i], i))
```

同時我們在儲存的過程中在記錄index, 這樣在整個過程結束後
我們將arr1以及arr2分別對index做排序, 即可還原出答案

```py
res = []
for v, _ in sorted(list(arr1), key=lambda x:x[1]):
    res.append(v)
for v, _ in sorted(list(arr2), key=lambda x:x[1]):
    res.append(v)
return res
```