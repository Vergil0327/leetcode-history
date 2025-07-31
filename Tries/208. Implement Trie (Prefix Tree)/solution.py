class TrieNode:
    def __init__(self):
        self.next = {}
        self.eow = False # end of word

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.next:
                node.next[ch] = TrieNode()
            node = node.next[ch]
        node.eow = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.next:
                return False
            node = node.next[ch]
        return node.eow
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.next:
                return False
            node = node.next[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)