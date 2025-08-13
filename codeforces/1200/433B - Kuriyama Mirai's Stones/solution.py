from itertools import accumulate


n = int(input())
stones = list(map(int, input().split()))
m = int(input())

# type 1: use prefix sum (1-indexed)
# prefix_sum[r] - prefix_sum[l-1]

# type 2: sort before prefix sum
# sorted_presum[r] - sorted_presum[l-1]

presum1 = list(accumulate(stones, initial=0))
presum2 = list(accumulate(sorted(stones), initial=0))

for _ in range(m):
    query = list(map(int, input().split()))
    typ, l, r = query[0], query[1], query[2]

    if typ == 1:
        print(presum1[r]-presum1[l-1])
    elif typ == 2:
        print(presum2[r]-presum2[l-1])
