# Intuition

想法是以coordinates[k]為分界, 分為前後半段的longest increasing subsequence
由於`coordinates`是亂序二維座標, 所以直覺會想到我們可以先對維度做排序

```py
from sortedcontainers import SortedList
class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        n = len(coordinates)
        x, y = coordinates[k]

        coordinates.sort(key=lambda x:(x[0], -x[1]))
        before, after = SortedList(), SortedList()
        for xx, yy in coordinates:
            if xx < x and yy < y: # 前半段LIS
                i = before.bisect_left(yy)
                if i == len(before):
                    before.add(yy)
                else:
                    num = before.pop(i)
                    before.add(min(num, yy))
            elif xx > x and yy > y: # 後半段LIS
                i = after.bisect_left(yy)
                if i == len(after):
                    after.add(yy)
                else:
                    num = after.pop(i)
                    after.add(min(num, yy))
        return len(before) + 1 + len(after)
```

## tricky sorting

但這個test case會發現我們`after`這陣列數組在x座標上重複了

```
coordinates = [[5,0],[9,3],[9,8]]
k = 0
Output: 3
Expected: 2
```

after = [3,8] => [[9,3], [9,8]]
但實際上我們希望的應該是[3]或[8], 兩者都可以接在coordinates[k]後面

而我們邏輯上應該要greedily將這個值壓得越小越好，小到剛剛好大過前個sequence item

所以我們sequence排序上我們對`x`由小到大排序後, 在對`y`由大到小排序
那這樣我們的`after`首先會遍歷到`[9,8]`, 變成`after=[8]`
再來再透過`bisect_left`將`after`更新為`after=[3]`

如此一來就會是正確的Longest Increasing Subsequence了

那既然已經是LIS, 我們也可以直接用簡單的list即可, 並不需要SortedList

```py
class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        n = len(coordinates)
        x, y = coordinates[k]

        coordinates.sort(key=lambda x:(x[0], -x[1]))
        before, after = [], []
        for xx, yy in coordinates:
            if xx < x and yy < y: # 前半段LIS
                i = bisect_left(before, yy)
                if i == len(before):
                    before.append(yy)
                else:
                    before[i] = min(before[i], yy)

            elif xx > x and yy > y: # 後半段LIS
                i = bisect_left(after, yy)
                if i == len(after):
                    after.append(yy)
                else:
                    after[i] = min(after[i], yy)
        return len(before) + 1 + len(after)
```