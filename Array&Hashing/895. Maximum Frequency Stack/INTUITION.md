# Intuition

1. 很直覺想到的是我們必須紀錄當前最高freq是多少, 這樣之後才能pop
2. 並且還要有stack儲存每個freq的數值

所以能想到的是我們必須有個hashmap來記錄每個值的frequency, 並且同時看能不能update currMaxFreq
然後有了frequency hashmap後, 我們以`frequency`為key, 再用個hashmap來對每個freq以stack的方式儲存value

所以我們如果拿example 1為例來模擬的話會是:
push很直覺的會是如下操作
對於每個newValue, 我們:
- update frequency hashmap => freqMap[newValue] += 1
- update current max frequency => currMax = max(currMax, freqMap[newValue])
- push value to freq stack => freqStack[freqMap[newValue]].append(newValue)

```
currMax = 1
freqMap = {
    5:1
}
freqStack = {
    1: [5]
}


currMax = 1
{
    5:1
    7:1
}
{
    1: [5,7]
}

currMax = 2
{
    5:2
    7:1
}
{
    2: [5]
    1: [5,7]
}

currMax = 2
{
    5:2
    7:2
}
{
    2: [5,2]
    1: [5,7]
}

currMax = 2
{
    5:2
    7:2
    4:1
}
{
    2: [5,2]
    1: [5,7,4]
}

currMax = 3
{
    5:3
    7:2
    4:1
}
{
    3: [5]
    2: [5, 7]
    1: [5, 7, 4]
}
```

那pop也一樣更新這三個資訊即可
