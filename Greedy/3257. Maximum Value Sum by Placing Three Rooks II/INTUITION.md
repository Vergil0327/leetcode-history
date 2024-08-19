# Intuition

[3256. Maximum Value Sum by Placing Three Rooks I](https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/)的follow-up

從leecode 3256知道我們每一row只需要top 3, 就足夠我們用三次O(m*3)循環去進行brute force找出答案
但現在board的數據規模變大, 該怎辦?

延續3256, 我們可以找出每row的top 3:

```py
best3_in_rows = [nlargest(3, [(board[i][j], i, j) for j in range(n)]) for i in range(m)]
```

那同樣概念, 是不是也能透過找出每column的top 3來縮小規模? 畢竟我們只需要挑出不同在row & column的三個元素即可

```py
best3_in_cols = [nlargest(3, [(board[i][j], i, j) for i in range(m)]) for j in range(n)]
```

那這樣就自然想到把這兩個結合在一起, 去除重複後找出前三大元素

```py
arr = list(set(list(chain(*best3_in_rows)) + list(chain(*best3_in_cols))))

res = -3 * 10**9 - 1
for i in range(len(arr)):
    val1, r1, c1 = arr[i]
    for j in range(i+1, len(arr)):
        val2, r2, c2 = arr[j]
        if r2 == r1 or c2 == c1: continue
        for k in range(j+1, len(arr)):
            val3, r3, c3 = arr[k]
            if r3 == r1 or r3 == r2 or c3 == c1 or c3 == c2: continue
            res = max(res, val1+val2+val3)

return res
```

可惜仍TLE (830 / 842 testcases passed)

這時再思考一下能不能再進一步篩選, 這時往greedy想
怎樣的board[i][j]會是我們的首選? => **在row跟col兩方面都最大的值**
如果我們挑`board[i][j]`, 但相同row上有個更大的值`board[i][j']`, 那在同樣block掉row-i的情況下我們肯定挑`board[i][j']`

所以我們再將`best3_in_rows`跟`best3_in_cols`交集在一起
然後再從中找出top-3

```py
arr = list(set(chain(*best3_in_rows)) & set(chain(*best3_in_cols)))
```

結果還是TLE, 卡在838 / 842 testcases passed

再來要縮小規模, 就比較考驗邏輯思維了

假設我們最佳解挑了`board[i][j]`, 那麼根據我們的`best3_in_rows`及`best3_in_cols`
最多會在`row-i`跟`col-j` block掉額外4個元素 (因為我們每row, col都取top3)

所以這時如果我們在選第二個最佳解`board[i'][j']`, 那最壞的可能性又會在`row-i'`跟`col-j'`排除掉額外四個元素

這時已經從`best3_in_rows`及`best3_in_cols`總共用掉**10**個元素了

所以如果要能挑出三個最佳解的元素的話, 我們至少需要挑出**11**個元素
因此我們只需要從`arr`裡取出`nlargest(11, arr)`然後再brute force即可

```py
class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        best3_in_rows = [nlargest(3, [(board[i][j], i, j) for j in range(n)]) for i in range(m)]
        best3_in_cols = [nlargest(3, [(board[i][j], i, j) for i in range(m)]) for j in range(n)]

        arr = list(set(chain(*best3_in_rows)) & set(chain(*best3_in_cols)))
        arr = nlargest(11, arr)
        
        res = -3 * 10**9 - 1
        for i in range(len(arr)):
            val1, r1, c1 = arr[i]
            for j in range(i+1, len(arr)):
                val2, r2, c2 = arr[j]
                if r2 == r1 or c2 == c1: continue
                for k in range(j+1, len(arr)):
                    val3, r3, c3 = arr[k]
                    if r3 == r1 or r3 == r2 or c3 == c1 or c3 == c2: continue
                    res = max(res, val1+val2+val3)

        return res
```
