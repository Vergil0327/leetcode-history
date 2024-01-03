# Intuition

num=43219, k = 4, can swap k times, answer is 13429

```
[XXXXXXXX]XXXXXXX
  k+1-size
```

首先我們貪心做法是: 持續在k-size這window裡, 由小到大, 範圍[0,9]挑一個最小的digit, 然後加到result string上

[43219]XXX => k -= 3, res = 1 + [4329]XXX

[43]29XXX => k -= 1, res = res + 3 + [429]XXX

移過去後, 剩餘的字符位置僅往右移, 但相對位置不變

所以我們可以遍歷index位置[0,n), 然後由小到大從0到9, 找看看能不能往右找到一個digit是在這k+1-size window內的

因此我們可以用個hashmap紀錄每個digit的index
那這樣我們就能透過hashmap[digit] = [idx1, idx2, ...]知道當前最靠左的index為idx1
也就是維護一個 hashmap{digit: deque of indices}
一但有個digit位於**idx1**, 且在這個k-size window之內, 那就代表我們可以append digit到result string上
然後我們再把這個idx1從deque中pop掉, 就能持續維護一個單調遞增的array並能以O(1)時間查找目前最靠i的index

想法有了, 但要如何正確更新`k`?

如果當前選擇要左移的num[i]的index為`idx`, 一開始的話放的位置是index=0
那麼`k -= idx - 0`, 但這個0並非一直不變

有可能你在左移num[i]之前, 已經有其他num[i]先左移過了

XXXXX num[i] XXXXX => YYYXXXXX <-num[i] XXXXX => YYY num[i] XXXXX ...

由於前面已經放置了3個左移的`YYY`
那這樣你只是從原本index=i的位置只移動到了index=3的位置
實際上只左移了**i-3**, 所以`k -= i-3`

由於我們至始至終都是貪心地由小到大放置digit
所以我們要維護一個數據結構能讓我們快數查找num[:i]裡有多少比當前digit位置還小的digit
假設是`x`, 這個`x`就是已經左移的數, 因此更新`k -= i-x`

為了快數查找一個區間內有多少小於當前digit的數, 由於目的是區間查找, 所以我們可以用**segment tree**

我們每找到一個合適的digit, 就在segment tree上標記這個seg[index] += 1
這樣我們後續查找時, 就能查seg[0:i]範圍內有多少個已經左移的digit, `k -= i-seg.countLessThan(i)`

```py
class SegmentTree:
    def __init__(self, n, op=sum):
        self.n = n
        self.st = st = [0]*(2*n)
        self.op = op

    def __getitem__(self, i):
        return self.st[i+self.n]
    def __setitem__(self, i, v):
        st, op, n = self.st, self.op, self.n
        i += n
        st[i] = v

        while i:
            st[i>>1] = op([st[i], st[i^1]])
            i >>= 1

    def countLessThan(self, pos):
      st, op, n = self.st, self.op, self.n
      l,r = n, pos+n

      res = 0
      while l <= r:
          if l == r:
              res = op([res, st[l]])
              break
          if l&1 == 1:
              res = op([res, st[l]])
              l += 1
          if r&1 == 0:
              res = op([res, st[r]])
              r -= 1
          l, r = l>>1, r>>1

      return res

seg = SegmentTree(n)
```

所以整體框架為:

```py
n = len(num)
position = defaultdict(deque)
for i in range(n):
    position[num[i]].append(i)

seg = SegmentTree(n)        
res = ""
for i in range(n):
    for d in range(10):
        d = str(d)
        if len(position[d]) > 0:
            pos = position[d][0]
            shift = seg.countLessThan(pos)
            
            if (swap := pos - shift) <= k:
                res += d
                
                k -= swap
                seg[pos] = seg[pos] + 1
                position[d].popleft()
                break
return res
```

總結:

1. 至少得想到greedy, 由小到大擺放digit 0~9, 並用hashmap確認能不能存在
2. 正確更新`k`, 得知道會有個shift/offset的存在, k = i - shift

time: $O(nlogn)$
space: $O(n)$