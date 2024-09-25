Trie = lambda: defaultdict(Trie)
IS_END = "IS_END"
COUNT = "COUNT"

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        tri = Trie()
        for word in words:
            root = tri
            for ch in word:
                root = root[ch]
                root[COUNT] = root.get(COUNT, 0) + 1
            root[IS_END] = True
            

        scores = [0]*len(words)
        for i, word in enumerate(words):
            root = tri
            
            for ch in word:
                root = root[ch]
                scores[i] += root[COUNT]

        return scores