from itertools import zip_longest

# Implementation 1
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

# Implementation 2
class WordFilter:

    def __init__(self, words: List[str]):
        self.tri = Trie()
        for i, word in enumerate(words):
            self.tri.insert(word, i)

    def f(self, pref: str, suff: str) -> int:
        return self.tri.query(pref, suff)

Trie = lambda: collections.defaultdict(Trie)
INDEX = "IDX"

class WordFilter:

    def __init__(self, words: List[str]):
        self.tri = Trie()
        for idx, word in enumerate(words):
            root = self.tri

            rWord = word[::-1]
            for i in range(len(word)):
                tmp = root
                for ch in word[i:]:
                    tmp = tmp[ch, None]
                    tmp[INDEX] = idx

                tmp = root
                for ch in rWord[i:]:
                    tmp = tmp[None, ch]
                    tmp[INDEX] = idx

                root = root[word[i], rWord[i]]
                root[INDEX] = idx

    def f(self, pref: str, suff: str) -> int:
        root = self.tri
        for key in zip_longest(pref, suff[::-1]):
            if key not in root: return -1

            root = root[key]
        return root[INDEX]
