from random import randint

# follow-up of 380. Insert Delete GetRandom O(1)
class Solution:

    # O(n)
    def __init__(self, n: int, blacklist: List[int]):
        self.poolsize = n-len(blacklist)
        self.pool = {}
        
        # target: pick num from [0, n-len(blacklist)-1]
        # construct mapping by swapping num in blacklist with pool's last valid num
        blackSet = set(blacklist)
        lastNum = n-1
        for bck in blacklist:
            # we only need to consider blacklist within our pick range [0, n-len(blacklist)-1]
            if bck < self.poolsize:
                while lastNum in blackSet:
                    lastNum -= 1
                self.pool[bck] = lastNum
                lastNum -= 1

    # O(1)
    def pick(self) -> int:
        n = randint(0, self.poolsize-1)
        return self.pool.get(n, n) # return mapping value if n is in blacklist else n itself




# concise version
class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        blacklist = set(blacklist)  #to avoid TLE
        self.N = N - len(blacklist) #to be used in pick()
        key = [x for x in blacklist if x < N-len(blacklist)]
        val = [x for x in range(N-len(blacklist), N) if x not in blacklist]
        self.mapping = dict(zip(key, val))

    def pick(self) -> int:
        i = randint(0, self.N-1)
        return self.mapping.get(i, i)