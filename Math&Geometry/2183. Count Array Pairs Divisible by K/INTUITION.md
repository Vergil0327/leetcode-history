# Intuition

nums[i]*nums[j] % k == 0 => nums[i]*nums[j]因數有k
=> 找出nums[i]所有能整除`k`的因數, 將k去除這些因數後剩下的k'必須存在於nums[j]裡
  => nums[j]必須包含`k // gcd(nums[i], k)`

所以如果有個hashmap存有**因數有k // gcd(nums[i], k)的所有數**的話
我們就能知道nums[i]有多少個nums[j]可以配對

先找出`k`的所有可能因數, 然後再將nums[i]分類
```py
n = len(nums)

Kfactors = set()
for i in range(1, int(sqrt(k))+1):
    if k%i != 0: continue
    Kfactors.add(i)
    Kfactors.add(k//i)

# groups: {common divisor with k: indices}
groups = defaultdict(list)
for i in range(n):
    for f in Kfactors:
        if nums[i]%f == 0:
            groups[f].append(i)
```

然後在遍歷nums[i]找出含有**k//gcd(nums[i], k)**的數即可