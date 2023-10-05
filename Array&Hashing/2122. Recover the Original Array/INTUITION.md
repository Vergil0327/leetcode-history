# Intuition

一開始想法是`lower[i] = arr[i]-k`, `higher[i] = arr[i]+k`
=> 所以lower[i]跟higher[i]差2k

因此合法解存在於:
- 兩兩配對必須差值相同, 皆能被2整除

所以馬上想到對nums排序: nums = [X X X X X X X X ...]
然後我們嘗試去找出可能的`k`值來

我們選nums[0]為基準, 那麼`2*k = kk = nums[i]-nums[0] where i from 1 to len(nums)-1`

所以排序後我們遍歷`nums[1:]`, 排除掉不合法情況:
- kk為positive integer => 不可為0
- kk必須能被2整除
- 在得到posible kk後, 我們就遍歷整個nums一遍來看是不是每個nums[i]都能找到nums[i]+kk
    - 找的方法也很簡單, 由於我們已經排序過, nums[i]必定得跟nums[i]+kk配對. 反之我們把nums[i]加入到hashmap裡, 那麼nums[i]必定存在一個nums[i]-kk的配對. 最後看hashmap有沒有為空即可
      - 如果最後hashmap為空, 代表每個nums[i]都能找到nums[i]-kk並與之配對
      - 如果不為空, 則kk不合法

```py
for num in nums[1:]:
    kk = num-nums[0]
    if kk == 0: continue
    if kk%2 != 0: continue

    paired = defaultdict(int)
    for num in nums:
        if num-kk in paired:
            paired[num-kk] -= 1
            if paired[num-kk] == 0:
                del paired[num-kk]
        else:
            paired[num] += 1

        if len(paired) == 0: # found k
            k = kk//2
```

等我們找到`k`後, 那還原`arr`就簡單了
一樣遍歷`nums`並透過hashmap紀錄哪些nums[i]已經配對過, 此時:
- nums[i]必定存在一個nums[i]+kk的配對 => `此時arr[i] = nums[i] + kk//2`
- 找到一個配對後我們把用來跟`nums[i]`配對的`nums[i]+kk`放入到hashmap裡計數, 等到下次遇到那就`hashmap[nums[i]] -= 1`並跳過, 一但**hashmap[nums[i]] == 0**就從集合裡移除.

這樣遍歷完後就能還原出原本的`arr`, 此時直接返回即可

```py
paired = defaultdict(int)
for num in nums:
    if num in paired:
        paired[num] -= 1
        if paired[num] == 0:
            del paired[num]
        continue
        
    res.append(num+k)
    paired[num+kk] += 1
```

time: $O(nlogn + n^2)$