# Intuition

數據量很小並且除了暴力破解看起來沒其他方法
所以用dfs去列舉所有可能

其中要注意幾個特別test case:
1. board = "RRYGGYYRRYYGGYRR", hand = "GGBBB"
這例子告訴我們不可以對hand去做filter, 即使board裡面沒有B, 我們也能利用B去做擋板來改變爆炸順序

2. board = "RRWWRRBBRR", hand = "WB"

直覺上可能會想說將hand[i]放的位置會是在在board[j]==hand[i]的情況, 來湊出consecutive sequence
但實際上會以這種情況:

answer: RRWWRRBBRR -> RRWWRRBBR[W]R -> RRWWRRBB[B]RWR -> RRWWRRRWR -> RRWWWR -> RRR -> empty

一開始的第一個**W**並不是放在跟W相鄰的位置上, 所以我們不能再dfs加上`if hand[i] == board[j]: 我們才產生newBoard`

所以我們能得出以下解法:
```py
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

        @cache
        def dfs(b, h):
            b = clear(b)
            if b and not h: return float('inf')
            if not b: return 0
            
            res = float('inf')
            for i in range(len(b)+1):
                for j in range(len(h)):
                    res = min(res, 1 + dfs(b[:i] + h[j] + b[i:], h[:j] + h[j+1:]))
            return res

        res = dfs(board, hand)
        return res if res < inf else -1
```

可惜這會TLE
所以必須要想一些剪枝的手段

1. 首先能想到的是對於當前的board來說, 相同的hand[i]其實掃過一遍結果都是一樣. 所以我們可以同樣的hand[i]我們只需要查驗一次即可

因此我們可以對hand排序, 然後在dfs內skip掉duplicate
```py
hand = ''.join(sorted(hand))

if i > 0 and hand[i] == hand[i-1]: continue
```

再來對於hand[i]放置的位置:
首先將hand[i]放在board[j] == hand[i]的位置肯定是比較好的
但從test case來看, 有的時候也必須放置在這以外的位置

ex. board = "RRWWRRBBRR", hand = "WB"
answer: RRWWRRBBRR -> RRWWRRBBR[W]R -> RRWWRRBB[B]RWR -> RRWWRRRWR -> RRWWWR -> RRR -> empty
                   -> RRWWRRBB[W]RR -> 

從上面例子來看, Ｗ插入在兩不同顏色的連續序列間的話, 就只會是個隔板, 不會有任何用處
只有插在某個連續序列**中間**, 目標是希望將一個連續序列拆開成兩個連續序列後, 能各自在跟左右兩邊去組合引爆並消除
所以從test case來看, 只能猜說或許這是個可以剪枝的方向
1. 將hand[i]放到同色的board[j]附近: if (board[j] == hand[i]): 插入hand[i]
2. 將hand[i]放到異色的連續序列board[j]中間: if (j>0 and board[j] == board[j-1] and board[j] != hand[i])

結合兩個條件變成: `if (board[j] == hand[i]) or (j > 0 and board[j] == board[j-1]):`