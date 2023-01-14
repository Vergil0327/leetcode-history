class RandomizedCollection:
    def __init__(self):
        self.pool = []
        self.val2idx = defaultdict(set)

    def insert(self, val: int) -> bool:
        val2idx, pool = self.val2idx, self.pool
        
        existed = val in val2idx
        val2idx[val].add(len(pool))
        pool.append(val)
        
        return not existed

    def remove(self, val: int) -> bool:
        val2idx, pool = self.val2idx, self.pool
        if val not in val2idx: return False

        n = len(pool)
        if val == pool[n-1]:
            val2idx[val].remove(n-1)
            if not val2idx[val]: del val2idx[val]
            pool.pop()
            return True

        i = next(iter(val2idx[val]))
        val2idx[val].remove(i)
        if not val2idx[val]: del val2idx[val]

        val2idx[pool[n-1]].remove(n-1)
        val2idx[pool[n-1]].add(i)
        pool[i], pool[n-1] = pool[n-1], pool[i]
        pool.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.pool)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()