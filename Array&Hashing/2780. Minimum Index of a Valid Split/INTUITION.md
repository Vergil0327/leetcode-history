# Intuition - 2 pass

這題我們要找的是一個最靠前的valid split
一個valid split `i`, 必須以`i`為分界的prefix跟suffix都有著相同的dominant element

所以如果我們可以用O(1)來判斷的話, 就可以用O(n)時間來決定valid split

因此我們先看每個prefix的dominant element

我們從左往前遍歷, 如果當前nums[i]來說:
- 如果freq1[nums[i]] + 1之後大於currMaxFreq
  - 代表這時nums[i]有可能是dominant elemnt
  - 判斷maxFreq*2有沒有 > size
    - 有的話則紀錄dominant[i] = nums[i]

```py
dominant = [-1] * n
freq1 = defaultdict(int)
maxFreq = 0
for i in range(n-1):
    size = i+1
    freq1[nums[i]] += 1
    if freq1[nums[i]] > maxFreq:
        maxFreq = freq1[nums[i]]
        if maxFreq*2 > size:
            dominant[i] = nums[i]
```

等到決定完所有prefix的dominant element後
我們在從後往前遍歷一遍:

```py
res = -1
freq2 = defaultdict(int)
maxFreq = 0
domiElem = -1
for i in range(n-1, 0, -1):
    size = n-i
    freq2[nums[i]] += 1
    if freq2[nums[i]] > maxFreq:
        maxFreq = freq2[nums[i]]
        domiElem = nums[i]
    if maxFreq*2 > size and dominant[i-1] == domiElem:
        res = i-1
```

- 如果freq2[nums[i]]+1後大於maxFreq的話, 代表我們可以更新suffix的dominant element = nums[i]
- 同時我們判斷, 如果此時maxFreq*2 > size並且當前suffix dominant elemnt == dominant[i-1]的話, 那我們就可以更新`res = i-1`, 也就是下圖:

左邊prefix的donimant element = dominant[i]
右邊suffix的donimant element可以在由右往左遍歷時得知
```
X X X X X X X X X  |  X X X X X X
               i-1  <-i       <-i
```