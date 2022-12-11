# Brute Force
class Allocator:

    def __init__(self, n: int):
        self.cap = n
        self.size = 0
        self.memo = [-1]*n
        

    def allocate(self, size: int, mID: int) -> int:
        if self.size + size > self.cap: return -1
        memo = self.memo
        require = -1 * size
        for i in range(self.cap):
            if i+size > self.cap: return -1

            # find available consecutive blocks
            if sum(memo[i:i+size]) == require:
                for j in range(i, i+size):
                    memo[j] = mID
                    self.size += 1
                return i
        return -1

    def free(self, mID: int) -> int:
        cnt = 0
        for i in range(self.cap):
            if self.memo[i] == mID:
                cnt += 1
                self.memo[i] = -1
        self.size -= cnt
        return cnt

# Sliding Window
class Allocator:

    def __init__(self, n: int):
        self.cap = n
        self.size = 0
        self.memo = [-1]*n
        

    def allocate(self, size: int, mID: int) -> int:
        if self.size + size > self.cap: return -1
        memo = self.memo
        
        l, r = 0, 0
        avai = 0
        idx = -1
        while r < self.cap:
            num = memo[r]
            r += 1

            if num == -1:
                avai += 1
                if avai == size:
                    idx = l
                    break
            else:
                avai = 0
                l = r

        if idx != -1:
            for j in range(idx, idx+size):
                memo[j] = mID
            self.size += size
        return idx

    def free(self, mID: int) -> int:
        cnt = 0
        for i in range(self.cap):
            if self.memo[i] == mID:
                cnt += 1
                self.memo[i] = -1
        self.size -= cnt
        return cnt
