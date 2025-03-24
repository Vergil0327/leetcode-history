# Intuition

brute force simulation很好想, 但會TLE
那比較顯而易見的優化就是我們將[l,r]範圍壓縮到**log**等級
對於`i in range(l, r+1)`, 他的操作數為`floor(log(i, 4)) + 1`
有了這個後, 我們就能縮小scale, 然後在同樣進行模擬

```py
# brute force
def minOperations(self, queries: List[List[int]]) -> int:
    res = 0
    for l, r in queries:
        
        nums = SortedList(range(l, r+1))

        count = 0
        while len(nums) > 1:
            x = nums.pop()
            y = nums.pop(0)
            if x//4 > 0:
                nums.add(x//4)
            if y//4 > 0:
                nums.add(y//4)
            
            count += 1
        if nums:
            x = nums[0]
            while x > 0:
                x //= 4
                count += 1
        res += count
    return res
```

對於原本的範圍`[l, r] = queries[i]`, 我們可以壓縮到[start, end] where start = floor(log(l, 4))+1, end = floor(log(r, 4))+1
這個`[start, end]`就是操作數的可能範圍, 那再來就是遍歷這段範圍來計算每個操作數能貢獻多少個數在原本的[l,r]裡

但這邊我們遍歷範圍改成`[start-1,end]`, 因為原本的`l`不一定剛好是4^x, 也可能是4^x+1, 4^x+2, 4^x+3
為了計算每個操作數涵蓋的interval, 所以我們遍歷範圍往外拓展一點

所以對於當前的`queries[i]`, 我們可以計算總共需要多少操作數:

```py
for l, r in queries:
    start = floor(log(l, 4))+1
    end = floor(log(r, 4))+1
    ops = 0
    for p in range(start-1, end+1):
        interval = [max(l, pow(4, p)), min(r, pow(4, p+1)-1)]

        op = p+1
        ops += max(0, op * (interval[1]-interval[0]+1))
```

由於我們可以兩個配對一起操作, 所以對於每個queries[i]來說
真正所需的操作數為: `res += ceil(ops/2)`