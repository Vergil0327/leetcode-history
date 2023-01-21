# Intuition

透過max heap每次都挑profit最大的來查看，再確認capital夠不夠
- 如果夠就做
- 不夠就先放在一旁queue著，繼續往下一個找，最後記得再加回到max heap裡

# Complexity

- time complexity
$$O(k * (nlogn + n + nlogn))$$

- space complexity

$$O(n)$$

但會發現我們這樣最壞情況必須必須反覆搜索到最後，然後再把整個queue重新加回去
這樣整個遍歷一遍，其實就失去了max heap的作用

因此我們可以再想一下，是不是先從capital著手，然後再透過max heap找最大max profit比較好

# Intuition2

首先我們將全部projects以capital排序，我們把我們能做的projects全部丟到max heap然後挑最大的做

做完後我們自身的capital就增加了，我們可以繼續移動index繼續往後把擴大資本後能做的projects丟到max heap裡，丟完後一樣找最大收益的project作

如此一來會發現，其實我們在搜索能做的project時:
- index都是持續往後找的，是O(n)的搜索，而加進max heap的操作為logn
- 而一開始對全部projects排序是O(nlogn)
- 找最大收益project是log(n)，找k次則為klogn

因此最終為O(knlogn)

# Complexity

- time complexity

$$O(k(nlogn + logn))$$

- space complexity

$$O(n)$$