# Intuition

這題單純考驗細不細心, 小心edge case即可

首先分跟秒分別落在`[0:99]`這區間

所以一開始我們先將`targetSeconds`轉成分秒
`minute, sec = targetSeconds//60, targetSeconds%60`

再來我們最多就兩種選擇

1. 直接轉到`minute`跟`sec`
2. 把一分鐘加到秒數去:
   - minute -= 1 and sec += 60
   - 前提是 minute > 0 and sec <= 39. 不然會不符合`[0:99]`區間範圍

再來我們就來討論這兩種可能

首先`option1`僅可能發生在`minute < 100`
而`option2`僅可能發生在`sec <= 39`

再來就是把`minute`跟`sec`處理成string

```py
option1 = ""
if minute < 100:
    # construct option1 from `minute` and `sec`
    
option2 = ""
if minute > 0 and sec <= 39:
    # construct option2 from `minute` and `sec`
```

那這邊要注意的是, 為了節省cost, 我們要善用prepending zero這功能
這代表我們可以去除所有的leading zeros, 所以:
```py
option = (str(minute) if minute > 0 else "")
if option:
    option += str(sec) if sec >= 10 else "0"+str(sec) # if we have minute to push, we need to fill "0" if sec < 10
else:
    option = str(sec) # no need for prepending zeros
```

等到這兩種option都構造好之後, 就依照敘述計算cost即可
```py
def cost(option):
    curr = str(startAt)
    cost = 0
    for i in range(len(option)):
        if option[i] == curr:
            cost += pushCost  # push
        else:
            curr = option[i]
            cost += moveCost + pushCost # push
    return cost

res = inf
if option1:
    res = min(res, cost(option1))
if option2:
    res = min(res, cost(option2))
return res
```