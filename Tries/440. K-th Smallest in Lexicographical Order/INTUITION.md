# Intuition

這題不用造出Trie，但必須要有Trie的圖像來幫助計算

強烈建議配合[這篇](https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/solutions/92242/concise-easy-to-understand-java-5ms-solution-with-explaination/)的圖示

依照字母順序從1~到n的話，依序會是

1, 10, 100, 1000, ...
2, 20, 200, 2000, ...
... n

如果我們有個十進位數字的Trie的話，字母順序排列就是preorder traversal的順序，會依序從1 -> 10 -> 100 -> ...

我們從`curr = 1`開始，如果以`1`開頭所有小於等於`n`的數加總都還是小於steps的話，我們可以直接全部加總上去
然後改從`curr+1 = 2`開始

```
if steps <= k:
    curr += 1
    k -= steps
```

但如果以`1`開頭的的數且小於等於`n`的數大於`k`的話，那我們只能逐步逼近`k`

例如 第k個數 落在1開頭的數字的話，就不能像上面一樣直接跳到以2開頭
ex.
1 -> 10, k -= 1
10 -> 100, k -= 1 逐步逼近找出第k個

```
if steps > k:
    curr *= 10
    k -= 1
```

**如何計算steps?**

從 curr = 1 開始，必且n1=curr, n2=curr+1
持續查看n1, n2

如果`n2 <= n`的話，代表[n1,n2)這範圍都是<=n的合法步數

ex.
1, 2   -> 1
10, 20 -> 10~19
100, 200 -> skip 100 ~ 199 steps

如果`n2>n`的話，代表我們只能加到[n1, n]這個區間

ex.
1, 2
10, 20
100, n=147, 200 -> over n, only 147-100 steps can go

當 n = 147 的話，n1=100, n2=200，代表我們只能計算到`[100~147]`這個區間