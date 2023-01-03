# 3-Pass

## Intuition

由於我們要求的是一個長度為三個遞增子序列`nums[j],nums[i],nums[k]`，因此我們可以遍歷中間的數`nums[i]`，然後判斷：
- 這個數的左邊有沒有存在一個數`nums[j]` 比 `nums[i]`小
- 這個數的右邊有沒有存在一個數`nums[k]` 比 `nums[i]`大

因此我們提前用O(n)時間來搜尋:
1. 從左到右，對於每個`i`位置來說，左半邊**小於**他的數的index是多少
2. 從右到左，對於每個`i`位置來說，右半邊**大於**他的數的index是多少

由於我們只需要知道有沒有一個數在左半邊比他小以及有沒有一個數在右半邊比他大

因此第一次遍歷，我們就維護一個最小值即可，並且如果當前`nums[i]`比這個最小值大，那就代表`nums[i]`存在一個`nums[j] < nums[i]` 並且 j = index of minimum value

反之亦然，第二次遍歷我們維護一個最大值，如果當前`nums[i]`比維護的最大值小，那就代表存在一個`nums[k]`使得`nums[i] < nums[k]`

因此透過兩次遍歷提前搜尋，第三次遍歷判斷，即可在`O(3n)`時間解出這道題

## Complexity

- time complexity

$$O(n)$$

- sapce complexity

$$O(n)$$

# Optimal 1-Pass Solution

## Intuition

我們可以用兩個變數來儲存nums[i]和nums[j]

在遍歷過程中:
  - 如果`num <= numI`，則更新numI
  - 如果前面if不成立並且`num < numJ`，則更新numJ
  - 如果前面兩個條件都不成立，並且當前`num`大於numI與numJ，則代表我們找到了nums[i], nums[j], nums[k]
  - 如果遍歷完都沒找到，代表不存在

注意為什麼第一個if是 `<=`，看下面這個case:

```
nums = [1,1,-2,6]
```
如果第一個條件是`<`的話，第二個1會更新到numJ去，如此一來numJ並不大於numI
由於必須是nums[i] < nums[j] < nums[k]，因此第一個if必須是`<=`，藉此更新numI永遠是最小的

## Complexity

- time complexity

$$O(n)$$

- sapce complexity

$$O(1)$$

# Longest Increasing Subsequence (LIS)

## Intuition

其實這題要問的就是存不存在一個長度至少為3的最長遞增子序列(longest increasing subsequence, LIS)

See LeetCode 300. LIS

透過LIS的貪心解法，也就是patient sort，也可看成是維護一個單調遞增的序列，並且像在玩接龍似的，持續優化這個序列，使其盡可能的能接得越長越好

因此我們可以透過binary search找出這個單調遞增序列`tails`中，大於等於`nums[i]`的位置，然後更新，持續維護這個單調遞增子序列，並且盡可能讓每個數值越小越好，數值越小越有機會接得越長

一但最後存在一個LIS長度至少為3，則代表存在一個`[nums[i],nums[j],nums[k]]`的子序列符合題意

## Complexity

- time complexity

$$O(nlogn)$$

- sapce complexity

$$O(n)$$
