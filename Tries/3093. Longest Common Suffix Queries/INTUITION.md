# Intuition

一開始先想到的brute force想法是:
找longest common suffix (LCS) => 每個wordsContainer[j]都從後往前跟當前wordsQuery[i]比對suffix, 然後找出最長的
=> O(wordsContainer.length * wordsQuery.length)

由於每個每個wordsContainer[j]我們都要從後往前比對找出LCS, 可以很直覺想到我們可以把wordsContainer全轉成Trie

```py
class TrieNode:
    def __init__(self):
        self.next = {}
        self.isEnd = False

trie = TrieNode()
cur = trie
for idx, word in enumerate(wordsContainer):
    cur = trie
    for i in range(len(word)-1, -1, -1):
        if word[i] not in cur.next:
            cur.next[word[i]] = TrieNode()
        cur = cur.next[word[i]]

    cur.isEnd = True
```

那轉成Trie之後, 對於每個wordsContainer[j]經過的節點, 我們就可以記錄當前的index
並且根據題意:

1. 在Trie裡相同節點我們僅需要紀錄長度最短的wordsContainer[j]
2. 如果兩者長度一樣, 那就選index最小的

所以我們的trie如下:

```py
trie = TrieNode()
cur = trie
for idx, word in enumerate(wordsContainer):
    cur = trie
    for i in range(len(word)-1, -1, -1):
        if word[i] not in cur.next:
            cur.next[word[i]] = TrieNode()
        cur = cur.next[word[i]]
        if cur.ans is None:
            cur.ans = (len(word), idx)
        else:
            if len(word) < cur.ans[0] or (len(word) == cur.ans[0] and idx < cur.ans[1]):
                cur.ans = (len(word), idx)
```

再來我們就能很簡單的去利用trie去搜索每個wordsQuery[i]即可

```py
for i, q in enumerate(wordsQuery):
    cur = trie
    for ch in q[::-1]:
        if ch not in cur.next: break
        cur = cur.next[ch]
        res[i] = cur.ans[1]
return res
```

那如果沒有任何一個跟wordsQuery[i]有LCS呢?, 那就要從wordsContainer[j]找出一個長度最小最靠左的作為答案
所以

```py
minLengthIdx = 0
for i in range(len(wordsContainer)):
    if len(wordsContainer[i]) < len(wordsContainer[minLengthIdx]):
        minLengthIdx = i
    
res = [minLengthIdx] * len(wordsQuery)
```