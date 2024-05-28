# Intuition

no two adjacent elements are selected. => House robber
brute force挺簡單的, 就持續在每個queries上去做house robber就好, 這樣時間上會是個 O(n^2) 的解法 => TLE

所以我們要改善的重點應該要想如何高效更新house robber
但當時競賽在這邊就卡死了

這題需要的, 其實是需要轉換思維, 用另種方式去解house robber

`nums = [i X X X X X k][k+1 X X X X X X j]`

對於一段nums[i:j], 我們可以利用divide & conquer的方式先想成: **dp[i][j] = dp[i][k] + dp[k+1][j]**
但為了符合**相鄰兩元素不可同時取**, 所以對於[i:k], [k+1:j]這兩段區間, 我們必須考慮這條件, 再分成

我們每個小區間的首尾是取或不取的排列組合
```
nums = [i X X X X X k]  [k+1 X X X X X X j]
       take        take n-take          take
       take       n-take take           take
       take       n-take n-take         take

       n-take      take n-take          take
       n-take      n-take take          take
       n-take      n-take n-take        take
       
       take        take n-take          n-take
       ...
       n-take      take n-take          n-take
       ...
```

以dp形式來看的話我們分成四種組合, 以0表示沒取, 1表示有取的話, 寫成dp00[i][j], dp01[i][j], dp10[i][j] 跟 dp11[i][j]
分別表示nums[i], nums[j]是取還是不取的dp值

狀態轉移則類似, 一並將小區間的首尾考慮進去, 從各組合中取最大即可

dp00[i][j] = max(
    dp00[i][k] + d00[k+1][j]
    dp00[i][k] + d10[k+1][j]
    dp01[i][k] + d00[k+1][j]
)

dp01[i][j] = max(
    dp00[i][k] + d01[k+1][j]
    dp01[i][k] + d01[k+1][j]
    dp00[i][k] + d11[k+1][j]
)

dp10[i][j] = max(
    dp10[i][k] + d00[k+1][j]
    dp11[i][k] + d00[k+1][j]
    dp10[i][k] + d10[k+1][j]
)

dp11[i][j] = max(
    dp10[i][k] + d01[k+1][j]
    dp11[i][k] + d01[k+1][j]
    dp10[i][k] + d11[k+1][j]
)

這樣divide & conquer到最後就會出現base case:

1. dp00[i][i] = 0
2. dp11[i][i] = nums[i]
3. dp10[i][i] = dp01[i][i] => invalid state => 由於我們是取max(), 所以賦值-inf

而這個divide&conquer的過程其實與segment tree相當類似, 所以可以轉成segment tree的形式來維護dp值
這樣在更新nums[i] = queries[i][1]時, 能以log(n)來更新
在求[0:n-1]區間的最大dp值, 也可以利用segment tree性質去求

另外這邊由於位置很重要, 子節點分別的位置對應:
00 = left string 00 + right string 00
00 = left string 01 + right string 00
00 = left string 00 + right string 10

所以segment tree不適合用iterative的形式, 不然我們在單點更新上會不知道哪個是左節點, 那個是右節點

```py
class SegmentTree():
    def __init__(self, A, op=max):
        n = len(A)
        
        # [dp00, dp01, dp10, dp11]
        self.st = st = ([[0]*4 for _ in range(n)] + [[0,-inf,-inf,num] for i, num in enumerate(A)])
        for i in range(n-1, 0, -1):
            if i%2 == 0:
                # dp00
                st[i][0] = op(
                    st[i<<1][0] + st[i<<1|1][0], # 00 = 00+00
                    st[i<<1][1] + st[i<<1|1][0], # 00 = 01+00
                    st[i<<1][0] + st[i<<1|1][2], # 00 = 00+10
                )
                
                # dp01
                st[i][1] = op(
                    st[i<<1][0] + st[i<<1|1][1], # 01 = 00+01
                    st[i<<1][1] + st[i<<1|1][1], # 01 = 01+01
                    st[i<<1][0] + st[i<<1|1][3], # 01 = 00+11
                )

                # dp10
                st[i][2] = op(
                    st[i<<1][2] + st[i<<1|1][0], # 10 = 10+00
                    st[i<<1][2] + st[i<<1|1][2], # 10 = 10+10
                    st[i<<1][3] + st[i<<1|1][0], # 10 = 11+00
                )

                # dp11
                st[i][3] = op(
                    st[i<<1][2] + st[i<<1|1][1], # 11 = 10+01
                    st[i<<1][2] + st[i<<1|1][3], # 11 = 10+11
                    st[i<<1][3] + st[i<<1|1][1], # 11 = 11+01
                )
            else:
                # dp00
                st[i][0] = op(
                    st[i<<1|1][0] + st[i<<1][0], # 00 = 00+00
                    st[i<<1|1][1] + st[i<<1][0], # 00 = 01+00
                    st[i<<1|1][0] + st[i<<1][2], # 00 = 00+10
                )
                
                # dp01
                st[i][1] = op(
                    st[i<<1|1][0] + st[i<<1][1], # 01 = 00+01
                    st[i<<1|1][1] + st[i<<1][1], # 01 = 01+01
                    st[i<<1|1][0] + st[i<<1][3], # 01 = 00+11
                )

                # dp10
                st[i][2] = op(
                    st[i<<1|1][2] + st[i<<1][0], # 10 = 10+00
                    st[i<<1|1][2] + st[i<<1][2], # 10 = 10+10
                    st[i<<1|1][3] + st[i<<1][0], # 10 = 11+00
                )

                # dp11
                st[i][3] = op(
                    st[i<<1|1][2] + st[i<<1][1], # 11 = 10+01
                    st[i<<1|1][2] + st[i<<1][3], # 11 = 10+11
                    st[i<<1|1][3] + st[i<<1][1], # 11 = 11+01
                )
            

        self.op = op
        self.n = n

    def __getitem__(self, i):
        return self.st[i+self.n]

    def __setitem__(self, i, v):le
        st, op, n = self.st, self.op, self.n
        i += n
        st[i][0] = 0
        st[i][3] = v # dp11[i] = v

        # ! ISSUE: st[i]是左? 是右?
        # 我們無從判斷st[i]跟st[i^1]哪個是左哪個是右邊, 即使i%2==0, 偶數並不代表一定是左節點, 他可能是從兩個右節點組合而來的substr
        # 無法很好地更新segment tree
        # 
        # while i: => WRONG!!!
        #     # dp00
        #     st[i>>1][0] = op(
        #         st[i][0] + st[i^1][0], # 00 = 00+00
        #         st[i][1] + st[i^1][0], # 00 = 01+00
        #         st[i][0] + st[i^1][2], # 00 = 00+10
        #     )
            
        #     # dp01
        #     st[i>>1][1] = op(
        #         st[i][0] + st[i^1][1], # 01 = 00+01
        #         st[i][1] + st[i^1][1], # 01 = 01+01
        #         st[i][0] + st[i^1][3], # 01 = 00+11
        #     )

        #     # dp10
        #     st[i>>1][2] = op(
        #         st[i][2] + st[i^1][0], # 10 = 10+00
        #         st[i][2] + st[i^1][2], # 10 = 10+10
        #         st[i][3] + st[i^1][0], # 10 = 11+00
        #     )

        #     # dp11
        #     st[i>>1][3] = op(
        #         st[i][2] + st[i^1][1], # 11 = 10+01
        #         st[i][2] + st[i^1][3], # 11 = 10+11
        #         st[i][3] + st[i^1][1], # 11 = 11+01
        #     )
            
        #     i >>= 1
```

