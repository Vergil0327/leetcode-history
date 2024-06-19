class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        # clear consecutive balls recursively
        def clear(s):
            n = len(s)

            i = 0
            while i < n:
                j = i
                while j < n and s[j] == s[i]:
                    j += 1
                if j-i >= 3:
                    return clear(s[:i] + s[j:])

                i = j

            return s

        
        n = len(hand)
        hand = ''.join(sorted(hand))
        @cache
        def dfs(board, hand):
            if not board:
                return n - len(hand)
            if not hand:
                return inf

            ans = inf
            for i in range(len(hand)):
                if i > 0 and hand[i] == hand[i-1]: continue
    
                for j in range(len(board)):
                    if (board[j] == hand[i]) or (j > 0 and board[j] == board[j-1]):
                        newBoard = clear(board[0:j] + hand[i] + board[j:])
                        ans = min(ans, dfs(newBoard, hand[0:i] + hand[i+1:]))
            return ans
        
        res = dfs(board, hand)
        return res if res < inf else -1
