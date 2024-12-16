class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return 0

        res = 0

        z1 = z_function(nums)
        for i in range(1, n):
            if z1[i] >= i:
                res += n - 2*i
                maxSize = 2*i
            else:
                maxSize = n

            z2 = z_function(nums[i:])
            for j in range(i+1, maxSize):
                if z2[j-i] >= j-i:
                    res += 1
        return res

def z_function(s):
    n = len(s)
    l = r = 0
    z = [0]*n

    for i in range(1, n):
        if i < r:
            z[i] = min(r-i, z[i-l])

        while i + z[i] < n and s[z[i]] == s[i+z[i]]:
            z[i] += 1
        if i+z[i] > r:
            l = i
            r = i+z[i]
    return z
