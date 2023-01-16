# Intuition

一開始想透果兩個變數`min`, `max`來指向當前的hashset找出MaxKey, MinKey，但是卻會碰到這樣的情況:

假如原本是這樣
min = 1, max = 2
MinSet = {"remove"}, MaxSet = {"leet", "code"}

我們在一個`dec "remove"`操作後，MinSet都變成空
這時`min`必須更新為`max`並且MinSet必須裝進所有MaxSet裡的數，這樣就無法達到O(1)時間了

**需要的資料結構**

1. Hashmap 儲存每個key出現的次數 `count`
2. Hashmap + Linked List 依序儲存當前所有頻率

這題最關鍵的就是要想到LRU, LFU那樣的做法，每當有新增刪除需要以O(1)時間操作時，只要`Hashmap + Doubly Linked-List`，透過hashmap儲存 Linked List的pointer，即可達到O(1)時間的新增刪除操作

並且還能透過一個Linked List來方便我們處理`getMinKey`及`getMaxKey`，只要我們每個Linked List Node都是依`frequency count`由小到大建立

只要我們知道要增刪的位置，我們就能保持整個Linked List是有序的

ex.
```
Linked List: count0 -> count1 -> count2 -> count3
```

每個List Node的key儲存`count`資訊
因此Linked List 開頭代表count=0的dummy node
- 如果要`getMinKey`，就只要透過`dummy.next.key`即可知道當前最小頻率為多少
- 如果要`getMaxKey`，就只要透過`dummy.prev.key`即可知道當前最大頻率為多少


3. Hashmap 儲存 每個頻率相對應的hashset `val2set`

因為我們只要返回該目標頻率集合內任一個key即可，因此我們可以利用hashset來儲存相同頻率的所有key

並且我們可以透過Linked List得到`dummy.next.key`或`dummy.prev.key`，也就是知道MinKey, MaxKey後即可透過:

```py
next(iter(val2set[dummy.prev.key]))
next(iter(val2set[dummy.next.key]))
```

來取得任一集合內的元素

這邊要注意的是假如`dummy.prev.key`或`dummy.next.key`指向的是dummy node，也就是頻率為0的ListNode的話，代表此時沒有任何元素存在

註:
不管是`inc`或是`dec`操作，只要涉及頻率為`0`的情況的話，我們都不對`0`相對應的集合或是Linked List進行任何新增/刪除的動作，因為0代表這元素不存在在我們的資料結構內