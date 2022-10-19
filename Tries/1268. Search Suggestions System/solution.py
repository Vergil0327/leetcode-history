# explanation: https://www.youtube.com/watch?v=GTPgTxTuung
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndWord = False

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        
        # construct Trie
        for word in products:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.isEndWord = True
                
        res = []
        prefix = ""
        curr = root
        
        def dfs(state, s, root):
            if len(state) == 3:
                return
            
            if root.isEndWord:
                state.append(s) # don't return. we need to continue exploring trie node
            
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if ch not in root.children:
                    continue
                s += ch
                dfs(state, s, root.children[ch])
                s = s[:-1]
            return
                
                
        for i in range(len(searchWord)):
            ch = searchWord[i]
            
            # edge case
            if ch not in curr.children:
                for j in range(i, len(searchWord)):
                    res.append([])
                return res
            
            prefix += ch            
            curr = curr.children[ch]
            
            state = [] # recommendataions, pass by assignment
            dfs(state, "", curr)
            
            # don't forget to append prefix
            for i in range(len(state)):
                state[i] = prefix+state[i]
            res.append(state)
        
        return res