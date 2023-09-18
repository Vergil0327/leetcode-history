# Intuition

一開始比較直覺想到的是:

如果我們維護兩個pointer, 指向最右可`pop`的位置以及最左可`push`的位置
這樣就能O(1)時間進行`pop`跟`push`

但由於`popAtStack`的關係, 會必須要在push及pop後更新這兩個pointer
使得我們必須用個**while-loop**來找尋下個位置, 一但中間有大量full stack的話
將會使得O(1)變為O(n)而因此TLE

```py
class DinnerPlates:

    def __init__(self, capacity: int):
        self.plate = defaultdict(list)
        self.l, self.r = 0, -1
        self.cap = capacity

    def push(self, val: int) -> None:
        plate = self.plate
        plate[self.l].append(val)
        while len(plate[self.l]) == self.cap:
            self.l += 1

        if len(plate[self.l]) == 0:
            self.r = max(self.r, self.l-1)
        else:
            self.r = max(self.r, self.l)

    def pop(self) -> int:
        if self.r == -1: return -1
        
        return self.popAtStack(self.r)

    def popAtStack(self, index: int) -> int:
        plate = self.plate
        if not plate[index]: return -1
        
        el = plate[index].pop()

        if index == self.r and len(plate[index]) == 0:
            while self.r >= 0 and len(plate[self.r]) == 0:
                self.r -= 1

        self.l = min(self.l, index)
        return el
```

由於我們需要很快知道最左可push的index, 因此我們可以用個**min heap**來儲存所有avaialbe index
至於最右可pop的stack, 其實我們就用一個stack來儲存所有stack即可, 不需要用hashmap

那這樣對於`push`來說:

先把invalid index移除掉
```py
while self.canPush and self.canPush[0] < len(plate) and len(plate[self.canPush[0]]) == self.cap:
    heapq.heappop(self.canPush)
```

再來如果**min heap**空了, 那就加入下個stack的index, `len(plate)`
此時如果**min heap[0]**的index就是`len(plate)`, 代表目前為止的plate都是滿的stack
所以在加入一個新的
```py
if self.canPush[0] == len(plate):
    plate.append([])
```

當所有前置作業準備完後
我們就可以將當前`val`加入到最左的non-full stack裡了
```py
plate[self.canPush[0]].append(val)
```

`pop`跟`popAtStack`則可以一起看, 由於`pop`只關心最右的空stack:
所以我們把不合法的empty stack都pop掉後, 在呼叫`self.popAtStack(len(plate) - 1)`即可

```py
def pop(self) -> int:
    plate = self.plate
    while plate and not plate[-1]:
        plate.pop()
    
    return self.popAtStack(len(plate) - 1)
```

至於`popAtStack`
我們先排除掉所有不合法的index以及plate[index]為空的情況後

直接執行`plate[index].pop()`並將`index`加入到`min heap`即可

所以本題的關鍵是必須想到leftmost可以用priority queue來快速查找
而rightmost就借用stack的特性即可

至於plate我們一開始是用hashmap, 但其實注意key不要越界的話, array也可以達到一樣效果

time:

push: O(logn)
popAtStack: O(logn)
pop: amortized O(1)
