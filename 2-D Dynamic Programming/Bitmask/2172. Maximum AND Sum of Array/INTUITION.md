# Intuition

我們想要the maximum possible AND sum of nums given numSlots slots.
並且:
- 1 <= numSlots <= 9
- 1 <= nums[i] <= 15
- AND operation只會使得數值越來越小

首先想到的解法是:
我們遍歷nums[i], 然後試著放進slot裡, 可以選擇放或不放, 放的話slot_size必須<2, 並且得知道當前的AND sum

那麼能想到的是:
1. 用3進位制的`state`來表示各個slot size, 三進位數值:[0,1,2], 個別代表該位slot的當前size. 由於`1 <= numSlots <= 9`, 最多就9位
2. n <= 2*numSlots <= 18
3. 可能得維護一個長度為numSlots的AND sum

那首先想到的brute force就是用dfs遍歷所有結果(backtracking)
state[slot]可得知當前size, 只要size < 2, 那我們就可以試著加入進去然後增加該slot的AND sum: (nums[i] AND slot)

可以很快寫出:

```py
def dfs(i, bitmask):
    if i == n:
        self.res = max(self.res, sum(self.and_sums))
        return
    # 找出當前各slot_size
    state = []
    while bitmask:
        state.append(bitmask%3)
        bitmask //= 3
    
    for slot in range(1, numSlots+1):
        idx = slot-1
        if state[idx] < 2:
            self.and_sums[idx] += slot&nums[i]
            dfs(i+1, state + pow(3, idx))
            self.and_sums[idx] -= slot&nums[i]
    return
```

但其實我們並不需要儲存各個slot's AND sum, 我們只要全部加總取最大值即可, 可以很直覺改寫成
```py
@cache
def dfs(i, bitmask):
    if i == len(nums): return 0
    
    # 找出當前各slot_size
    state = [0]*numSlots
    bit = bitmask
    for j in range(numSlots):
        state[j] = bit%3
        bit //= 3

    res = 0
    for slot in range(1, numSlots+1):
        if state[slot-1] >= 2: continue
        res = max(res, dfs(i+1, bitmask + pow(3, slot-1)) + (nums[i]&slot))

    return res
```

時間複雜度:
沒有memorization情況是: O(numSlots^(n*3^numSlots))
那加上memorization則為: O(numSlots * n * 3^numSlots)

空間複雜度: O(n * 3^numSlots)