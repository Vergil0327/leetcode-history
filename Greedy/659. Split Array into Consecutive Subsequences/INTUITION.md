# Greedy

## Intuition

這題最重要的兩個思想是
1. 如果已存在一個valid consecutive subseq.，能繼續接上就接上

因為假如我們獨自在開一個新的seq.，後面必須有兩個連續的數才行
並且就算存在這兩個連續的數，實際上新開的seq.跟前一個也是連續的

ex. 1,2,3,4
如果我們開創一個1,2,3 seq.，4必須繼續接上，不然就得確保後需有5,6的存在

2. 如果不存在任何的valid consecutive subseq.，那必須確保後續兩個連續數存在才能開創新的seq.

並且題目已由小到大排序，所以每次都往後確認即可
對於每個`num`，就往後確認`num+1`&`num+2`

## Approach

*題目已由小到大排序*

1. 用一個`hashmap`計算每個數出現的次數. `可以使用python的Counter`
2. 再用一個`hashmap`記錄每個seq.所需的tail number.

遍歷整個陣列(數組)時，每次都確認能不能繼續接在某個已存在的seq.之後
如果不行，確認後兩個連續數存不存在
- 存在，開一個新的seq.
- 不存在，那就不可能分出合法的consecutive subsequence，就返回False