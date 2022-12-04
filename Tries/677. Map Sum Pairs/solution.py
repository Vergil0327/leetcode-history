class TrieNode:
    def __init__(self):
        self.next = {}
        self.prefixCount = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.record = {}

    def insert(self, key: str, val: int) -> None:
        delta = val-self.record[key] if key in key in self.record else 0

        curr = self.root
        for ch in key:
            if ch not in curr.next:
                curr.next[ch] = TrieNode()
            curr = curr.next[ch]

            if key not in self.record:
                curr.prefixCount += val
            else:
                curr.prefixCount += delta

        self.record[key] = val

    def sum(self, prefix: str) -> int:
        curr = self.root
        for ch in prefix:
            if ch not in curr.next:
                return 0

            curr = curr.next[ch]
        return curr.prefixCount