所以這邊我們就用tree的形式

```py
class Node:
    def __init__(self, l, r) -> None:
        self.l, self.r = l, r
        self.left = self.right = None
        self.info = [0,0,0,0] # [dp00, dp01, dp10, dp11]

class SegmentTree:
    def __init__(self, l: int, r: int, nums: int): # init range [l,r] with nums
        def init_tree(l, r, nums):
            node = Node(l, r)
            if l == r:
                node.info = [0, -inf, -inf, nums[l]]
                return node
            
            mid = (l+r)//2
            if node.left == None:
                node.left = init_tree(l, mid, nums)
                node.right = init_tree(mid+1, r, nums)

                node.info[0] = max(
                    node.left.info[0] + node.right.info[0], # 00 = 00+00
                    node.left.info[1] + node.right.info[0], # 00 = 01+00
                    node.left.info[0] + node.right.info[2], # 00 = 00+10
                )
                
                # dp01
                node.info[1] = max(
                    node.left.info[0] + node.right.info[1], # 01 = 00+01
                    node.left.info[1] + node.right.info[1], # 01 = 01+01
                    node.left.info[0] + node.right.info[3], # 01 = 00+11
                )

                # dp10
                node.info[2] = max(
                    node.left.info[2] + node.right.info[0], # 10 = 10+00
                    node.left.info[2] + node.right.info[2], # 10 = 10+10
                    node.left.info[3] + node.right.info[0], # 10 = 11+00
                )

                # dp11
                node.info[3] = max(
                    node.left.info[2] + node.right.info[1], # 11 = 10+01
                    node.left.info[2] + node.right.info[3], # 11 = 10+11
                    node.left.info[3] + node.right.info[1], # 11 = 11+01
                )
            return node
        self.root = init_tree(l, r, nums)

    def update(self, idx: int, val: int) -> None:
        def _update(node, idx, val):
            if idx < node.l or idx  > node.r: return # not covered by [l,r]

            if idx <= node.l and node.r <= idx:
                node.info[3] = val
                node.info[0]
                return
            
            if node.left:
                _update(node.left, idx, val)
                _update(node.right, idx, val)
                
                node.info[0] = max(
                    node.left.info[0] + node.right.info[0], # 00 = 00+00
                    node.left.info[1] + node.right.info[0], # 00 = 01+00
                    node.left.info[0] + node.right.info[2], # 00 = 00+10
                )
                
                # dp01
                node.info[1] = max(
                    node.left.info[0] + node.right.info[1], # 01 = 00+01
                    node.left.info[1] + node.right.info[1], # 01 = 01+01
                    node.left.info[0] + node.right.info[3], # 01 = 00+11
                )

                # dp10
                node.info[2] = max(
                    node.left.info[2] + node.right.info[0], # 10 = 10+00
                    node.left.info[2] + node.right.info[2], # 10 = 10+10
                    node.left.info[3] + node.right.info[0], # 10 = 11+00
                )

                # dp11
                node.info[3] = max(
                    node.left.info[2] + node.right.info[1], # 11 = 10+01
                    node.left.info[2] + node.right.info[3], # 11 = 10+11
                    node.left.info[3] + node.right.info[1], # 11 = 11+01
                )

        return _update(self.root, idx, val)
```

那最終答案就是每次更新完去找出整個區間的最佳值即可

```py
seg = SegmentTree(0, n-1, nums)

res = 0
for i, x in queries:
    seg.update(i, x)
    
    res += max(seg.root.info)
    res %= mod
return res
```