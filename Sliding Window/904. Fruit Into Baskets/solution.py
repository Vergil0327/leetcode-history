class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter = defaultdict(int)
        l = r = 0
        n = len(fruits)
        picked = 0
        res = 0
        while r < n:
            fruit = fruits[r]
            counter[fruit] += 1
            picked += 1
            r += 1

            while len(counter) > 2:
                counter[fruits[l]] -= 1
                if counter[fruits[l]] == 0:
                    del counter[fruits[l]]
                l += 1
                picked -= 1
            res = max(res, picked)
        return res