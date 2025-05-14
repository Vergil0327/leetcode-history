# https://leetcode.com/problems/palindrome-pairs/solutions/79195/o-n-k-2-java-solution-with-trie-structure/
class TrieNode:
    def __init__(self) -> None:
        self.next: Dict[str, TrieNode] = {}
        self.index = -1
        self.arr = []

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        root = TrieNode()

        def isPal(word, l, r):
            while l < r:
                if word[l] != word[r]: return False
                l, r = l+1, r-1
            return True

        def addWord(root, word, index):
            for i in range(len(word)-1, -1, -1):
                ch = word[i]

                if ch not in root.next:
                    root.next[ch] = TrieNode()

                if isPal(word, 0, i):
                    root.arr.append(index)

                root = root.next[ch]
            root.arr.append(index)
            root.index = index

        def search(words, i, root):
            for j in range(len(words[i])):
                if root.index >= 0 and root.index != i and isPal(words[i], j, len(words[i])-1):
                    res.append([i, root.index])
                if words[i][j] not in root.next: return
                root = root.next[words[i][j]]
            
            for j in root.arr:
                if i == j: continue
                res.append([i, j])

        for i in range(len(words)):
            addWord(root, words[i], i)

        for i in range(len(words)):
            search(words, i, root)

        return res

# O(N*L^2)
# https://www.youtube.com/watch?v=L7MmngL-iaM
class Solution_TLE:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word2idx = {}
        for i, word in enumerate(words):
            word2idx[word] = i

        complementPair = set()
        for word in words:
            complementPair.add(word)

        @lru_cache(None)
        def isPal(s):
            if not s: return True

            l, r = 0, len(s)-1
            if s[l] == s[r]:
                return isPal(s[l+1:r])
            else:
                return False
            
        res = set()
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                s1, s2 = word[:j], word[j:]

                # complementPair + words[i] = s + (s1 + s2):
                # check if `s1` is palindrome and s is reversed(s2).
                if isPal(s1):
                    s = s2[::-1]
                    if s != word and s in complementPair:
                        res.add((word2idx[s], i))

                # words[i] + complementPair = (s1 + s2) + s
                # check if `s2` is palindrome and s is reverseds1.
                if isPal(s2):
                    s = s1[::-1]
                    if s != word and s in complementPair:
                        res.add((i, word2idx[s]))
        return list(res)