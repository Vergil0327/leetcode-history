# Intuition

這題可以用雙序列DP來解，但時間複雜度會是O(MNK)導致TLE
因此我們可以轉換個方式想

我們總共要從`nums1`, `nums2`中找`K`個，那我們就遍歷所有可能來找出組合

ex.
從`nums1`中找1個, `nums2`中找K-1個
從`nums1`中找2個, `nums2`中找K-2個
從`nums1`中找3個, `nums2`中找K-3個
...
從`nums1`中找K-2個, `nums2`中找2個
從`nums1`中找K-1個, `nums2`中找1個

也就是將共`K`個分配給`nums1`跟`nums2`，這樣時間複雜度就會縮至O(K* max(M,N))

那high level的核心程式碼為:

```py
for i in range(K+1):
    if i > len(nums1): continue
    if K-i > len(nums2): continue
    seq1 = findMaxSeq(nums1, i)
    seq2 = findMaxSeq(nums2, K-i)
    curr = merge(seq1, seq2)
    res = max(res, curr)
```

遍歷`K`，分配`i`個給`nums1`，`K-i`給`nums2`，如果`nums1`或`nums2`不夠取就跳過

**子問題1**

那 **findMaxSeq** 該如何處理?

由於我們要找的是一個最大的子序列，因此我們可以維持一個遞減的序列
這時我們可以用單調遞減的Stack來幫助我們

在`nums1`中，維持**至少i個**的情況下，維護一個單調遞減的Stack
在`nums2`中，維持**至少K-i個**的情況下，維護一個單調遞減的Stack

每當遇到一個`num`比Stack[-1]還要大時，在還能夠移除掉stack的情況下就移除
ex. stack = [5,4,3,2], num=6, can removed 3 totally
最後 stack = [5,6,X,X]. (56XX > 5432)
只要當前的`num`比Stack[-1]還大，能移除就盡量移除，因為最終子序列肯定比原本大

並且記住最後單調遞減的Stack的size並不一定是我們所要求的
所以最後從`nums1`返回的序列，size必須限制在`i`個
同樣的從`nums2`返回的size則是`K-i`個

**子問題2**

那 **merge** 部份就單純多了，這部分就相當於 merge K list
我們用two pointers來相互比較，優先挑最大的即可

但有一點要特別注意的是，如果兩個數相等的話該怎辦?
ex. seq1 = [6,8,1,2], seq2 = [6,6,1,2]

如果有當前兩個數 seq1[i] == seq2[j]的話，我們必須持續地往後面比較(iteratively)
當後面有有比較大的數存在時，則優先選擇該序列，因為這樣最終排列比較大

seq1:[6,8,1,2] -> [8,1,2] -> [1,2]
seq2:[6,6,1,2] -> [6,6,1,2] -> ...
挑出來會是 （6,8,...)，才會是最佳解
但如果不持續往後比對的話，有可能會是 (6,6,...)

# Complexity

- time complexity

$$O(K * N)$$

- space complexity

$$O(N)$$