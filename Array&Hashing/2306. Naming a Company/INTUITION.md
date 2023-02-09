# Intuition

```
example
Input: ideas = ["coffee","donuts","time","toffee"]
Output: 6
```

依據題意，每個詞可拆解成[ideaA[0], ideaA[1:]]，兩詞互換suffix後，必須不在ideas集合裡

首先想到的是我們把相同suffix的存在一起，同個group之間一定是不合法的，我們只要從不同group中，扣掉各自共同擁有的首字母，即可組成合法組合

`res += (setA.size - common_set.size) * (setA.size -common_set.size)`

由於前後對調也是合法組合，所以我們還要 `*= 2`

`res += (setA.size - common_set.size) * (setA.size -common_set.size) * 2`

```py
ideas = ["coffee","donuts","time","toffee"]
groupBySuffix = {'offee': {'c', 't'}, 'onuts': {'d'}, 'ime': {'t'}}

items = list(groupBySuffix.items())
for i in range(len(items)):
    set_a = items[i][1]
    for j in range(i+1, len(items)):
        set_b = items[j][1]
        common = len(set_a&set_b)
        res += (len(set_a)-common) * (len(set_b)-common) * 2
```

但會發現這樣會TLE，因為我們其實可能會遍歷`O(n^2) = 5*10^4 * 5*10^4`

既然這樣，我們該想到的是，我們應該反過來 `groupByFirst`
這樣我們僅需要遍歷兩層26個字母，所以上方的程式碼可轉為

```py
for i in range(26):
    a = chr(ord("a")+i)
    if a not in groupByFirst: continue
    for j in range(i+1, 26):
        b = chr(ord("a")+j)
        if b not in groupByFirst: continue

        common = len(groupByFirst[a]&groupByFirst[b])
        res += (len(groupByFirst[a])-common) * (len(groupByFirst[b])-common)*2
```


{'c': {'offee'}, 'd': {'onuts'}, 't': {'offee', 'ime'}}