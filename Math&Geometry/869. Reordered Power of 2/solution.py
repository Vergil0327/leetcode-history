class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        for perm in permutations(str(n)):
            if len(perm) > 1 and perm[0] == "0": continue # invalid
            num = int("".join(perm))
            x = int(log2(num))
            if pow(2, x) == num: return True
        return False

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def key(num):
            s = str(num)
            key = [0]*10
            for d in s:
                key[int(d)] += 1
            return tuple(key)
        
        target = key(n)
        
        # n <= 10^9
        upperbound = ceil(log2(10**9))
        for x in range(upperbound):
            num = str(pow(2, x))
            if key(num) == target: return True
        return False