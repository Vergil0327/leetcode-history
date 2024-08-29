# Intuition

由於我們要刪除的剛好是**中間**節點
所以我們可以用slow, fast pointers來找出中間節點並刪除

如下圖所示, 透過`while fast and fast.next`這條件去移動兩個快慢指針
最終`slow`指針就會剛好落在中間節點
所以我們在額外存一個prev節點去移除即可

```
X - X - X
    s
        f

X - X - X - X
        s
               f
```

edge case: 如果整個linked list只有一個節點, 那就是返回None