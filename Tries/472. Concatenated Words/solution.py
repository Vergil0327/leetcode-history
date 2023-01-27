class TrieNode:
    def __init__(self):
        self.next = {}
        self.eow = False # end of word

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.next:
                    curr.next[ch] = TrieNode()
                curr = curr.next[ch]
            curr.eow = True

        def dfs(curr, word, concatenated):
            for i, ch in enumerate(word):
                if curr.eow:
                    if dfs(root, word[i:], concatenated+1): return True

                if ch not in curr.next: return False
                curr = curr.next[ch]

            return curr.eow and concatenated > 0

        res = []
        for word in words:
            if dfs(root, word, 0): res.append(word)

        return res