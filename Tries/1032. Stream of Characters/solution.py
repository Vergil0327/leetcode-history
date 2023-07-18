class Trie:
    def __init__(self):
        self.next = {}
        self.eow = False # end of word

class StreamChecker:

    def __init__(self, words: List[str]):
        self.minLen = inf
        self.trie = Trie()
        for word in words:
            self.minLen = min(self.minLen, len(word))
            curr = self.trie
            for ch in word[::-1]:
                if ch not in curr.next:
                    curr.next[ch] = Trie()
                curr = curr.next[ch]
            curr.eow = True

        self.stream = ""

    # O(len(stream of words until now))
    def query(self, letter: str) -> bool:
        self.stream += letter

        # impossible to form a valid suffix
        if len(self.stream) < self.minLen: return False

        curr = self.trie
        for i in range(len(self.stream)-1, -1, -1):
            if self.stream[i] not in curr.next: return False
            curr = curr.next[self.stream[i]]
            if curr.eow: return True
        return False
