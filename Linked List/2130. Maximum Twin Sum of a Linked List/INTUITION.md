# Intuition

這題可以很直覺的想到用個array存起來, 然後用two pointers從兩端往回計算twin sum
或者是先算出總共的`n`是多少
然後把一半先reverse, 然後在同步移動兩段的pointer計算twin sum

但這題有個精妙的解法是

- 我們用slow跟fast pointer來移動. 當fast走到底時, slow會剛好是後半段linked list的head

```
X X X X X X X X
        s ->
                f->
```

- 所以我們在移動的同時, 我們可以同步reverse前半段linked list. 也就是隨著slow pointer來翻轉

```
X<-X<-X<-X  X->X->X->X
       prev s          f

slow, fast = head, head
prev = None
while fast and fast.next:
    fast = fast.next.next
    
    # reverse
    nxt = slow.next
    slow.next = prev
    prev, slow = slow, nxt
```

- 再來我們就從兩段linked list的head開始, 也就是`prev`和`slow`, 移動兩pointer來計算twin sum

```
X<-X<-X<-X  X->X->X->X
       <-p  s->

res = 0
while slow and prev:
    res = max(res, slow.val + prev.val)
    slow, prev = slow.next, prev.next
```