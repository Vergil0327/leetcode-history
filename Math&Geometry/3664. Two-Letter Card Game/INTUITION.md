# Intuition

> note. Each cards[i] is composed of only lowercase English letters between 'a' and 'j'.

假設x="a"
並且card的第一位是"a", 那麼"a?"有:

1. aa: 可以跟任意其他含有"a"的配對(撇除自身), ex. aa + (a?, ?a)
2. a?: ab ac ad ae af ..., 這些可以內部自己配對, (ab, ac), (ab, ad), ..., 也能跟aa配對
3. ?a: ba ca da ea ..., 這些可以內部自己配對, 也能跟aa配對

這邊我們可以先計算**第2**跟**第3**類, 內部能配對出的compatible pairs
兩兩配對, 並計算最後剩餘多少, 剩餘部分可以跟"aa"配對

```py
def countPairs(count):
    sl = SortedList()
    for num in count:
        if num > 0:
            sl.add(num)
        
    pairs = 0
    while len(sl) > 1:
        a = sl.pop()
        b = sl.pop(0)
        pairs += 1
        a -= 1
        b -= 1
        if a > 0:
            sl.add(a)
        if b > 0:
            sl.add(b)
    return pairs, sum(sl)
```

透過helper function, 可以計算出2, 3類內部配對以及剩餘沒配對的
假設還剩下`x`個沒配對的, 這些可以在跟"aa"配對
所以還可配對出min(x, # of "aa")個compatible pairs

那到目前為止就知道, 總共有`p`個compatible pairs, 然後還剩下`# of "aa" - min(x, # of "aa")`個"aa"

最後這點比較tricky:
假設我們現在已有(ab, ac) compatible pair, 並且還剩下兩個"aa"
那麼我們可以將(ab, ac)換成:(ab, aa), (ac, aa)
這樣組合配對可以得到更多分

> 兩個"aa"可以拿來跟一組compatible pair多配一對, 如果有`p`組 compatible pairs, 在"aa"充分足夠的情況下也只能多額外配出`p`對
> 但如果"aa"不夠充分, 那最多就只能額外配出`# of "aa" / 2`

所以, 如果我們現在有`p`個compatible pairs, 以及剩下`m`個"aa"
那麼我們透過這樣的組合方式還可以額外得到: min(p, m // 2)的

因此最終計算為:

```py
pairs = remain = 0
for count in [countL, countR]:
    p, r = countPairs(count)
    pairs += p
    remain += r

used = min(wildcard, remain) # pair remaining with wildcards
wildcard -= used
extra = min(pairs, wildcard // 2) # split (a?, a?) with (a?, aa), (aa, a?) to earn more points
return pairs + used + extra
```

# Optimized

countPairs這邊還能更優化, 而且這邊有個要注意的地方是:

例如: arr = [1,2,2,3]這個case, expected: countPairs([1,2,2,3]) = 4
但如果直接拿max跟min持續配對, 會只配出3對並剩下同類型的2個而無法再配對

後來看到比較好的O(1) math solution為:

```py
def countPairs(count):
    s = sum(count)
    m = max(count)
    pairs = min(s - m, s // 2)
    remain = s - 2 * pairs
    return pairs, remain
```

- 如果max很大, 只能配出`s - m`
- 如果max很小, 每個數量都差不多, 那就能持續兩兩配對配出`s // 2`

```py
def countPairs(count: List[int]) -> Tuple[int, int]:
    total = 0
    max_count = 0
    for c in count:
        if c > 0:
            total += c
            if c > max_count:
                max_count = c
    
    if total == 0: return (0, 0)
    
    pairs = min(total - max_count, total // 2)
    remaining = total - 2 * pairs
    return (pairs, remaining)
```

Why It Works
The solution is elegant and efficient because it uses a mathematical approach to compute the maximum number of pairs without iteratively forming them. Let’s break it down step-by-step:

1. Edge Cases

- Empty List: if not count: return (0, 0) handles an empty input by returning no pairs and no remaining items.
- All Zeros: if total == 0: return (0, 0) ensures that if there are no items (sum of counts is 0), the function returns (0, 0).

These checks ensure correctness for trivial inputs.

2. Core Variables

- total: The sum of all counts (total = sum(c for c in count if c > 0)), representing the total number of items across all types.
- max_count: The maximum count of any single type (max_count = max(c for c in count if c > 0)), tracking the largest group of items of a single type.
- These are computed in a single pass through the input list, ignoring zeros for efficiency.

For the test case count = [1, 1, 2, 4, 0, 0, 0, 0, 0, 0]:

- Non-zero counts: [1, 1, 2, 4].
- total = 1 + 1 + 2 + 4 = 8.
- max_count = max(1, 1, 2, 4) = 4.

3. Computing Pairs
The number of pairs is calculated as:

```py
pairs = min(total - max_count, total // 2)
```
This is the key insight. Let’s unpack why this formula works:

- Constraint 1: total // 2
Each pair requires two items (one from each of two different types). The maximum number of pairs possible is limited by the total number of items divided by 2, since each pair consumes two items. Thus, total // 2 is the upper bound on pairs based on the total item count.

  - For total = 8, total // 2 = 8 // 2 = 4.


- Constraint 2: total - max_count
To form a pair, you need items from two different types. If one type has a very large count (e.g., max_count), it could limit the number of pairs because you need enough items from other types to pair with it. The sum of items from all other types is total - max_count. This represents the maximum number of pairs that can be formed, as each pair needs one item from the largest type and one from another type.

  - For max_count = 4, total - max_count = 8 - 4 = 4.


- Taking the Minimum:
The actual number of pairs is the minimum of these two constraints:

  - total // 2: Ensures we don’t exceed the total items available.
  - total - max_count: Ensures we have enough items from other types to pair with the largest type.
  - So, pairs = min(4, 4) = 4.



This formula elegantly captures the bottleneck: either we’re limited by the total number of items or by the availability of items from types other than the largest one.

4. Computing Remaining Items
The remaining items are calculated as:

```py
remaining = total - 2 * pairs
```

- Each pair consumes 2 items, so 2 * pairs items are used.
- Subtract this from the total to get the number of items left unpaired.
- For pairs = 4, remaining = 8 - 2 * 4 = 8 - 8 = 0.

Thus, the function returns (pairs, remaining) = (4, 0).

### Why the Formula is Correct

The formula pairs = min(total - max_count, total // 2) works because:

- Total items limit: total // 2 ensures we don’t try to form more pairs than we have items for.
- Type diversity limit: total - max_count ensures we have enough items from other types to pair with the largest type. If total - max_count is small, it means most items are in one type, limiting the number of pairs due to a lack of diverse types.