# Intuition

首先能先確認此題有沒有解:

```py
count = Counter()
for num in nums:
    count[num] += 1
for num in forbidden:
    count[num] += 1

# no enough position for current num
if any(freq > n for freq in count.values()): return -1
```

如果有任意nums[i]沒有足夠的位置, 那麼此題無解
也就是nums[i]的數目加上他被禁止的位置數目的總和, 必須不超過`n`

那麼再來就是計算有多少個invalid nums[i]需要swap

1. 先用hashmap `needSwap`紀錄需要交換位置的nums[i]總數
2. 再來我們目標是要將nums[i]跟另外個任意nums[j]交換位置, 所以我們此時只需關注每個distinct nums[i]的個數, 所以轉換成list並由小到大排序
3. 由於已經確認有足夠位置交換出合法解, 用雙指針兩兩交換, 從需要最多swap的數開始交換. 直到`l > r`

```py
# step.1
needSwap = Counter()
for i in range(n):
    if nums[i] == forbidden[i]:
        needSwap[nums[i]] += 1

# step.2
swaps = list(needSwap.values())
swaps.sort()

# step.3
res = 0
l, r = 0, len(swaps)-1
while l <= r:
    swap = min(swaps[l], swaps[r])
    res += swap
    swaps[l] -= swap
    swaps[r] -= swap
    if swaps[l] == 0 and swaps[r] == 0:
        l, r = l+1, r-1
    elif swaps[l] == 0:
        l += 1
    else:
        r-= 1
return res
```