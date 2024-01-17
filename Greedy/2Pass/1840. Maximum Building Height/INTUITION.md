# Intuition

n=5, restrictions=[[2,1],[4,1]]

1: 0
2: min(1, x)
3: min(3-1, x)
4: min(1, x)
n: min(n-1, x)

對於不在restrictions內的位置的限制, 相當於: [_id, _id-1]
> see example2, 沒有限制的話到達該位置最多只能是`_id-1`高度

那麼對於i-th building來說:

..., height[i-1], height[i], height[i+1], ...

考慮左邊鄰居的限制的話:
```py
maxHeightL = [0]*n
for _id in range(2, n+1):
    i = _id-1
    maxHeightL[i] = min(restrictions[_id] if _id in restrictions else _id-1, maxHeightL[i-1]+1)
```

考慮右邊鄰居限制的話
```py
maxHeightR = [0]*n
maxHeightR[-1] = min(n-1, restrictions[n] if n in restrictions else n-1)
for _id in range(n-1, 0, -1):
    i = _id-1
    maxHeightR[i] = min(restrictions[_id] if _id in restrictions else _id-1, maxHeightR[i+1]+1)
```

為了方便找尋每個_id的maxHeight, restrictions我們轉成hashmap的形式:

```py
restrictions = {_id: maxHeight for _id, maxHeight in restrictions}
```

所以在同時考慮左右兩邊限制情況下, 我們的i-th building的maxHeight就等於min(maxHeightL[i], maxHeightR[i])
全部遍歷一遍找全局最大即可得到maxHeight over n buildings

```py
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions = {_id: maxHeight for _id, maxHeight in restrictions}

        maxHeightL = [0]*n
        for _id in range(2, n+1):
            i = _id-1
            maxHeightL[i] = min(restrictions[_id] if _id in restrictions else _id-1, maxHeightL[i-1]+1)

        maxHeightR = [0]*n
        maxHeightR[-1] = min(n-1, restrictions[n] if n in restrictions else n-1)
        for _id in range(n-1, 0, -1):
            i = _id-1
            maxHeightR[i] = min(restrictions[_id] if _id in restrictions else _id-1, maxHeightR[i+1]+1)
        
        return max(min(L, R) for L, R in zip(maxHeightL, maxHeightR))
```

這想法事後發現跟經典題目[135. Candy](../135.%20Candy/README.md)很像

但run了一下發現會memory limit exceeded (MLE)
這時看一下constraint應該能很快想到: n最高到10^9個

所以我們應該只考慮restrictions就好


因此我們不該遍歷每個building, 我們遍歷有限制的就好

首先我們先把首尾限制給加進去

```py
restrictions = [[1,0]] + restrictions
restrictions.sort()
if restrictions[-1][0] < n:
    restrictions = restrictions + [[n, n-1]]
```

ex. restrictions = [0,0], ..., [a, ha], [b, hb], ..., [n, n-1]

這時能增加的delta height = b-a

再來一樣先順著考慮右邊鄰居限制:

對於a來說:

**a->b**如果沒限制, `h = ha+(b-a)`
> 但因為有限制, 所以h = min(hb, ha+(b-a))

不過如果[a,b]之間夠遠的話, 我們勢必可以先遞增後遞減來從ha抵達hb => `ha, +1,+1,+1,+1,..., -1,-1,-1,-1, ..., hb`
這時最高點就會出現在中間位置

所以如果**h > hb**, 代表最高點會出現在中間位置, 就像前面講的: 

`ha +1+1+1+1, ..., `maxHeight`, -1-1-1-1, hb`

這時`diff=h-hb`就是多出來的位置, 而這些位置必須拿來放成對的+1,-1才能使得最後h符合hb
所以中間的最高點位置就是: `h = hb + diff/2`

所以寫成程式碼的話就是:
```py
h = ha+(b-a)
if h > hb:
    diff = h-hb
    h = hb + diff//2
```

因此我們先順著考慮右邊鄰居高度, 並直接更新restrictions[i+1][1], 相當於將前面的maxHeightR[i]更新在restrictions[i]上:

```py
m = len(restrictions)
for i in range(m-1):
    a, ha = restrictions[i]
    b, hb = restrictions[i+1]
    
    h = ha + abs(b-a)

    # [a,b]之間夠遠
    if h > hb:
        diff = h-hb
        h = hb + diff//2
    
    restrictions[i+1][1] = min(h, hb)
```

再來考慮左邊鄰居限制 => 把restrictions反著考慮一遍
由於前面已經將restrictions[i]順著右邊鄰居更新過一遍了
這時只要在逆著考慮回來的同時, 找出全局最高height即可

```py
restrictions.reverse()

res = 0
for i in range(m-1):
    a, ha = restrictions[i]
    b, hb = restrictions[i+1]
    
    h = ha + abs(b-a)

    # [a,b]之間夠遠
    if h > hb:
        diff = h-hb
        h = hb + diff//2

    # find maximum valid height
    res = max(res, h)

    restrictions[i+1][1] = min(h, hb)
```

# Complexity

- time complexity: $O(mlogm)$
- space complexity: $O(1)$