# Intuition

搜索文字的prefix/suffix => 首先想到的是Trie
由於要搜索的是同時擁有合法prefix, suffix的字, 以往trie都是單搜prefix或suffix
不知道有沒有辦法利用(prefix[0], suffix[-1])這樣類似的key來對trie進行搜索
直覺上應該是可以透過這樣的方式來作為Trie的key, 但可能要考慮一下如果preifx, suffix在query的時候一長一短
ex. ("prefix", "suf")這樣的情況的話, 在搜索中key就會出現類似這種情況("f", None), ("i", None), ...

所以最好的方式是在建立words[i]的trie時, 我們就提前處理好這些key
對於words[i]來說:

在prefix跟suffix都共同長度下：

```py
s1, s2 = word, word[::-1]

root = self.root
for i in range(len(word)):
    key = (s1[i], s2[i])
    if key not in root.next:
        root.next[key] = TrieNode()
    root = root.next[key]
    root.idx = wordIdx
```

但由於還要考慮prefix跟suffix可能有一方比較短, 所以我們把所有prefix跟suffix跟None的組合都也一並加入到trie裡

```py
s1, s2 = word, word[::-1]

root = self.root
for i in range(len(word)):
    # (prefix[i], None)
    tmp = root
    for ch in s1[i:]:
        key = (ch, None)
        if key not in tmp.next:
            tmp.next[key] = TrieNode()
        tmp = tmp.next[key]
        tmp.idx = wordIdx

    # (None, suffix[i])
    tmp = root
    for ch in s2[i:]:
        key = (None, ch)
        if key not in tmp.next:
            tmp.next[key] = TrieNode()
        tmp = tmp.next[key]
        tmp.idx = wordIdx
````

當我們把所有可能的key都加入後, 剩下的query就簡單了, 我們只需要

```py
s1, s2 = prefix, suffix[::-1]

root = self.root
for key in zip_longest(s1, s2):
    if key not in root.next: return -1
    root = root.next[key]
return root.idx
```

## Trie - implementation 1

```py
class TrieNode:
    def __init__(self):
            self.next = {}
            self.idx = -1

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str, wordIdx: int) -> None:
        s1, s2 = word, word[::-1]

        root = self.root
        for i in range(len(word)):
            tmp = root
            for ch in s1[i:]:
                key = (ch, None)
                if key not in tmp.next:
                    tmp.next[key] = TrieNode()
                tmp = tmp.next[key]
                tmp.idx = wordIdx

            tmp = root
            for ch in s2[i:]:
                key = (None, ch)
                if key not in tmp.next:
                    tmp.next[key] = TrieNode()
                tmp = tmp.next[key]
                tmp.idx = wordIdx

            key = (s1[i], s2[i])
            if key not in root.next:
                root.next[key] = TrieNode()
            root = root.next[key]
            root.idx = wordIdx
        

    def query(self, pre: str, suf: str):
        s1, s2 = pre, suf[::-1]

        root = self.root
        for key in zip_longest(s1, s2):
            if key not in root.next: return -1
            root = root.next[key]
        return root.idx
```

## Trie - implementation 2

另外在官方詳解上有個有趣的簡易實作Trie的方式是用defaultdict
資訊另外用個unique key去紀錄

```py
Trie = lambda: collections.defaultdict(Trie)
INFO = "ANY_UNIQUE_KEY_FOR_INFO"
```

那這樣要建構trie的話就會是:

```py
self.tri = Trie()
for idx, word in enumerate(words):
    root = self.tri

    rWord = word[::-1]
    for i in range(len(word)):
        tmp = root
        for ch in word[i:]:
            tmp = tmp[ch, None]
            tmp[INFO] = idx

        tmp = root
        for ch in rWord[i:]:
            tmp = tmp[None, ch]
            tmp[INFO] = idx

        root = root[word[i], rWord[i]]
        root[INFO] = idx
```