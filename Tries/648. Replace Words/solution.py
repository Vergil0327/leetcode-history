class TrieNode:
    def __init__(self):
        self.next = {}
        self.endWord = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tri = TrieNode()
        for word in dictionary:
            curr = tri
            for ch in word:
                if ch not in curr.next:
                    curr.next[ch] = TrieNode()
                curr = curr.next[ch]
            curr.endWord = True
        
        res = []
        words = sentence.split()
        for word in words:
            root = ""
            curr = tri
            found = False
            
            for ch in word:
                if ch not in curr.next:
                    break
                
                root += ch
                if curr.next[ch].endWord:
                    found = True
                    res.append(root)
                    break

                curr = curr.next[ch]
            
            if not found:
                res.append(word)
                
        return " ".join(res)