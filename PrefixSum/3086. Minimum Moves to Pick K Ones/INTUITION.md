# Intuition

題目敘述:
- pick up index `dylanIdx` from [0,n-1]
- do one of the following action:
    1. select index `j` where `j != dylanIdx` and set nums[j] = 1 => flip 0 into 1 (at most `maxChange` times)
    2. swap two adjacent values. if `1` swap to `dylanIdx`, Dylan get 1 and set 0 to it.

[1,1,0,0,0,1,1,0,0,1], k=3, maxChange=1

0 dylanIdx 0 => two steps to get 1 point (set & swap) => 0 dylanIdx 1, then 0 dylanIdx 0
1 dylanIdx 1 => one swap step to get 1 point => 1 dylanIdx 0 or 0 dylanIdx 1

而我們要找的是**the minimum number of moves to pick exactly k ones**

首先想到的是, 我們的dylanIdx要挑整體上離每個`1`都很近的點, 然後再用**set & swap**取代那些較遠的點

所以我們只需關心那些`1`的index, 但這時要注意的是由於我們可以透過maxChanges來拿分, 所以中心點並不一定是最優的

```py
oneIndices = [i for i, v in enumerate(nums) if v == 1]
n = len(oneIndices)
dylanIdx != n//2 # -> see example 1. nums = [1,1,0,0,0,1,1,0,0,1], k = 3, maxChanges = 1. select 1 as dylanIndex.
```

所以我們先brute force試試, 我們遍歷所有可能位置作為dylanIdx點
再來就延續我們剛剛的想法, 由於 maxChanges + sum(nums) >= k
所以我們就greedily找出那些離最近的點進行操作, 所以我們用min heap存放每個`1`離dylanIdx的距離

再來我們就greedily挑選那最優的選擇:
由於1個`maxChanges`需要**set&swap**兩步驟, 並且題目確保`sum(nums)+maxChanges >= k`, 所以:
1. 如果pq[0]距離`dylanIdx` < 2, 我們就透過swap來得分
2. 如果沒有, 但是`maxChanges > 0`, 那我們就用兩步來得1分, 並且`maxChanges -= 1`
3. 如果以上都沒有, 那代表我們只能乖乖swap那些較遠距離的點, `steps += heapq.heappop(pq)`


edge case: 如果oneIndices為空, 那代表我們只能透過maxChanges來操作, 這時直接返回k*2即可

上述想法得到第一個TLE version O(n^2):

```py
def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
    oneIndices = [i for i, v in enumerate(nums) if v == 1]
    n = len(oneIndices)
    if n == 0: return k*2
    res = inf
    for dylanIdx in range(1, n-1):
        
        pq = [abs(oneIndices[i]-oneIndices[dylanIdx]) for i in range(n) if i != dylanIdx] # distance to dylanIdx for those `1`
        heapq.heapify(pq)

        steps = 0
        ones = 1
        changes = maxChanges
        while ones < k:
            if pq and pq[0] < 2:
                ones += 1
                steps += heapq.heappop(pq)

            elif changes > 0:
                ones += 1
                steps += 2
                changes -= 1

            else:
                ones += 1
                steps += heapq.heappop(pq)


        res = min(res, steps)

    return res
```

這時更進一步想,
扣掉maxChanges, 我們只需要額外**max(1, k-maxChanges)**個點
而能勝過maxChanges的只有那些`distance < 2`的, 也就是`dylanIdx-1`跟`dylanIdx+1`這兩個位置

所以如果我們用`m`代表我們額外需要swap的`1`的數量, m最少1個點dylanIdx, 因此`m = max(1, k-maxChanges)`
最多需要`m+3`個點, 分別是 **dylanIdx-1, dylanIdx, dylanIdx+1**

因此這題就可以轉成我們要找在長度為[m,m+3]的sliding window之中, 找出最小distance to dylan index和

