# Intuition

- 分別將`node.val < x` 及 `node.val >= x` 儲存在不同陣列或是dummy pointer即可

若是將node分別接在個別dummy pointer的話，必須額外遍歷一次計算有多少個`node < x`
這樣我們才知道何時停下pointer的移動，然後將前半部分的Linked List(val < x)的尾端接到另半部分的Linked List (val >= x)

# Complexity

- time complexity

$$O(n)$$

- space complexity

$$O(n)$$ or $$O(1)$$