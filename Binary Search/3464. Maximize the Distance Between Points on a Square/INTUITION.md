# Intuition

we want to find the maximum possible minimum Manhattan distance between the selected k points
whenever see maximum possible minimum ... => try binary search to guess answer first

```py
l, r = 0, k * 10**9
while l < r:
    mid = r - (r-l)//2
    if check(mid):
        l = mid
    else:
        r = mid-1
return l
```

now problem turn into find a way to check whether we can select k points with minimum Manhattan distance at least mid

為了方便判斷每個點跟點之間的距離, 我們把矩形四個邊攤開成一個一維矩陣
例如順時鐘方向: left axis -> top axis -> right axis -> bottom axis
把點歸類到這幾個軸上後我們**排個序**
那麼我們就能配合binary search去猜測minimum distance, 然後試著greedily去找出k個點

# Approach

首先先歸類每個點到四個軸上

```py
# map boundary points (x,y) to 4 axis
axis = [[], [], [], []] # Left, Top, Right, Bottom
for x, y in points:
    if x == 0 and y != 0:
        axis[0].append((x,y))
    elif x != 0 and y == side:
        axis[1].append((x,y))
    elif x == side and y != side:
        axis[2].append((x,y))
    else:
        axis[3].append((x,y))

# Sort points in each line (Right and Bottom lines are
# sorted in reverse to sort all points in clockwise dir)
axis[0].sort()
axis[1].sort()
axis[2].sort(reverse=True)
axis[3].sort(reverse=True)
extended_axis = [*axis[0],*axis[1],*axis[2],*axis[3]] # Recombine points
```

再來我們的bianry search主框架:

```py
l, r = 0, 2 * side
while l < r:
    mid = r - (r-l)//2
    if check(mid):
        l = mid
    else:
        r = mid-1
return l
```

那剩下就是如何實作`check`這個helper function

主要概念就是Greedy!, 我們遍歷整個extended_axis (由四個軸攤開成一維矩陣), 然後一旦當前點與前個path末端點距離符合當前猜測的minimum distance `mid`, 我們就試著將當前點接在前個path後面, 然後試著更新

1. 首先我們將從extended_axis[0]開始做為起點, 然後開始遍歷extended_axis[1:]並持續加入到隊列(deque)裡
2. 一旦我們當前(x,y)與隊列的頭的距離`>= d`, 我們就試著將(x,y)接在後面看看
    - 如果接在後面後能更新當前最大path size, 那就更新
    - 直到沒有合適的點為止, 繼續遍歷下個點
3. 最後看存不存在一個至少k-size的path

# Other Apporach

大致上主要核心思想都是將矩形攤開成一維矩陣
這邊更是將每個(x,y)點轉化成一維上的單點

left軸上, 每個位置用y表示
top軸上, 每個位置因為都接在left軸後面, 所以位置用`side+x`表示
right軸上, 每個位置用`2*side + (side-y)`表示
bottom軸上, 每個位置用`3*side + (side-x)`表示

那這樣我們一維矩陣就有每個點的相對位置了, 後續再做**排序**
便能得到位置先後順序正確的一維矩陣

那後續一樣是利用greedy的概念, 盡可能挑出k個合適的點

```py    
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def boundary_param(x, y, side):
            if x == 0:
                return y
            elif y == side:
                return side + x
            elif x == side:
                return 2*side + (side - y)
            else:
                return 3*side + (side - x)

        p = []
        for x, y in points:
            p.append(boundary_param(x, y, side))
        p.sort()

        n = len(p)
        e = p + [val + 4*side for val in p]
        def can_pick_start(i, d, next_idx):
            count = 1
            cur = i
            limit = e[i] + 4*side - d
            while count < k:
                nxt = next_idx[cur]
                if nxt >= i + n:
                    return False
                if e[nxt] > limit:
                    return False
                cur = nxt
                count += 1
            return True

        def feasible(d):
            next_idx = [0]*(2*n)
            idx = 0
            for j in range(2*n):
                while idx < 2*n and e[idx] < e[j] + d:
                    idx += 1
                next_idx[j] = idx

            for i in range(n):
                if can_pick_start(i, d, next_idx):
                    return True
            return False

        left, right = 0, 2*side
        while left < right:
            mid = (left + right + 1) // 2
            if feasible(mid):
                left = mid
            else:
                right = mid - 1
        return left
```