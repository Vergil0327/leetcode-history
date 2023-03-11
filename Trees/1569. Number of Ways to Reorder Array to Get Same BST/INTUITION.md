# Intuition

只要給定一個序列`nums`，必定能產生唯一一種BST

產生方式如下
```py
class TreeNode
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def insert(root, v):
    if v < root.val:
        if not root.left:
            root.left = TreeNode(v)
            return
        insert(root.left, v)
    else:
        if not root.right:
            root.right = TreeNode(v)
            return
        insert(root.right, v)

root = TreeNode(nums[0])
for num in nums[1:]:
    insert(root, num)
```

那對於一個BST來說, see example2
```
nums = [3,4,5,1,2]
    3
  1   4
   2   5
```
左子樹為[1,2], 右子樹為[4,5]
對於該ＢＳＴ來說，合法的序列為
只要左子樹序列跟右子樹序列在合併的時候相對位置不變
即可產生相同的BST
[1,2,4,5]
[1,4,2,5]
...
也就是說我們要求的可能組合可以轉化成這個問題
*How many number of ways to interleave two ordered sequences*
兩個序列interleave的結果都是合法的解

所以對於
left = [....], len = m
right = [.....], len = n
interleave(left, right) = [.....] => 其實就是在m+n個位置裡，任取m個位置，取完後n也就確定了
所以是Cm取n, 求組合數的問題

所以如果左子樹有 m 個節點, 右子樹有 n 個節點
他們的組合結果就有 C(m+n, m) 個

那如果左子樹本身有 `x` 個組合, 右子樹有`y`個組合
左子樹的`x`個組合中的任一種序列形式都可以跟右子數的`y`個組合中任一搭配
所以一棵樹的總共可能組合為 `x * y * C(m+n, m)`

```py
def dfs(nums)
    root = nums[0]
    nums = nums[1:]

    left, right = [], []
    for num in nums[1:]:
        if num < root:
            left.append(num)
        else:
            right.append(num)

    m, n = len(left), len(right)
    x = dfs(left)
    y = dfs(right)

    return x * y * C(m+n, m)
```

那遞歸的base case該如何處理?
當子數的節點個數**小於3**時 (只有0, 1, 2個), 可能的序列組合只可能是`1`

最後求出的全部組合數，扣掉題目本身的組合即為答案`dfs(nums)-1`

**helper function Cmn**

C m 取 n = m! / n! / (m-n)!
但如果數值很大又要取MOD的話，除法並沒有任何取餘數的特性
因此我們可以用另一種組合數的遞歸表達式來計算
`C(m, n) = C(m-1, n-1) + C(m-1, n)`

他的意思是，C m 取 n 就相當於 在m個數內挑取n個時，**一定包含任意元素x**加上**一定不包含任意元素x的組合**
- 一定包含元素x就代表是: C(m-1, n-1) (有一個已經確定是元素x)
- 一定不包含元素x則為: C(m-1, n) (m個裡面剔除掉元素x)

**Base Case**
1. C(m, 0) = 1
2. C(m, 1) = m
3. 另外C m 取 n的個數跟 C m 取 (m-n)的組合數是相同的，因為挑出n後，剩下的m-n也就確定沒挑到了
所以 `C(m, n) = C(m, m-n) if n > m-n`
這樣我們能確保m比n大, 一定會走到前面兩個base case而非m先為0

