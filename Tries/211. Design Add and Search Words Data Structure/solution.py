class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.tri = TrieNode()
        self.maxWordLen = float("-inf") # early return False for any search word whose length is greater than max

    def addWord(self, word: str) -> None:
        self.maxWordLen = max(self.maxWordLen, len(word))
        
        root = self.tri
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]
        root.endOfWord = True

    def search(self, word: str) -> bool:
        if len(word) > self.maxWordLen:
            return False
        
        root = self.tri
            
        def dfs(j, root):
            curr = root
            
            for i in range(j, len(word)):
                ch = word[i]
                if ch == '.':
                    for child in root.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if ch not in root.children:
                        return False
                    root = root.children[ch]
            return root.endOfWord

        return dfs(0, root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)