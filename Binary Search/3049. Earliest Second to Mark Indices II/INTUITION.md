# Intuition

我們可以做的操作有:
- 直接把nums[chaingeIndices[i]]設為0 (zero-out operation)
- mark nums[i] where nums[i] == 0 and i in range [1,n]
- nums[i] -= 1 where i in range [1,n]
- set nums[changeIndicies[j]] = 0 where j is current second

那這問題其實是在問:
能不能找出一個earliest second `x` where x in [1,m], 能讓我們透過changeIndices[:x]將整個nums都轉為0

minimum decision problem => think binary search

- 至少需要len(nums) seconds => (all zero already)
- 至多需要sum(nums) + len(nums) => all -= 1 operation + mark operation
- 我們要在[1,m]之間找出earliest second `x`

如果我們能在`x-1`秒將nums全轉為0 => 那`x`秒肯定也可以
如果我們不能在`x`秒將nums全轉為0 => 那`x+1`秒肯定也不行
具有單調性 => 可以嘗試binary search

框架如下:
由於這題可能要找earliest second in range [1,m]
我們將search space設為[1, m+1], 這樣我們就能判斷假如最後出來答案是`m+1`, 代表此題無解
找search minimum value by binary search整體框架如下:

```py
l, r = 0, m+1
while l < r:
    mid = l + (r-l)//2
    if is_possible(mid):
        r = mid
    else:
        l = mid+1
return l if l <= m else -1
```

那再來就是關鍵的helper func `is_possible`

我們希望透過is_possible檢查當前的`mid`是否可以利用changeIndices[:mid]來將整個nums clear to zero
can we clear nums by changeIndices[:mid]?

首先觀察一下操作, greedy來想:
1. 我們要盡可能地將mark這步放在最後, 讓前面的步驟盡量去將nums[i]轉成0
2. 比起`-=1 operation`, `zero-out operation`更好
    - 因此能用`zero-out`就用, **除非**存在nums[i]只能透過`-=1 operation`歸零, 我們才必須犧牲之前的`zero-out operation`
3. 對於同一個changeIndices[i], `zero-out`這項操作越早用越好, 這樣後續的changeIndices[i]就能拿來進行`-=1`操作將其他的nums[j]歸零
4. 不管是`-=1`或是`zero-out`操作, 後面都必須還留有時間進行`mark`操作

這邊有個trick是, 我們在檢查changeIndices[:mid]能不能clear nums時
我們從後往前遍歷`i where i in [1,mid]`
這樣每經過一秒, 我們就多一步`mark operation`, 這樣我們如果判斷我們要進行`zero-out`操作時, 我們可以很快知道後面存不存在`mark` operation來支持我們這麼做
因為要是後面沒有秒數可以去`mark`, 那麼我們`zero-out`也沒有意義

所以我們由後往前遍歷, 並紀錄當前能用的`mark`操作

```py
mark = 0
for i in range(m-1, -1, -1):
    mark += 1
```

那再來就是zero-out的判斷, 在`i`秒時, 我們能將nums[changeIndices[i]-1] zero-out
就像前面所提的, `zero-out`在第一次遇到changeIndices[i]時就用是最好的
這樣後續再遇到相同的changeIndices[i], 我們能拿來進行`-=1`或`mark`操作

例如 example1: nums=[3,2,3], changeIndices = [1,3,1,2,2,2,3]
優先將nums=[0,2,3]才會是最優解

所以我們先預處理, 找出我們第一次遇到`changeIndices[i]`的秒數`i`位置

```py
# firsts[changeIndices] = sec
firsts = {}
for i in range(m):
    j = changeIndices[i]-1 # 1-indexed to 0-indexed
    if changeIndices[i] not in firsts and nums[j] > 0:
        firsts[j] = i
```

那這樣我們將firsts反一反, 就能知道第`i`秒是不是第一次遇到`changeIndices[i]`
是的話那我們就`zero-out`, 以利後面`-=1`或`mark`

也就是:
```py
# firsts_rev[sec]: i => 當前sec是第一次能對nums[i] zero-out
first_zero_out = {sec:i for i, sec in firsts.items()}
```

但別忘了還有個前提是, 我們在`zero-out`時, 必須保證後續我們還能進行`mark`
這也是我們為什麼從後往前遍歷

難萬一後面我們沒辦法進行`mark`呢?
我們就必須捨棄掉`zero-out` operation, 但不是捨棄當前的
zero-out肯定是用在nums[changeIndices[i]]越大越好
因此我們應該捨去的, 是`nums[changeIndices[i]]`最小的

因此我們可以透過minimum heap, 來讓我們`lazily`聰明地捨去擁有最小nums[changeIndices[i]]的`zero-out` operation

我們**從後往前**遍歷`i` sec
- 如果`i`不在first_zero_out裡, 那代表我們無法對他zero-out, 紀錄`mark`操作`+= 1`
- 如果`i`在first_zero_out裡:
    - 我們把nusm[first_zero_out[i]]放到min heap裡
    - 並同時判斷我們有沒有`mark`操作能支持我們進行`zero out`
        - 如果mark > 0, 那很好, 我們可以耗掉1個mark操作來進行這次的`zero-out`.
            - if mark > 0: mark -= 1
        - 如果mark <= 0, 那代表我們必須替換掉最小的zero-out operation. 並額外騰出一個`mark` operation
            - else: heapq.heappop(pq) and mark += 1

所以整理一下變成:
```py
mark = 0
pq = [] # min heap
for i in range(mid-1, -1, -1):
    if i not in first_zero_out:
        mark += 1
    else:
        heapq.heappush(pq, nums[first_zero_out[i]])
        if mark > 0:
            mark -= 1
        else:
            heapq.heappop(pq)
            mark += 1
```

那最終判斷依據是什麼?

我們要將sum(nums)化為0, 我們透過zero-out消去sum(pq)
化為0後我們要至少有len(nums)個mark operation
而其中我們已經在zero-out的同時進行mark了, 所以還得扣掉len(pq)
所以最終就是: (sum(nums)-sum(pq)) + (len(nums)-len(pq)) 必須 <= mark

此時的這個`mark`可以想成free_operation或許更好, 因為它代表著`-=1`操作以及`mark`
`(sum(nums)-sum(pq)) + (len(nums)-len(pq))`代表扣掉zero-out操作後
能不能透過剩餘的操作數進行`-=1`以及`mark`來將整個nums clear to zero

所以可以表示成:

```py
def is_possible(sec):
    free_op = 0
    pq = [] # min heap
    for i in range(sec-1, -1, -1):
        if i not in first_zero_out:
            free_op += 1
        else:
            heapq.heappush(pq, nums[first_zero_out[i]])
            if free_op > 0:
                free_op -= 1
            else:
                heapq.heappop(pq)
                free_op += 1
    return (sum(nums)-sum(pq)) + (len(nums)-len(pq)) <= free_op
```