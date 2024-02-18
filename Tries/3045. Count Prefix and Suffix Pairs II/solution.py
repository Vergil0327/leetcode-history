class TrieNode:
    def __init__(self) -> None:
        self.next: Dict[str, TrieNode] = {}
        self.word_cnt = 0

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        s1, s2 = word, word[::-1]
        res = 0
        
        root = self.root
        for key in zip(s1, s2):
            if key not in root.next:
                root.next[key] = TrieNode()

            root = root.next[key]
            res += root.word_cnt
        
        root.word_cnt += 1 # add word count
        return res

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        n = len(words)

        root = Trie()
        for j in range(n):
            cnt = root.insert(words[j])
            res += cnt
            
        return res
