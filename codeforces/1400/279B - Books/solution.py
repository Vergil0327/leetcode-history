n, t = list(map(int, input().split()))
nums = list(map(int, input().split()))

# from problem description,
# we need to find max subarray size when subarray sum <= t

l = r = res = time = 0
while r < n:
    time += nums[r]
    r += 1

    while l < r and time > t:
        time -= nums[l]
        l += 1

    res = max(res, r-l)
print(res)