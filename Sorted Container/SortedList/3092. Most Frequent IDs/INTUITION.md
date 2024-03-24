# Intuition

將整個過程模擬一遍即可
過程中我們需要一個hashmap `count`來記錄當前nums[i]的出現次數
由於我們要找出max frequency, 所以我們需要個有序容器來儲存當前所有frequency
當count[nums[i]] == 0時, 要從有序容器中移除
由於需要動態更新, 所以我們需要Sorted List, 而不能用max heap

```py
count = Counter()
sl = SortedList()

res = []
for num, f in zip(nums, freq):
    if count[num] in sl:
        sl.remove(count[num])
        
    count[num] += f
    if count[num] > 0:
        sl.add(count[num])
        
    res.append(sl[-1] if sl else 0)
return res
```

# Intuition 2

但後來發現事實上也可以用heap解, 只需要outdated, 也就是跟hashmap裡的值不同的刪除即可

```py
def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
    maxHeap = []
    count = Counter()
    res = []
    for num, f in zip(nums, freq):
        count[num] += f
        heappush(maxHeap, [-count[num], num])
        while maxHeap and count[maxHeap[0][1]] != -maxHeap[0][0]:
            heappop(maxHeap)
        res.append(-maxHeap[0][0] if maxHeap else 0)
    return res
```