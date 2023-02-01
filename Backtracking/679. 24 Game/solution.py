class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        permutations = []
        def getPerm(state, bitmask):
            if len(state) == 4:
                permutations.append(state.copy())
                return
            for i in range(4):
                if (1<<i)&bitmask: continue
                bitmask |= (1<<i)
                getPerm(state + [cards[i]], bitmask)
                bitmask ^= (1<<i)
        getPerm([], 0) # or itertools.permutations(cards)

        def dfs(nums, l, r):
            if l == r: return {nums[l]}

            res = set()
            for i in range(l, r):
                left = dfs(nums, l, i)
                right = dfs(nums, i+1, r)
                for x in left:
                    for y in right:
                        res.add(x+y)
                        res.add(x-y)
                        res.add(x*y)
                        if y != 0:
                            res.add(x/y)
            return res

        PRECISION = 1e-10
        for nums in permutations:
            SET = dfs(nums, 0, 3)
            for res in SET:
                if abs(res-24) < PRECISION: return True
        return False