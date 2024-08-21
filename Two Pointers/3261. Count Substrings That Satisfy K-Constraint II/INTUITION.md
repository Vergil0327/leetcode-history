# Intuition

直覺做法是O(n^2) solution => 但數據規模不允許, 會TLE

```py
def sliding_window(s):
    n = len(s)

    res = 0

    l = r = 0
    zero = one = 0
    while r < n:
        zero += int(s[r] == "0")
        one += int(s[r] == "1")
        r += 1

        while l < r and zero > k and one > k:
            zero -= int(s[l] == "0")
            one -= int(s[l] == "1")
            l += 1

        res += r-l # 對於左端點`l`來說, 有r-l個右端點能組成合法的substring
        
    return res

ans = []
for l, r in queries:
    ans.append(sliding_window(s[l:r+1]))
return ans
```

從數據規模來看, 每個queries[i]只允許O(1)或O(logn)時間來處理

但新增test case後, segment tree的O(queries.length * logn)解法也會TLE了
> 626 / 627 testcases passed

```py
class Node:
    def __init__(self, l, r) -> None:
        self.l, self.r = l, r
        self.left = self.right = None
        self.info = self.lazy_tag = self.lazy_delta = 0 

class LazySegmentTreeSumIncreaseDelta:
    def __init__(self, l: int, r: int, val: int): # init range [l,r] with val
        def init_tree(l, r, val):
            node = Node(l, r)
            if l == r:
                node.info = val
                return node
            
            mid = (l+r)//2
            if node.left == None:
                node.left = init_tree(l, mid, val)
                node.right = init_tree(mid+1, r, val)
                node.info = node.left.info + node.right.info
            return node
        self.root = init_tree(l, r, val)

    # propagation lazy tag and value from parent to child nodes
    def pushDown(self, node):
        if node.lazy_tag == 1 and node.left:
            node.left.info += node.lazy_delta * (node.left.r - node.left.l + 1)
            node.right.info += node.lazy_delta * (node.right.r - node.right.l + 1)

            node.left.lazy_tag = 1
            node.left.lazy_delta += node.lazy_delta
            
            node.right.lazy_tag = 1
            node.right.lazy_delta += node.lazy_delta
            node.lazy_tag = node.lazy_delta = 0

    def updateRange(self, l: int, r: int, val: int) -> None:
        def update(node, l, r, val):
            if r < node.l or l  > node.r: return # not covered by [l,r]

            if l <= node.l and node.r <= r:
                node.info += val * (node.r-node.l+1)
                node.lazy_tag = 1
                node.lazy_delta += val
                return
            
            if node.left:
                self.pushDown(node)
                update(node.left, l, r, val)
                update(node.right, l, r, val)
                node.info = sum([node.left.info, node.right.info])

        return update(self.root, l, r, val)

    def queryRange(self, l: int, r: int) -> int:
        def query(node, l, r):
            if r < node.l or l > node.r: return 0

            if l <= node.l and node.r <= r:
                return node.info
            
            if node.left:
                self.pushDown(node)
                res = sum([query(node.left, l, r), query(node.right, l, r)])
                node.info = sum([node.left.info, node.right.info])
                return res
            
            return node.info # should not reach here
        return query(self.root, l, r)


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:        
        n = len(s)

        right = [-1]*n # valid right boundary of i, s[i:right[i]+1] is valid substring
        count0 = count1 = j = 0
        for i in range(n):
            while j < n and (count0+int(s[j]== "0") <= k or count1+int(s[j]=="1") <= k):
                count0 += int(s[j]== "0")
                count1 += int(s[j]== "1")
                j += 1
            right[i] = j-1

            count0 -= int(s[i] == "0")
            count1 -= int(s[i] == "1")

        
        for i in range(len(queries)):
            queries[i].append(i)
        queries.sort(reverse=True)

        root = LazySegmentTreeSumIncreaseDelta(0, n-1, 0)
        res = [0] * len(queries)
        i = n-1
        for l, r, idx in queries:
            while i >= l:
                root.updateRange(i, right[i], 1)
                i -= 1
            res[idx] = root.queryRange(l, r)
        return res
```

所以這題希望的解法為O(n)

對於一段substring s[l:r]來說:

- 對於左端點`l`, 如果他的最遠的合法右端點為`m`, 那麼對於右端點`min(m,r)`來說[l, min(m, r)]這範圍都可以作為左端點形成合法k-constraint substr
  - count = (1 + size) * size //2 where size is `min(m, r)-l+1`

```
l X X X X X m X X X X r
```

- 那s[min(m,r)+1:r]這段呢? 我們從右端點來看, 並假設m < r, `m`的左邊這段[l:m]已經都計算過, 再來就看[m+1:r]這段作為右端點時, 有多少左端點位於[l,r]範圍內形成合法k-constraint substr
    - 透過right_to_left[rr] where rr in [m+1,r] range, 我們能知道[m+1, r]這範圍的每個點作為右端點時, 可以跟各自的左端點形成多少合法substr
      - valid_substr = sum(rr-right_to_left[rr]+1 for rr in range(m+1, r+1))
      - 而這個區間和可以預先計算prefix sum, 所以valid_substr = presum[r] - presum[m]

```
l X X X X X m X X X X r
```

兩種情況加總後, 即為[l,r]這範圍內的所有k-constraint substr
因為對於右端點來說, 合法最左端點可能落在[l,r]範圍內, 也可能超出l

1. 第一種情況, 計算了所有[l,min(m, r)]作為左端點, 右端點座落於min(m, r)的k-constraint substr
2. 第二種情況, 則再補上 計算所有右端點座落於[min(m, r)+1,r]的k-constarint substr, 這時左端點勢必會落在[l,r]之間, 因為第一種情況已經考慮右端點為min(m,r)的情況下的**最遠**合法左端點`l`