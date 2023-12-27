# Intuition

我們能對任意subarray進行sorting, 亦即我們能對任意subarray進行各種sorting
也就是我們能對每個subarray進行bubble sort => 代表對於任意s[i]只要s[i-1] > s[i], 我們就能swap(s[i-1], s[i])

因此得到一個很重要的結論是: 只要s[i-1] > s[i], 我們就能將s[i]往前移

既然如此, 那我們看下面這例子
由於我們要將s==t, 我們就由左往右逐個觀看看能不能透過swap使得s[i] == t[i]

```
s = X X Y X Y X X X
    0 1 2 3 4 5 6 7
t = Y Y Y Y Y Y Y Y
    i
```
所以i from 0 to n-1, 首先看t[0]:
我們必須將s[2]移到index=0的位置才行, 這代表必須滿足: s[2] < (s[0] and s[1])

並且由於最多就10個digits, "0"~"9", 所以我們可以先用`pos[digit]`紀錄他們出現的**index**
這樣我們在判斷`t[i]`能不能透過bubble sort來被s滿足時
我們就能透過在`pos[digit]`上, 遍歷所有**小於t[i]**的這些digits來看, 是不是存在任何一個比t[i]小的digit的index小於當前`i`
如果是, 那代表我們沒辦法在s[i]找到一個可以swap到i位置的t[i], 直接返回False
等到遍歷完t[i], 那就代表每個t[i]都可以透過bubble sort找到一個相對應的s[i], 所以返回True

# Complexity

- time complexity
$$O(10 * n)$$

- space complexity
$$O(n)$$