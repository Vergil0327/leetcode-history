# Intuition

- 至少每個points[i]都得走過一遍, 不然minimum會是0
- 如果當前points[i]比較低, 但又有多餘的步數能走到底, 那就能來回多走幾次拉高最低minimum value
- 看到maximum minimum => 想到binary search

所以首先想到的是利用binary search去猜測這個maximum possible minimum value, 這時問題轉成該如何確認該value可不可行
如果能找到O(n)的helper function來檢查這件事, 這題就能以nlog(n)的時間完成

ex. points = [2,4,5], m = 5
[0,0,0] -> [2,0,0] -> [2,4,0] -> [4,4,0] -> [4,8,0] -> [4,8,5]
所以如果gameScore[i]需要抵達兩次, 代表第一次抵達後還需要額外回頭一次
因此, 過程中我們得紀錄當前i-th position需要來回多少步, 並將多走的步數分數加到下一個iteration去

主框架會像是:

```py
l, r = 0, max(points)*m
while l < r:
    mid = r - (r-l)//2
    if check(mid):
        l = mid
    else:
        r = mid-1
return l
```

難的部分在於如何正確計算back-and-forth的步數

首先起始我們先從0-th position開始, 起始分數points[0]
再來就依據分數來計算還需多少步, 並將額外來回走的步數加到下個位置去

```py
def check(target):
    # base case: already at 0-th position
    step = 1
    score = points[0]
    
    for i in range(n):
        # edge case
        if i == n-1:
            if score >= target: return True
            back_forth = ceil((target-score) / points[i])
            return step + back_forth * 2 <= m

        if score >= target:
            step += 1
            if step > m: return False
            score = points[i+1]
        else:
            back_forth = ceil((target-score) / points[i])
            step += back_forth*2 + 1 # 1 for forwarding to next position
            if step > m: return False
            score = points[i+1] * (back_forth+1)
    return True
```

但呈交後會發現有個坑(edge case)存在, 那就是

如果我們在`n-2`位置來回移動時, 如果最後結果導致`n-1`位置也已經滿足`target`了
那這時我們就不需要再移動到`n-1`位置去了, 也就是可以少走這一步

所以我們在來回走那一部分, 必須對`i == n-2`這位置額外做判斷

```py
def check(target):
    # base case: already at 0-th position
    step = 1
    score = points[0]
    
    for i in range(n):
        # edge case
        if i == n-1:
            if score >= target: return True
            back_forth = ceil((target-score) / points[i])
            return step + back_forth * 2 <= m

        if score >= target:
            step += 1
            if step > m: return False
            score = points[i+1]
        else:
            back_forth = ceil((target-score) / points[i])

            # n-2 edge case:
            if i+1 == n-1 and points[i+1] * back_forth >= target and step+back_forth*2 <= m: # no need for further step
                return True

            step += back_forth*2 + 1 # 1 for forwarding to next position
            if step > m: return False
            score = points[i+1] * (back_forth+1)
    return True
```