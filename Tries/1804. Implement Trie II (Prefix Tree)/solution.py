from typing import Dict

class TrieNode:
    def __init__(self) -> None:
        self.next: Dict[str, TrieNode] = {}
        self.prefixCount = 0
        self.wordCount = 0

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        for ch in word:
            if ch not in root.next:
                root.next[ch] = TrieNode()
            root = root.next[ch]
            root.prefixCount += 1 # increment along the path
        root.wordCount += 1

    def countWordsEqualTo(self, word: str) -> int:
        curr = self.root
        for ch in word:
            if ch not in curr.next:
                return 0
            curr = curr.next[ch]
        return curr.wordCount

    def countWordsStartingWith(self, word: str) -> int:
        curr = self.root
        for ch in word:
            if ch not in curr.next:
                return 0
            curr = curr.next[ch]
        return curr.prefixCount

    def hasPrefix(self, word: str) -> bool:
        return self.countWordsStartingWith(word) > 0

    def erace(self, word: str):
        curr = self.root
        for ch in word:
            if ch not in curr.next: return

            curr.next[ch].prefixCount -= 1
            if curr.next[ch].prefixCount == 0:
                del curr.next[ch]
                return
            curr = curr.next[ch]
        curr.wordCount -= 1