# Intuition

這種需要高效更新, 並要計算區間乘積的問題, 首先想到segment tree
- 利用segment tree高效更新nums[queires[0]] = queries[1]
- 利用segment tree計算區間[queries[2], n-1]裡有多少合法subarray數目使得`product%k`

但再來就沒頭緒該怎麼做了, 可能會類似這樣

```py
res = []
for idx, val, start, x in queries:
    seg[idx] = val%k
    res.append(seg.query(start, n, x))
return res
```

Here is the solution and explanation from [@Cry Andrich](https://leetcode.com/problems/find-x-value-of-array-ii/solutions/6668800/segment-tree-explanation-python-java-c)

### Counting Prefix Remainders

We need, for each remainder r ∈ [0, k-1], the number of non-empty prefixes of a given segment whose product ≡ r (mod k).
A classic way to support point updates and range prefix-remainder queries is a segment tree where each node stores:

cnt[r] = number of non-empty prefixes in that node's segment whose product ≡ r (mod k)
prod = the product of all elements in that node's segment, reduced mod k

### Merging Two Child Segments

Suppose we have:

- Left child representing segment A, with (cnt_A, prod_A)
- Right child representing segment B, with (cnt_B, prod_B)

A prefix of A‖B (the concatenation) is either:

1. A prefix entirely within A (contributes cnt_A[r] to merged cnt[r]), or
2. All of A followed by a prefix of B. For each remainder r_b in cnt_B, those cnt_B[r_b] prefixes of B become remainder (prod_A x r_b) mod k when prepended by the full product of A.

The merged segment's total product is: prod_A‖B = (prod_A x prod_B) mod k