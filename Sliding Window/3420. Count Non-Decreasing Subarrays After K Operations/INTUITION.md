# Intuition

O(n^3) brute force:

```py
n = len(nums)

def check(i, j):
    need = 0
    mx = nums[i]
    for idx in range(i+1, j+1):
        x = max(0, mx-nums[idx])
        need += x
        mx = nums[idx] + x
    return need <= k

res = 0
for i in range(n):
    for j in range(i, n):
        if check(i, j):
            res += 1
return res
```

subarray相關問題可以聯想到prefix sum或是sliding window

如果`nums[i:j]` (both i,j inclusive)可以在k次操作以內形成non-decreasing
那麼`nums[i+1:j]`, `nums[i+2:j]`, ..., `nums[j-1:j]`, `nums[j:j]`也會是合法non-decreasing subarray
貢獻的合法數為: `j-i+1`

所以想法是我們就持續移動sliding window右端點`r`, 直到使整個window合法的操作數超過`k`次時, 在移動左端點`l`縮小window
那每次只要有合法window, 貢獻subarray數就是`j-i+1`

這樣就將時間複雜度降低至O(n^2)

```py
n = len(nums)

def check(i, j):
    need = 0
    mx = nums[i]
    for idx in range(i+1, j):
        x = max(0, mx-nums[idx])
        need += x
        mx = nums[idx] + x
    return need

l = r = res = 0
while r < n:
    r += 1

    while l < r and check(l, r) > k:
        l += 1

    res += r-l

return res
```


但根據數據規模大小, 時間上僅能接受O(n)或O(nlogn)
那看來我們`check`必須以O(1)時間達成才行

這邊看`check`函式會發現我們會需要知道window內是否是non-decreasing
這時想到monotonic stack

我們可以用一個monotonic decreasing stack去紀錄當前window內的最大max element

[4,5,2,2] => non-decreasing => [4,5,5,5]
對於後面兩個2, 他們的absolute difference是找左側最近的mx去計算
那這時會發現我們可以改個方向遍歷, 由右往左遍歷然後配合monotonic decreasing stack, 這樣一但遍歷到`5`時, 便持續將stack裡的2給彈出來並同時計算所需操作數
1. [2]
2. [2,2]
3. [2,2] 5 => [2] 5 => [5]

因此大致上的想法會是改成**由右往左**進行sliding window並同時維護monotonic decreasing stack去計算所需操作數

```py
def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
    nums.reverse()

    res = 0
    window = deque()
    l = 0
    for r in range(len(nums)):
        # reversed_nums=[6, 4, 8]
        # 實際上原本是: [8, 4, 6] => non-decreasing => [8,8,8]
        # 所以這邊做的事情是: [6,6,8] => [8,8,8], 先計算(6,4), 再來這段會全變成6, 然後再計算(6,8), 將全部6轉成8的操作數
        while window and nums[window[-1]] < nums[r]:
            rr = window.pop()
            ll = window[-1] if window else l - 1
            cnt = rr - ll
            k -= cnt * (nums[r] - nums[rr])
        window.append(r)

        # nums[window[0]]是目前max, max-nums[l]就會是滑窗左端點移動後所返回的操作數
        while k < 0:
            k += nums[window[0]] - nums[l]
            if window[0] == l:
                window.popleft()
            l += 1
        res += r - l + 1
    return res
```

同樣地, sliding window找出最大合法subarray後, 裡頭合法的subarray數同樣為`r-l+1`