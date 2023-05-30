# Intuition - Brute Force

遍歷上下邊界(i,j)
這樣矩形的top跟bottom就決定了, 必且此時的高度為`j-i+1`

再來遍歷寬度`k`其中`0 <= k < n`
所以我們會得到由(i,j)與寬度k組成的任意矩形

ex.
```
 [1,0,1]
 [1,1,0] i
 [1,1,0] j
```
ex. i=1, j=2, k = 1:
```
 [1,0,1]
 [{1},1,0]
 [{1},1,0]
```

ex. i=1, j=2, k=2
```
 [1,0,1]
 [{1,1},0]
 [{1,1},0]
```

但由於限制值必須都為1, 所以我們用`height = [0] * n`來紀錄高度
如果height[k] == j-i+1, 代表以column來看是個合法的矩形
再來就數在i到j的段區間內有多少個高度為h的合法矩形

這邊先想一下如果是一維矩陣該怎麼找出值都為1的submatrix

```
1 1 1 0 1 1 0 1
i=0, 1個submatrix
i=1, 再多2個submatrx. (自身以及長度為2的submatrix)
i=2, 再多三個submatrix, (自身 + 長度為2 + 長度為3)
i=3, 0 submatrix
...
```

```py
res = length = 0
for i in range(len(arr)):
    if arr[i] == 0:
        length = 0
    else:
        length += 1
    res += length
return res
```

所以延伸成2-D array, 相當於在鎖定矩形的上下邊界`i`, `j`後計寬度算0到n這段有多少高度為h的合法矩形
- 如果`height[k] != h`, 代表無法組成一個合法矩陣
- 如果`height[k] == h`, 代表這一整個column可以組成一層合法矩陣疊加在當前2-D array上. cnt += width

```py
h = j-i+1 # height
cnt = width = 0
for k in range(n):
    if height[k] != h:
        width = 0
    else:
        width += 1
    cnt += width
res += cnt
```

time complexity: $O(M*M*N)$

# Better Solution - Monostack

將整個matrix想成histogram:
```
  * * *
  * * * * * *
* * * * * * *
            j
```

我們high level的目的是計算histogram內有多少合法矩形
`height[j] = 2`代表在`j-th column`這位置的histogram高度為2 (有連續兩個1)
然後再透過mono-stack找出prevSmaller的index位置

```py
heights = [0] * n
res = 0
for i in range(m):
    for j in range(n):
        if mat[i][j] == 0:
            heights[j] = 0
        else:
            heights[j] += 1

    res += histogram(heights)
```

對於高度為height[j]的矩形的, 在[prev_smaller_idx:i]這段區間內總共有這麼多個:
``py
counter[i] += arr[i] * (i-prev_smaller_idx)
```

ex. i = 3 -> prev_smaller_idx=0, height[i] = 2
這樣這段範圍內高度為2的矩形總共有3*2六個

```
  * * *
* * * *
0 1 2 3 = i

*   *   *   **   **   ***
* + * + * + ** + ** + *** = 6

高度為arr[prev_smaller_idx]的矩形從prev_smaller_idx到i位置也有

如果我們用一個長度為n的array `total` 來紀錄的話
arr[prev_smaller_idx] * (i+1)個 = total[prev_smaller_idx]

total[i] = total[prev_smaller_idx] + arr[i] * (i-prev_smaller_idx)
```

原解答[在這](https://leetcode.com/problems/count-submatrices-with-all-ones/solutions/720265/java-detailed-explanation-from-o-mnm-to-o-mn-by-using-stack/)