而這時我們已經撇除maxChanges的因素了, 要在這sliding window之中, 找出個dylanIdx並使得每個點到dylanIdx的距離最短
這其實就是leetcode 296. Best Meeting Point, 這dylanIdx的最佳位置其實就是median point(中位數位置)
此時各個點到dylanIdx的距離和會是minimum distance

因此整體框架如下, 其中n=0的情況我們額外處理, n=0代表nums=[0]*n, 代表我們全部都只能用maxChanges來獲得1:

```py
def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
    oneIndices = [i for i, v in enumerate(nums) if v == 1]
    n = len(oneIndices)
    if n == 0: return k*2 # 額外處理
    
    mx = max(1, k-maxChanges)
    res = inf
    for m in range(mx, (mx+3)+1):
        for l in range(n-m+1):
            r = l+m-1

            steps = (k-m)*2 # choose m points for operation2, (k-m) for operation1
            steps += calDist(l, r)

            res = min(res, steps)
    return res
```

但細心一點會發現, 或者fail一次就會看到這個test case: nums=[1,1], k=1, maxChanges=2
(k-m)*2這部分不可以是負數, 所以其實我們的m還需要幾個限制:
1. 最多就n個1, m <= n
2. 我們目標只需要k個1, m <= k

所以我們遍歷的`m`應在這個範圍內: [mx, min(n, k, mx+3)]

至於這個helper func **calDist**, 就得借助剛剛提到的用median point作為中位數來計算了
我們知道`dylanIdx`會是(l+r)//2

```py
# [X X X X X X X X X X X X dylanIdx X X X X X X X X X X X]
#  l                                                    r
def calDist(l, r):
    return sum(abs(oneIndices[dylanIdx]-oneIndices[i]) for i in range(l, r+1))
```

但這樣會是個O(n)的時間複雜度, 搭上主框架整體就會變O(n^2)了
這邊我們得找個更高效的方式去計算這個sliding window的每個點到median point的距離和

[l, dylanIdx-1]: oneIndices[dylanIdx] - oneIndices[i] for i in range(l, dylanIdx)
=> (oneIndices[dylanIdx]-oneIndices[l]) + (oneIndices[dylanIdx]-oneIndices[l+1]) + ... + (oneIndices[dylanIdx]-oneIndices[dylanIdx-1])
=> (dylanIdx-l) * oneIndices[dylanIdx] - (oneIndices[l]+oneIndices[l+1]+ ... +oneIndices[dylanIdx-1])
=> (dylanIdx-l) * oneIndices[dylanIdx] - (presum[dylanIdx-1]-presum[l-1])


[dylanIdx+1, r]: oneIndices[i] - oneIndices[dylanIdx] for i in range(dylanIdx+1, r+1)
=> 同上推導
=> (oneIndices[dylanIdx+1]+ ... + oneIndices[r]) - (r-dylanIdx)*oneIndices[dylanIdx]
=> (presum[r]-presum[dylanIdx]) - (r-dylanIdx)*oneIndices[dylanIdx]

結合兩式子可得:
(dylanIdx-l) * oneIndices[dylanIdx] - (presum[dylanIdx-1]-presum[l-1]) + (presum[r]-presum[dylanIdx]) - (r-dylanIdx)*oneIndices[dylanIdx]
=> (presum[r]-presum[dylanIdx])-(presum[dylanIdx-1]-presum[l-1]) + (dylanIdx-l-r+dylanIdx) * oneIndices[dylanIdx]
=> 小心可能會有越界問題, 所以改成

因此:

```py
presum = list(accumulate(oneIndices))
def calPresum(left, right):
    if left > right: return 0
    return presum[right] - (presum[left - 1] if left-1 >= 0 else 0)

def calDist(l, r):
    dylanIdx = (l+r)//2
    return calPresum(dylanIdx+1, r) - calPresum(l, dylanIdx-1) + (dylanIdx-l-r+dylanIdx) * oneIndices[dylanIdx]
```

time: $O(n)$
space: $O(n)$