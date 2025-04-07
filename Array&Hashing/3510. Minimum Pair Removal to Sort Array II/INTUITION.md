# Intuition

1. 由於我們操作只能從minimum pair sum開始進行合併, 所以我們肯定得需要一個有序容器來容納每個pair.
    - 由於相同pair sum, 以最靠左為優先, 所以有序容器裡的權重為(pair sum, index)
    - `sl = SortedList([nums[i] + nums[i + 1], i] for i in range(n - 1))`
2. 由於我們必須隨時能判斷當前的`nums`是否已經是排序好的狀態, 所以我們必須記錄一下當前有多少個pair是需要更換的, 後面隨著操作再持續更新
    - `inverse = sum(nums[i] > nums[i + 1] for i in range(n - 1))`

3. 下面示意圖模擬整個過程, 會發現整個操作過程很像是**doubly linked list**, 所以對於每個nums[i], 我們分別紀錄它當前指向的左右節點為`L[i]`, `R[i]`. 後續我們只要持續維護`L[i]`, `R[i]`即可有效節省時間, 而非更新整個`nums`

```
O O O O O O O O {X O} O  O O O
O O O O O O O O {X _} O  O O O
O O {X _ _} O O {X _  _} O X O

...

O O O O O -> sorted
```

4. 後續就是模擬整個過程, 並維護`L`, `R`, `inverse`即可, 整體架構如下
    - 對於當前操作pair (i,j), 假如在`nums`裡位置為[..., l, i, j, r, ...], 在合併(i,j)時, (l,i'), (i,j), (j,r)都會影響到`inverse`, 其中`i'`為合併後的結果

```py
from sortedcontainers import SortedList
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        inverse = sum(int(nums[i] > nums[i+1]) for i in range(n-1))
        sl = SortedList([nums[i] + nums[i + 1], i] for i in range(n-1))

        L = list(range(-1, n-1))
        R = list(range(1, n+1))

        def add(i):
            nonlocal inverse

            j = R[i]
            if 0 <= i < j < n:
                sl.add([nums[i]+nums[j], i])
                inverse += int(nums[i] > nums[j])

        def remove(i):
            nonlocal inverse

            j = R[i]
            if 0 <= i < j < n:
                sl.discard([nums[i]+nums[j], i])
                inverse -= int(nums[i] > nums[j])

        res = 0
        while inverse > 0:
            res += 1

            # [..., l, i, j, r, ...]
            # find index of minimum pair sum
            _, i = sl.pop(0)
            j = R[i]
            l, r = L[i], R[j]

            # remove linked list nodes first
            remove(l)
            remove(i)
            remove(j)

            # merge (i,j), update `L`, `R`, `nums[i]`
            nums[i] += nums[j]
            R[i] = r
            if r < n:
                L[r] = i

            # add new merged node back to linked list
            add(l)
            add(i)
        return res
```

其中`remove`跟`add`兩個helper function為:

```py
def add(i):
    j = R[i]
    if 0 <= i < j < n:
        sl.add([nums[i]+nums[j], i])
        inverse += int(nums[i] > nums[j])

def remove(i):
    j = R[i]
    if 0 <= i < j < n:
        sl.discard([nums[i]+nums[j], i])
        inverse -= int(nums[i] > nums[j])
```