# Intuition

要找longest common prefix
直覺先往Trie去想, 如果我們把所有word都加進去並記錄每個a-z字符有多少個字詞貢獻的話
那麼從根節點開始, 用DFS遍歷a-z即可知道有哪些common prefix的字詞是`>= k`個的
最後把這些分別在每個節點cache起來, 這樣未來再繼續DFS時, 就避免遍歷到該節點時又再次計算了

所以主框架為:

- 以nlog(n)來進行`remove`跟`insert`
- 然後再同樣以nlogn(26n)進行`count`

```py
def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
    trie = Trie(0)

    for word in words:
        trie.insert(word)

    res = []
    for word in words:
        trie.remove(word)
        res.append(trie.count(k))
        trie.insert(word)

    return res
```