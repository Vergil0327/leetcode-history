from collections import defaultdict

## Trie - implementation 1

class TrieNode:
    def __init__(self):
            self.next = {}
            self.isEnd = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word) -> None:
        root = self.root
        for i in range(len(word)):
            if word[i] not in root.next:
                root.next[word[i]] = TrieNode()
            root = root.next[word[i]]
        root.isEnd = True

## Trie - implementation 2

Trie = lambda: defaultdict(Trie)
IS_END = "ISEND"

words = ["word1", "word2", "word3", "word4"]
tri = Trie()
for word in words:
    root = tri
    for ch in word:
        root = root[ch]
    root[IS_END] = True