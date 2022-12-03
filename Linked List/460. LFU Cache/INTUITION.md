### Hashmap + Doubly-Linked List

首先我們觀察一下我們需要哪些資料結構

```
    hashmap.  doubly-linked list
freq1 ->  [key1, key2, key3...]  -> min freq
freq2 ->  [key1, key2, key3...]
freq3 ->  [key1, key2, key3...]


self.min -> used for least ferqeuntly used & remove least used
```

如果要達到`O(1)`查詢的話，我們會需要個`hashmap`來建立**key-value關係**

再來當我們查詢後，我們也要更新frequency，所以也需要另一個`hashmap`來建立**key-frequency關係**

同時我們還必須要建立各個**freqency與其底下所有key的關係**

這部分是為了當capacity不夠時，我們必須從最小freqeuncy的linked list內刪除最少使用的ListNode

這部分就跟LRU很像，我們需要將key以doubly-linked list方式儲存以達到`O(1)`的新增/刪除

```
這邊我們會使用環形linked list
新增從root.next開始新增
這樣環形的尾端(root.prev)就會是最少使用的ListNode
```

而且我們還會需要一個variable來標記目前最小freqeuncy是多少，這樣我們才能快速找出最低frequency的linked list


最後，當我們查詢後，我們也會需要更新使用頻率

同樣地，更新後我們必須將ListNode從舊的freqeuncy鏈上移至新的freqeuncy鏈上

因此我們前面的**key-value關係**應該要存放的是`ListNode`而不是單純的integer value

這樣我們在刪除的時候能快速取得ListNode並刪除
並且在更新frequency後，要將node移動到另個linked list也比較方便

總結:
1. key-value hashmap: {key: value}: {int: ListNode}
2. key-freqency hashmap: {key: frequency}: {int: int}
3. frequency-keys hashmap: {freq: keys}: {int: ListNode}
4. variable to store current minimum frequency: int


**put(key: int, val: int) -> None**

- 如果capacity <= 0:
  edge case, 無法進行任何操作

- 如果key已經存放在`key2val cache`裡:
  1. 更新node value
  2. 更新frequency
  3. 將node從舊的freqeuncy鏈上移除，並移至新的frequency鏈上.
     1. disconnect
     2. insertToFront
     3. 重要! 必須檢查移動後Linked List是否為空(只剩root node），如果是，則必須更新`min`，將其指向目前最低的頻率
        - increment `min` by 1
        - 
- 如果key不存在，代表我們要新增ListNode

  1. 首先看我們capacity夠不夠，滿了的話必須從最少使用的ListNode開始刪除
     1. 藉由`min`變數找到目前最小freqeuncy doubly-linked list
     2. 移除least recently-used node (root.prev)
     3. 並同時從cache中刪除value與freqeuncy紀錄
  2. 創建一個新的ListNode
  3. 建立`key-value`關係，value為ListNode
  4. 建立`key-frequency`關係，freqeuncy為1
  5. 新增ListNode至frequency linked List上
  6. 重要! 更新`min`為1，有新增的話最低頻率必為1

**get(key: int) -> int**

1. 如果key不存在cache裡，返回`-1`
2. 如果存在
   1. 更新頻率
   2. 將ListNode從舊frequency移至新freqeuncy上
3. 重要! 一樣必須檢查更新完後目前的freqeuncy linked list是否為空，是的話必須更新`min`
4. 返回cache value
