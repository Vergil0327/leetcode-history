# Intuition

如果操作數`y`次可以使得s符合, 那麼`y+1`次肯定也能使得s符合
如果`y`次不行, 那麼你給我`y-1`次也肯定不行
既然有這種單調性質的話, 那麼最小操作數可以試著用binary search去猜看看

那這樣的話, 問題就變成binary search中的check function該怎麼做

對於中間連續x個1:

假設limit length=2, 那代表每連續**3**個數就必須操作一次插入一個隔板

```
x=5
000 11111  000
000 11011  000

x=6
000 111111 000
000 110101 000

x=7
000 1111111 000
000 1101101 000
```

可看出所需操作數為: `consecutive // (limit_length+1)`

因此整體框架為:

```py
l, r = 1, n
while l < r:
    mid = l + (r-l)//2
    if check(mid):
        r = mid
    else:
        l = mid+1
return l
```

```py
arr = [len(list(consecutive)) for _, consecutive in groupby(s)]

def check(target_len):
    return sum(length//(target_len+1) for length in arr) <= numOps
```

但會發現target_len==1時, 會是edge case, 需要單獨處理

target_len=1, 代表要將s轉成"010101..."或"101010..."
因此就計算diff就好, 然後看轉成"010101..."跟"101010..."哪個所需操作較低, 選低的

```py
if target_len == 1: # should be alternate "010101..." or "101010..."
    x = sum(int(ch) != i % 2 for i, ch in enumerate(s)) # check diff compared with "01010101..."
    # then, diff compared with "101010..." is len(s)-x
    return min(x, len(s) - x) <= numOps
```