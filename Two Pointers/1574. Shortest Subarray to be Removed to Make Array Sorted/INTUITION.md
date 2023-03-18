# Intuition

看Example 1
[1,2,3,10], 4 ,[2,3,5]
        l       r
    [3 10   4]
       [10  4   2]
最終答案是刪掉[3,10,4]或[10,4,2]

我們的目標是刪掉一段subarray，使得剩下的整體是個non-decreasing
只要知道左右邊界就可以確定subarray, 我們可以試著想看看有沒有什麼可以單調移動左右邊界來找尋合法subarray的方法

刪掉subarray, 假設這段是arr[l:r], 後要使得剩下的array是non-decreasing
這代表前面一段跟後面一段都是non-decreasing的，並且整體也是non-decreasing的
所以我們可以把arr分成三段來看:

arr = [XXXXXXXX]XXXXX[XXXXXX]
              l       r
1. arr[:l] non-decreasing
2. arr[r:] non-decreasing
3. arr[l] <= arr[r]

所以我們可以遍歷左邊區間i從0到l, 來找合法的r
由於arr[r]必須大於等於arr[l], 代表i從0到l往左移動時，r也只會單調的往右移動
所以我們可以用two pointers來找出我們要刪除的中間區間

# Approach

arr = [XXXXXXXX]XXXXX[XXXXXX]
              l       r
1. arr[:l] non-decreasing
2. arr[r:] non-decreasing
3. arr[l] <= arr[r]

所以一開始我們可以先找出前後兩個non-decreasing interval

```py
l, r = 0, n-1
while l+1 < n and arr[l] <= arr[l+1]:
    l += 1
while r-1 >= 0 and arr[r] >= arr[r-1]:
    r -= 1
```

那最終答案的初始值就是:
`res = min(n-l-1, r) # remove arr[l+1:] or arr[:r]`

然後我們就遍歷左邊區間[0:l]，並利用第三點條件`arr[r]>=arr[l]`來找尋合法的r即可