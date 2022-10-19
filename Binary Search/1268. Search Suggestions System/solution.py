# explanation: https://www.youtube.com/watch?v=GTPgTxTuung

class TrieNode:
    def __init__(self):
        self.c = {}
        self.endWord = False

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        
        res = []
        
        prefix = ""
        for ch in searchWord:
            prefix += ch
            i = bisect.bisect_left(products, prefix)
            
            recom = []
            for j in range(i, len(products)):
                if not products[j].startswith(prefix) or len(recom) == 3: break
                recom.append(products[j])
            res.append(recom)
        return res
