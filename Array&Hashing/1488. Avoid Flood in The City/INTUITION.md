# Intuition

如果rains[i] = 0, 可以對這天之前的某個湖抽水
由於限制只能對第i天前的湖水抽水, 所以我們應該記錄index以方便之後決策
ex. dryDay.append(i)

如果rains[i] > 0:
1. 如果rains[i]沒下過, 那就下沒關係, 我們紀錄他哪天下. rainDay[rains[i]] = i
2. 如果已經下過雨:
    - 那我們就必須在dryDay裡挑一天去抽水
    - 並且這個dryDay必須 => rainDay[rains[i]] < dryDay < i
    - 那如果有多個dryDay可選? => 挑越靠前越好, 後面dryDay留給後面的rains[i]用
    => 代表這個dryDay可以用binary_search.bisect_right來找一個 `> rainDay[rains[i]]` 的位置, 並且dryDay使用後要移除
    => 用SortedList
3. 如果有沒有使用到的dryDay, 隨便抽一個lake, 1 <= lake <= 10^9, 0代表dry day不代表湖