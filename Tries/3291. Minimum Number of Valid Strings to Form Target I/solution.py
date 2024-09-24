# Trie = lambda: defaultdict(Trie)
# IS_END = "ISEND"

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

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        tri = Trie()
        for word in words:
            # root = tri
            # for ch in word:
            #     root = root[ch]
            # root[IS_END] = True
            tri.insert(word)

        @cache
        def dfs(i, tri):
            if i >= len(target): return 0

            res = inf
            root = tri
            for j in range(i, len(target)):
                if target[j] in root.next:
                    root = root.next[target[j]]
                    res = min(res, dfs(j+1, tri)+1)
                else:
                    break

            return res
        
        res = dfs(0, tri.root)
        return res if res < inf else -1
    
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)

        dp = [inf] * (n + 1)
        dp[0] = 0

        def exist(w):
            for word in words:
                if word.startswith(w):
                    return True
            return False

        l = 0
        for r in range(1, n + 1):
            while l < r and not exist(target[l:r]):
                l += 1

            if l == r: return -1

            dp[r] = dp[l] + 1
        
        return dp[n]