# Intuition

由於我們要知道occruence, 所以我們用hashmap `numFreq`來紀錄目前有多少種freqeuncy
而我們的目標是移除一個element後numFreq == 1

所以首先: 如果numFreq > 2, 那移除一個element後, 至少還剩下2種freq => 肯定不符合我們要的

因此我們只要考慮numFreq==2 以及 numFreq==1這兩種情況:

- numFreq == 2:

合法情況1:
nums = aaa bbb ccc d
移除1個d後剩下的freq都是3

合法情況2:
nums = aaa bbb ccc dddd
移除1個d後剩下的freq都是3

- numFreq == 1:

合法情況1:
nums = xxxxxxxxx
移除一個x後, freq仍然只有一種

合法情況2:
nums = x y z a b c
移除任意一個數後, freq依然只有一種

由於len(nums) >= 2:
- both [X,X] and [X,Y] are valid case
- res至少是2

# Apporach

所以我們再用一個hashmap `freq`來紀錄每個`nums[i]`到目前為止出現幾次
並且同步更新目前有幾種frequency

另外我們用`numFreq`紀錄: {freq: hashset to store nums[i]}

```py
freq = defaultdict(int)
numFreq = defaultdict(set)
for i, num in enumerate(nums):
    if num in freq and num in numFreq[freq[num]]:
        numFreq[freq[num]].remove(num)
        if not numFreq[freq[num]]:
            del numFreq[freq[num]]

    freq[num] += 1
    numFreq[freq[num]].add(num)
```

再來就依序討論各種情況
- if len(numFreq) == 1:
  - `_, SET = next(iter(numFreq.items()))`
  - nums = xxxxxx:
    - found valid answer if `len(SET) == 1`
  - nums = a b c d e f
    - found valid answer if `len(SET) == i+1`
- if len(numFreq) == 2:
  - `arr = sorted(numFreq.items())`, sort by frequency
  - set1, set2 = arr[0][1], arr[1][1]
  - v1, v2 = next(iter(set1)), next(iter(set2))
  - nums = XXX YYY Z:
    - found valid length if `len(set1) == 1 and freq[v1] == 1`
  - nums = XXX YYY ZZZZ:
    - found valid length if `len(set2) == 1 and freq[v2]-1 == freq[v1]`

# Other Solution

這題也可以從後往前找, 找到的第一個valid length即為答案

```py
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq = Counter(nums)
        numFreq = defaultdict(int)
        for f in freq.values():
            numFreq[f] += 1

        for i in range(len(nums)-1, -1, -1):
            if len(numFreq) == 1:
                f, cnt = next(iter(numFreq.items()))
                # nums = xxxxxx or nums= x y z a b c
                if cnt == 1 or f == 1:
                    return i+1

            elif len(numFreq) == 2:
                tmp = sorted(numFreq.items()) # [freq, count]
                # nums = AAA XXX YYY ZZZZ
                if tmp[1][0] == tmp[0][0]+1 and tmp[1][1] == 1:
                    return i+1

                # nums = AAA XXX YYY Z
                if tmp[0][0] == 1 and tmp[0][1] == 1:
                    return i+1
            
            num, f = nums[i], freq[nums[i]]

            freq[num] -= 1
            if freq[num] == 0:
                del freq[num]

            numFreq[f] -= 1
            if numFreq[f] == 0:
                del numFreq[f]

            if f-1 > 0:
                numFreq[f-1] += 1

        return 2
```