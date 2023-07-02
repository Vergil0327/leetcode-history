# Intuition

對於subarray, 首先先往sliding window去想

```
X X X X X X {X X X X X X X}
l                        r
```

對於`nums[r]`來說, 我們目的是要讓每個pair的差都小於等於2

如果我們如果要確認這個條件
假設我們的window是個有序的bucket的話，我們僅需要看最大值跟最小值有沒有相差小於等於2:

這代表我們需要維持`window[-1]-window[0] <= 2`這個條件

所以首先我們可以用two pointers, `l`, `r`來找出一段subarray, 然後:

1. 對於有序容器, 我們可以用SortedList來維護我們的sliding window
2. sliding window加入`nums[r]`後, 如果`window[-1]-window[0] > 2`, 我們就持續移動`l`並從sliding window內移除`nums[l]`
3. 等到整個window都合法後, 對於`nums[r]`來說, 能跟他配對的`l`有`len(window)`個, 所以`res += len(window)`

time: O(nlogn)