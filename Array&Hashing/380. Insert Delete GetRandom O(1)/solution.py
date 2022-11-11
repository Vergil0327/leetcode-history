# https://labuladong.github.io/algo/2/20/33/

import random
class RandomizedSet:

    def __init__(self):
        self.len = 0
        self.valToIdx = {}
        self.pool = []

    def insert(self, val: int) -> bool:
        if val in self.valToIdx:
            return False

        self.pool.append(val)
        self.valToIdx[val] = self.len
        self.len += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valToIdx:
            return False
        
        # get key of val and remove from hashmap
        i = self.valToIdx[val]
        
        # update index
        self.valToIdx[self.pool[self.len-1]] = i
        
        # swap target with last element and pop. O(1)
        self.pool[i], self.pool[self.len-1] = self.pool[self.len-1], self.pool[i]
        self.pool.pop()
        
        # remove val's index
        self.valToIdx.pop(val)
        self.len -= 1 # update len
        
        return True


    def getRandom(self) -> int:
        i = random.randint(0, self.len-1)
        return self.pool[i]
