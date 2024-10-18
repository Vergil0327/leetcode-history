# Intuition

從數據規模看, brute force O(n^2)是肯定不行的
再來看到條件`0 <= deliciousness[i] <= 2^20`, 心想那這樣兩者相加, 最大也就2^21
代表最多就22種可能的power of 2, [0, 2^21]

這時想到: 或許我們可以從這個值域下手, 22 * O(n)數據規模上也是可行

所以就想到我們能不能遍歷所有可能的power of 2, 然後再以O(n)時間搜索

主框架為:

```py
res = 0
for p in range(22):
    target = pow(2, p)

    # TODO: found possible combination (i, j)
```

因此再來我們先計數 (相同的數不需要重複搜索)
得到所有不重複的deliciousness[i]後, 很直覺地能想到
我們只需要排個序, 就能用two pointers從左右兩端出發
就能以O(n)時間找出可能的`deliciousness[i] + deliciousness[j] == target`

找到`deliciousness[i] + deliciousness[j] == target`後, 我們分情況討論:
1. 如果**deliciousness[i] == deliciousness[j]**, 那就是`comb(count[deliciousness[i]], 2)` (C count[deliciousness[i]] 取 2)
2. 如果**deliciousness[i] != deliciousness[j]**, 那就是`count[deliciousness[i]] * count[deliciousness[j]]`

全部加總並對10^9+7取餘後即為答案

```py
count = Counter(deliciousness)
keys = list(sorted(count.keys()))
n = len(keys)

for p in range(22):
    target = pow(2, p)
    
    # two pointers搜索
    j = n-1
    for i in range(n):
        while j > i and keys[i] + keys[j] > target:
            j -= 1
        if j < i: break

        if keys[i] + keys[j] == target:
            if i == j:
                res += comb(count[keys[i]], 2)
            else:
                res += count[keys[i]] * count[keys[j]]
            res %= mod
```

time: O(22n + nlogn)
space: O(n)