def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dic = set(words)
        memo = {}
        def dfs(word):
            if word in memo:
                return memo[word]
            
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in dic and suffix in dic:
                    return True
                if prefix in dic and dfs(suffix):
                    return True
                if suffix in dic and dfs(prefix):
                    return True
            
            memo[word] = False
            return False
        
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
                
        return res