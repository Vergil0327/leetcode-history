# Intuition

我們目標是要判斷每個點是不是都有存在著一個atk跟def都嚴格大於自己的點

比較直覺的做法是先排序其中一項屬性，然後再比較另一個

所以我們可以借鑑bucket sort的方式, 先用個hashmap把相同atk的點先集合在一塊, 那這樣只要對這些group組做排序

這樣對於當前sameAttack group來說:
我們只要跟higher attack groups裡的`maximum defence`比對即可

所以我們首先先以attack做分類, 然後把這些點都存進max heap裡
```py
sameAttack = defaultdict(list)
for atk, defen in properties:
    heapq.heappush(sameAttack[atk], -defen)
```

再來我們在取出每個groups裡的最大defence以及他們相對應的attack存進全局的max heap

```py
maxH = []
for atk, pq in sameAttack.items():
    heapq.heappush(maxH, (pq[0], atk))
```

那這樣我們就知道我們由小到大遍歷`sameAttack`:
1. 以atk作為index, atk <= 當前atk的都pop掉後, 我們就能知道higher attack groups裡的`max_def`是多少
2. 再來我們再把當前groups裡所有`def >= max_def`都pop掉
3. 那麼剩下還沒pop掉的就是weak point

time: O(nlogn) 

# Other Solution 1 - Sorting

但整理一下上面的解法可知
重點就是先對attack做排序, 然後跟higher attacks的點裡的max defense做比較

所以我們可以先對attack由大到小排序
然後維護一個`maxDefUntil`

1. 如果當前`properties[i][1] < maxDefUntil`, 那他就是weak point
2. 如果不是, 那就更新`maxDefUntil`

但這有個重點是, 如果attack相等怎辦?
所以我們應當首先對attack由大到小排序, 如果相等再對defense由小到大排序
這樣當attack相等時, 由於當前def必定大於前一個，這樣就能避免誤算 (因為weak point必須atk跟def都嚴格大於才行)

# Other Solution 2 - Sorting + Stack

這個概念也是一樣, 只是改成用monotonic stack來取代`maxDefUntil`

```py
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        
        stack = []
        ans = 0
        
        for a, d in properties:
            while stack and stack[-1] < d:
                stack.pop()
                ans += 1
            stack.append(d)
        return ans
```