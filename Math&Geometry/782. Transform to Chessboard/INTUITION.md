# Intuition

minimum number of moves => BFS?
for better convenient calculation, we can use bitmask to represent for each row
and we can concat each bitmask as state to check if we visited current board or not

use state below as each board's
```py
state = 0
for i in range(n):
    state |= (cur[i]<<(n*i))
```

可惜MLE:

```py
n = len(board)

brd = []
for i in range(n):
    bit = 0
    for j in range(n):
        bit |= board[i][j]<<j
    brd.append(bit)

# BFS
def check(bits):
    first = bits[0]&1
    for i in range(n):
        for j in range(n):
            cur = (bits[i]>>j)&1
            
            if i-1 >= 0:
                up = (bits[i-1]>>j)&1
                if cur == up: return False
            if i+1 < n:
                down = (bits[i+1]>>j)&1
                if cur == down: return False
            if j-1 >= 0:
                right = (bits[i]>>(j-1))&1
                if cur == right: return False
            if j+1 < n:
                left = (bits[i]>>(j+1))&1
                if cur == left: return False
    return True

def swapColBit(bits, i, j):
    for row in range(len(bits)):
        col1 = (bits[row]>>i)&1
        col2 = (bits[row]>>j)&1
        if col1 != col2: # should swap
            mask = (1<<i) | (1<<j)
            bits[row] ^= mask
    return bits

queue = deque([brd])
visited = set()
step = 0
while queue:
    for _ in range(len(queue)):
        cur = queue.popleft()
        state = 0
        for i in range(n):
            state |= (cur[i]<<(n*i))

        if state in visited: continue
        visited.add(state)
        if check(cur): return step

        # change row i, j
        for i in range(n):
            for j in range(i+1, n):
                cpy = cur.copy()
                cpy[i], cpy[j] = cpy[j], cpy[i]
                queue.append(cpy)

        # change column i, j
        for i in range(n):
            for j in range(i+1, n):
                nxt = swapColBit(cur.copy(), i, j)
                queue.append(nxt)
    step += 1
return -1
```

提早排除掉不可能合法的會更快嗎?
=> 任意兩row或兩column互換, 每row跟每column的1, 0個數都是不變的, 都會各半
=> 再來就是不管row或column之間怎麼換, 都只會有兩種形式, 並且兩種形式會是互斥:
ex. 101010101... 跟 010101010...
ex. 1010跟0101

所以我們就檢查每一row, column是不是1's, 0's各半, 然後是不是從row來看或從column來看, 都只有兩種形式

```py
def checkPossible(board):
    n = len(board)

    # check rows
    typ1 = typ2 = 0
    typ1 += 1 # choose row1 as typ1
    for i in range(1, n):
        if board[i][0] == board[0][0]:
            typ1 += 1
            for j in range(n):
                if board[i][j] != board[0][j]: return False
        else:
            typ2 += 1
            for j in range(n):
                if board[i][j] == board[0][j]: return False
    
    if abs(typ1-typ2) > 1: return False # typ1, typ2應該為n//2 或 {n//2, (n+1)//2}

    # check columns
    typ1 = typ2 = 0
    typ1 += 1 # column1 as typ1
    for j in range(1, n):
        if board[0][j] == board[0][0]:
            typ1 += 1
            for i in range(n):
                if board[i][0] != board[i][j]: return False
        else:
            typ2 += 1
            for i in range(n):
                if board[i][0] == board[i][j]: return False
    if abs(typ1-typ2) > 1: return False # typ1, typ2應該為n//2 或 {n//2, (n+1)//2}
    return True
```

所以從排除非法board這邊會發現, 不管row或column, 都只會有兩種形式的排列

ex. 只看row的話可能就只有`10011`跟`01100`, 然後看column只會有`11100`跟`00011`
如果我們將`10011`作為typ1, `01100`作為typ2
當我們透過swap, 把typ1變成`10101`時, 其實其他同樣為typ1的row也會同步變成`10101`
同時typ2的`01100`也會還原成`01010`

所以我們分別以row跟column來看, 分別計算各自需要多少swap後, 相加即為整體需要的swap次數
並且我們只需要挑第一個row跟第一個column來計算就好, 因為其他row跟column都會隨著swap一併操作

那麼該如何計算swap? 
我們要將第一行`10011` => `10101`, 我們可以計算他有多少個錯位的bit, 一次swap可解決一對錯位的bit
所以**swap = 錯位bit數目/2**

由於我們要找minimum steps, 所以我們行跟列的swap數目都要計算, 最後各自取最小的即可
最後行列兩邊的minimun swaps相加即為所求

但別忘了我們在計算錯位時:
- 偶數長度: 第一行可以是`1010`也可以是`0101`
    - ex. 1100來看:
        - 111000 -> 101010: 2錯位, 1 swap
        - 111000 -> 010101: 4錯位, 2 swap
- 奇數長度: 只能是`10101` 或 `01010`, 根據他的1, 0數目
    - ex. 11100
        - 11100 -> 10101: 2 diff, 1 swap
        - 11100 -> 01010: 3 diff => impossible
    - 所以當n是奇數長度時, 是不可能會有奇數個diff的, 所以如果我們計算出奇數個diff, 代表當前的pattern是不可能達成的.所以我們得幾算另一種pattern, 次數就是n-diff

[video explanation by @HuifengGuan](https://www.youtube.com/watch?v=t0eV9eiA3eg&ab_channel=HuifengGuan)