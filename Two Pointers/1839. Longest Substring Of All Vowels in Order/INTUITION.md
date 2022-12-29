# Two Pointers

## Intuition

因為'a','e', 'i', 'o', 'u'必須是有序的，所有的'a'都必須'e'之前，所有的'e'也必須在'i'之前，因此我們只要遍歷`word`找出'a'的位置作為起始點`l`，然後盡可能地依字母順序移動`r` pointer，並記錄每個合法的[l,r]區間，找出最長長度即可

'aaaeeeiooouuuu'
l r->->-> 不停移動`r`

'aaaeeeooouuuu'
l r->->  萬一途中缺少任一字母而無法組成合法的aeiou時，便停止，繼續往下找

## Complexity

- time complexity

$$O(n)$$

- space complexity

$$O(1)$$