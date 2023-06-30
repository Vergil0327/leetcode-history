# Intuition

首先應該是由小的subtree到大的subtree來看
如果左右兩邊都是合法BST並且加入root node後依然是BST, 那麼我們就能merge在一塊視作一個大的BST
所以應該要從**post-order**來下手

```
    root
left    right
```

那如果要判斷當前這個是不是合法BST的話
假設left, right這兩個subtree都已經是合法BST了, 那麼對於root來說
root必須滿足: `max(left) < root < min(right)`

所以我們可能除了sum還需要紀錄min, max的訊息來協助我們判斷是不是能merge成一個大的BST
如果可以, 那我們就能更新max_sum

如果不滿足, 那麼也沒有辦法再往上組成合法BST
所以我們返回`sum=-inf`來標記這部分subtree無法組成BST
之後就在post-order位置持續更新這三個變數即可

另外base case則是:
- 對於任何一個leaf node, 他都是合法的BST, 所以我們可以對每個leaf node進行更新
- 並且對於`None`節點, 我們返回sum=0, minLeft=inf, maxRight=-inf, 這樣以leaf node來看也滿足 maxRight < leaf_node.val < minLeft