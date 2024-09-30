# Intuition

為了找出合法的lexicographically smallest **almost equal** sequence, 我們必須:
- **Greedily**的去選擇每個`word1[i]`
- 或是**Greedily** skip當前word1[i] (但前提是後續能組出合法almost equal sequence)

所以首先
1. 如果word[i] == word2[j]: 直接選, 這樣index才會是smallest
2. 如果word1[i] != word2[j] 並且我們還沒有跳過任何一次:
   - 這時我們要判斷假設我們選了word1[i]作為skip的話, 還有沒有機會組成合法**almost equal sequence**
     - 如果可以, 那就選並標記`skip=True`

所以我們會需要知道從當前`word1[i]`位置開始, 後續word1[i+1:]還能不能選出word2[j+1:]

因此我們從後往前遍歷word1[i], 然後標記要組出word2[j:] suffix的最後位置
定義last[i]: the last index in word1 to create suffix word2[i:]

```py
m, n = len(word1), len(word2)

last = [0] * n
j = n-1
for i in range(m-1, -1, -1):
    if j >= 0 and word1[i] == word2[j]:
        last[j] = i
        j -= 1
```

有了這資訊後我們就能遍歷word1[i], 然後greedily pick or skip
skip的時候如果當前字母已經是word2[n-1](最後一個字母), 或是skip後我們還能組出word2[j+1:] suffix, 那我們就應該選當前字母`word1[i]`作為跳過的字母
這樣最終就會是lexicographically smallest valid indices

```py
for i in range(m):
    if j == n: break # already found answer

    if word1[i] == word2[j]:
        res.append(i)
        j += 1
    elif not skip and (j == n-1 or i < last[j+1]):
        skip = True
        res.append(i)
        j += 1
```

# Complexity

time: O(word1.size)
space: O(word2.size)