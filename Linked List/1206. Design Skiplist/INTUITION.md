# Intuition

依據題意提示, 我們得利用linked list來搜索num存不存在
而為了達到log(n), 大概得配合array + binary search去想

所以想法是利用array儲存多個head of linked list, 利用binary search找到該區間的linked list後
再去搜索`num`存不存在或是新增/刪除的位置
但實作後會發現個問題就是, 萬一這個array存的head就是我們該刪除的節點該怎辦?
array除了pop以外, 對於中間元素的刪除都是O(n), 那這樣就無法達到log(n)的要求了
而且實際上該怎麼去balance每個linked list長度也是個問題, 不然binary search就沒有意義了

所以當前這想法是有誤的
我們這邊SkipList要想的應該是如圖所示:
1. level1: 一個儲存所有節點的linked list
2. level2: 2倍快進的linked list
3. level3: 4倍快進


那這樣在搜尋方面, 從最上層(level3)開始找, 我們直接看head.next的數值, 如果是空或者是大於target
我們就往下一層, 下層元素會是上層元素的兩倍多, 再去快進查詢`<= target`的節點位置, 以此類推

而在刪除方面也是類似概念去搜索, 只是找到該目標元素後, 必須從該層以及該層之後的該元素都刪除

最複雜就是**新增**, 整個skip list的核心就是每往下一層數量就多一倍
而且仔細看動圖會發現, 他有個coin flip, 這其實是在**新增**這步驟的一個核心概念
```
level4 30
level3 30 -> 50
level2 30 -> 50 -> 70
level1 30 -> 40 -> 50 -> 60 -> 70 -> 90
```

在level1那層, 是所有節點都包含, 再往上到level2那層, 節點數目變50%, 再往上變25%
所以在新增的時候我們可以用一個機率, 在level1時機率是100%, 我們一定新增
然後逐層往上, 機率逐層遞減來決定要不要新增, 透過隨機機率來讓每層達到我們希望的機率分佈
也就是每往上一層, 節點數目就少50%

這樣所有層數的儲存空間會是: N + N/2 + N/4 + ... = 2N = O(n) space

所以我們的基本數據結構ListNode儲存兩個資訊:
1. ListNode.next: 儲存下個節點
2. ListNode.down: 下層節點

那search就很簡單, 我們從首節點開始, 先往右搜尋
由於一開始層數是最稀疏的, 所以會快速往右直到node.val < target
然後到該層盡頭後再往下層繼續找
```py
node = self.head
while node:
    # skip most nodes quickly
    while node.next and node.next.val < target:
        node = node.next
    # current node should be previos node of target
    if node.next and node.next.val == target: return True

    node = node.down
return False
```
如果所有層數遍歷玩都沒找到該節點, 代表該節點不存在

同理, erase也是一樣概念:
我們快速往右找到target node的previous node, 然後利用linked list的特性刪除後
再往下層, 然後一樣往右找到target node的previous node, 直到我們將每層的target node都給刪光

```py
node = self.head
found = False

while node:
    while node.next and node.next.val < num:
        node = node.next
    if node.next and node.next.val == num:
        node.next = node.next.next
        found = True
    
    node = node.down
return found
```

最後的**add**則較為複雜

分為兩大部分, 首先第一部分是找出每一層的previous node

```py
nodes = []
cur = self.head
while cur:
    while cur.next and cur.next.val < num:
        cur = cur.next
    nodes.append(cur)
    cur = cur.down
```

再來第二部分就是我們從最底層開始插入wanted node

首先我們用個變數`should_insert`來代表機率,相當於動圖的coin flip
只有當`should_insert==True`時, 我們才插入節點, 這樣越往上層機率越低, 以達到我們希望的節點數量分佈
然後一開始已經是最下層, 所以`down = None`

再來就開始從最底層往上插入wanted node
我們持續從`nodes`裡找出該層的previous node, 然後將wanted node插入到previsou_node.next
並更新down = previous_node.next, 這樣我們再往上層的時候, down才會是對的
該層插入完後, 我們就進行一次擲硬幣(coin flip)的動作, 透過隨機機率來看我們往上一層後還要不要插入
等到全部層數都結束後, 如果`should_insert`仍然為**True**
代表我們需要新增一層, 此時我們更新我們的首節點為: `self.head = ListNode(-1, None, self.head)`

```py
should_insert = True
down = None
while should_insert and nodes:
    node = nodes.pop()
    node.next = ListNode(num, node.next, down)
    down = node.next
    should_insert = random.getrandbits(1) == 0 # coin flip, 判斷下一層還該不該插入該節點

if should_insert:
    self.head = ListNode(-1, None, self.head)
```