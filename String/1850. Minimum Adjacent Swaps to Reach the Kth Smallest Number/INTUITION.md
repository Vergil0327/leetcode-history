# Intuition

ex.1 5489355_142
-> 5489355_214
-> 5489355_241
-> 5489355_412
-> 5489355_421

k-th target, 從後往前來看:
一開始看n-1位跟n-2位最後兩位的permutation
然後看最後三位的permutation
...
其中後面位數要跟前面位數交換時, 後面位數必須跟比他小的位數交換才會wonderful

所以如果我們能求出`num' = findNextPermutation(num)`
那麼在找出k-th wonderful後, 跟原本的num計算最小交換數即可

首先可以用冒泡法O(n^2):
swap數就一個位置一個位置來看, 每次都將需要的數持續swap到該位置，最後加總後即可得到最小交換數

再來也可以透過計算reverse pairs來計算swap數目: 最小swap數可以用求reverse pairs得知, 而reverse pair可以用merge sort來解
leetcode 493.

而findNextPermutation完完全全就是leetcode 31.

```py
def findNextPermutation(num):
    nums = list(num)
    n = len(num)
    # 先找出跟哪個位置交換會變得更大
    i = n-1
    while i >= 1 and nums[i] <= nums[i-1]:
        i -= 1

    if i == 0: return sorted(num)

    i -= 1 # 這是我們要交換的位置

    # 找到比num[i]更大的數交換
    j = n-1
    while j > i and nums[j] <= nums[i]:
        j -= 1
    nums[i], nums[j] = nums[j], nums[i]

    # 後面位數排序成最小
    nums[i+1:] = sorted(nums[i+1:])
    return "".join(nums)
```