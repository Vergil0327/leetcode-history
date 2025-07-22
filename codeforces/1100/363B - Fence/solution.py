[n, k] = input().split()
n, k = int(n), int(k)
 
nums = list(map(int, input().split()))
 
l = r = 0
h = float('inf')
res = cur = 0
while r < n:
    cur += nums[r]
    r += 1
 
    while l < r and r-l > k:
        cur -= nums[l]
        l += 1
 
    if r-l == k:
        if cur < h:
            h = cur
            res = l+1 # to 1-indexed
print(res)