# Intuition

首先比較好想到的是對於這種有一連串queries的，我們可以考慮排個序來看看有沒有幫助

我們對queries由小到大排序後，我們要找的就是在一個時間範圍內有多少server沒有接收到request

所以我們也將logs對時間排序

那這樣排完後很明顯就是個sliding window的問題
我們用兩個pointer, `l`跟`r`來代表合法的logs區間

對於排序後的queries來說, 我們可以得知當前要詢問的區間範圍為: [q-x, q] = [start, end]

那這邊我們可以用個hashmap來紀錄當前這個sliding window有多少server有收到request

所以首先我們先移動右邊界`r`, 把所有log時間 <= end的全部加入到window裡:

```py
while r < size and logs[r][1] <= end:
    window[logs[r][0]] += 1
    r += 1
```

然後再移動左邊界`l`, 把不符合的的log移除掉

```py
while l < size and logs[l][1] < start:
    window[logs[l][0]] -= 1
    if window[logs[l][0]] == 0:
        del window[logs[l][0]]
    l += 1
```

那這樣就能得知當前範圍內有多少server沒有收到request:
`res[idx] = n-len(window)`