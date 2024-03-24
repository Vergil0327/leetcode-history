class TrieNode:
    def __init__(self):
        self.next = {}
        self.ans = None
        
                
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = TrieNode()
        cur = trie
        for idx, word in enumerate(wordsContainer):
            cur = trie
            for i in range(len(word)-1, -1, -1):
                if word[i] not in cur.next:
                    cur.next[word[i]] = TrieNode()
                cur = cur.next[word[i]]
                if cur.ans is None:
                    cur.ans = (len(word), idx)
                else:
                    if len(word) < cur.ans[0] or (len(word) == cur.ans[0] and idx < cur.ans[1]):
                        cur.ans = (len(word), idx)
        
        minLengthIdx = 0
        for i in range(len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[minLengthIdx]):
                minLengthIdx = i
            
        res = [minLengthIdx] * len(wordsQuery)
        for i, q in enumerate(wordsQuery):
            cur = trie
            for ch in q[::-1]:
                if ch not in cur.next: break
                cur = cur.next[ch]
                res[i] = cur.ans[1]
        return res
