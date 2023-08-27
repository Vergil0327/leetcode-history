# Intuition
if sum(nums) < target, we can directly return -1
else:
    target = 2^0 + 2^1 + ... + 2^n

we can see problem with binary representation

1. transform nums[i] into binary repr to see nums[i] can supply which bit and store every bit position's count

```py
bits = [0] * 32
for num in nums:
    bits[int(log2(num))] += 1
```

2. iterate total 32 bit from least significant bit
    - if target need this bit, i.e. (target>>i)&1 == 1
        - if bits[i] > 0, directly use it and bits[i] -= 1
        - else we need do operations in larger bit we have which means bits[j] > 0 and j > i
            - since we get 2 bits[j-1] after we do operations to bits[j], we can cover all the bits[j], bits[j+1], ..., bits[i-1]. thus we only need to record minimum bit target need

```py
need = inf
for i in range(32):
    if (target>>i)&1:
        if bits[i]:
            bits[i] -= 1
        else:
            need = min(need, i)

    if bits[i] and need < i:
        bits[i] -= 1
        res += i-need
        need = inf # reset
```

3. recycle unused sum

for each iteration: `bits[i+1] = bits[i]//2`

because if we already have two 4, and target need 8 subsequence sum, we don need to do operation until we get 8, we should directly take two 4.