# Intuiion

這題如果用python-SortedList, 那就秒解

但本題正解是利用two heap來巧妙求出第i-th largest element

核心思想是實作兩個heap, 分別是:
1. min heap, 其中裡面item的comparator為: `self.score < other.score or (self.score == other.score and self.name > other.name)`
2. max heap, 其中裡面item的comparator為: `self.score > other.score or (self.score == other.score and self.name < other.name)`

```py
class MinHeapItem:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __lt__(self, other):
        return self.score < other.score or \
               (self.score == other.score and self.name > other.name)

class MaxHeapItem:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __lt__(self, other):
        return self.score > other.score or \
               (self.score == other.score and self.name < other.name)
```

那再來就觀察

我們每當呼叫**get**, 第i-th呼叫就希望得到i-th largest item
所以我們希望的是:
- maxHeap[0]為`i-th largest item` (1-indexed)
- minHeap維護`前i-1大的items` (1-indexed), 其中minHeap[0]為第i大的item

**add**
所以每次加入一個item到minHeap裡, minHeap[0]就會是第i大的元素
再把他加入到maxHeap裡

**get**

第i大的item為`maxHeap[0]`
並把這第i大item重新加回minHeap, 這時minHeap維護的就會是前i+1大的元素
那這樣我們後續呼叫**call**時, 就會持續維護前`i+1`個item, 然後maxHeap就自動找出下一個第`i+1`大的元素
