class Trie:
    def __init__(self, count):
        self.next = {}
        self.word_cnt = count
        self.k_length = None

    def insert(self, word, idx=0):
        self.k_length = None
        if idx == len(word): return

        ch = word[idx]
        if ch not in self.next:
            self.next[ch] = Trie(0)
        self.next[ch].word_cnt += 1
        self.next[ch].insert(word, idx+1)
        

    def remove(self, word, idx=0):
        self.k_length = None
        if idx == len(word): return

        ch = word[idx]
        if ch not in self.next: return

        if self.next[ch].word_cnt == 1:
            del self.next[ch]
            return

        self.next[ch].word_cnt -= 1
        self.next[ch].remove(word, idx+1)

    def count(self, k):
        if self.k_length: return self.k_length

        length = 0
        for ch in string.ascii_lowercase:
            if ch not in self.next: continue

            if self.next[ch].word_cnt >= k:
                length = max(length, 1+self.next[ch].count(k))

        self.k_length = length
        return length

class Solution:
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
