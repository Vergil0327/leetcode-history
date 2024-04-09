# Intuition

題意:

```py
n = len(nums)
res = 0
for i in range(n):
    for j in range(i):
        if low <= nums[i]^nums[j] <= high:
            res += 1
return res
```

對於這種找出所有可能pair的, 我們可以試著反著想
試著觀察看看能否單獨一個個找出每個nums[i]能有多少合法pair, 然後再加總起來

low <= nums[j]^nums[i] <= high

所以對於每個nums[i], 我們只要利用上面這個條件, 找出合法nums[j]的數量加總起來
即可找出有多少個合法pair
那麼為了找出範圍內的nums[j], 我們可以拆分成: countXorLessThan(high+1) - countXorLessTHan(low)

這時想到如果是find maximum XOR with an element in array => Trie
或許也可以用Trie的特性去找出有多少nums[j] XOR nums[i]是lower than high或low-1

概念上框架是:

```py
n = len(nums)

res = 0
root = Trie()
for i in range(n):
    hi = root.count(nums[i], high+1)
    lo = root.count(nums[i], low)
    res += hi-lo
    root.add(nums[i])
return res
```

所以trie.count(nums[i], threshold)要找的就是所有跟nums[i]進行XOR操作後, 小於threshold的數, 這些數都是合法nums[j]
因此:

我們從高位往低位找, 對於當前i-th bit
1. x = (nums[i]>>i)&1
2. t = (threshold>>i)&1

我們希望找到x XOR y < t (threshold), 其中y來自(nums[j]>>i)&1, 這時我們就看trie:

1. t == 1: 如果threshold的bit是1
    1. 如果x=1:
        - 對於當前bit是1的nums[j]: 1 XOR 1 = 0 < 1 = threshold => 代表接下來不管bits為如何, 所有的nums[j]跟nums[i]進行XOR後都小於threshold. 全都是小於threshold合法nums[j]
        - 對於當前bit是0的nums[j]: 1 XOR 0 = 1 == 1 = threshold => 繼續遞歸看下個bits, 找出合法nums[j]
    2. 如果x=0:
        - 對於當前bit是0的nums[j]: 0 XOR 0 = 0 < 1 => 此後所有可能的nums[j]跟nums[i]XOR後都是小於threshold的
        - 對於當前bit是1的nums[j]: 0 XOR 1 = 1 == 1 = threshold => 繼續遞歸看下個bit, 找出小於threshold的nums[j]
2. t == 0: 同理

所以我們可以得出

```py
def count(self, num, threshold):
    root = self.root
    res = 0
    for i in range(31, -1, -1):
        x = (num>>i)&1
        t = (threshold>>i)&1

        if t == 1:
            if x == 1:
                # 1 XOR y ? 1 = threshold
                if 1 in root.next:
                    res += root.next[1].cnt # y = 1

                if 0 in root.next:
                    root = root.next[0] # y = 0
                else:
                    break
            if x == 0:
                # 0 XOR y ? 1 = threshold
                # y=0 -> 0 XOR 0 < 1 = threshold
                if 0 in root.next:
                    res += root.next[0].cnt

                # y=1 -> 0 XOR 1 = 1 = threshold => 繼續遞歸看下個bit位
                if 1 in root.next:
                    root = root.next[1]
                else:
                    break
        else:
            if x == 1:
                # 1 XOR y ? 0=threshold
                # y = 0 -> 1 XOR 0 = 1 > 0 threshold => 此路找不到合法nums[j]

                # y = 1 -> 1 XOR 1 = 0 == 0 threshold => 繼續看下個bit
                if 1 in root.next:
                    root = root.next[1]
                else:
                    break
            if x == 0:
                # 0 XOR y ? 0=threshold
                # y = 0 -> 0 XOR 0 = 0 == 0 threshold => 繼續遞歸看下個bit
                if 0 in root.next:
                    root = root.next[0]
                else:
                    break
                # y = 1 -> 0 XOR 1 = 1 > 0 threshold => 此後找出的nums[j]都無法使得nums[i]^nums[j] <= threshold
    return res
```


time: O(n * log(32))