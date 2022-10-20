class TrieNode: 
	def __init__(self): 
		self.children = {}
		self.isEnd = False 
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie 
        trie = TrieNode() 
        cur = trie
        for word in words: 
            cur = trie
            for i in range(len(word)): 
                if word[i] not in cur.children: 
                    cur.children[word[i]] = TrieNode()
                cur = cur.children[word[i]]
            cur.isEnd = True 
        
        res = []
        def dfs(r, c, cur, path): 
            ch = board[r][c]
            if ch in cur.children:   
                board[r][c] = '#' # to avoid checking visited cells
                node = cur.children[ch]
                path.append(ch)
                
                if node.isEnd: # found a match 
                    res.append(''.join(path.copy()))
                    node.isEnd = False # I can now delete this word and avoid future duplicative match 
                    
				        # If I am at a leaf, there is no further exploration and I can truncate the leaf
                if not node.children: 
                    cur.children.pop(ch) # highly influence performance.
                else: 
                    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]: 
                        _r, _c = r + dr, c + dc 
                        if 0 <= _r < ROWS and 0 <= _c < COLS: 
                            dfs(_r, _c, node, path)

                path.pop() 
                board[r][c] = ch # revert the "visited" marker
        
        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS): 
            for c in range(COLS): 
                dfs(r, c, trie, [])
        return res 