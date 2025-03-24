class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        presum_skill = list(accumulate(skill, initial=0))

        finish_t = [0] * n
        for j in range(m):
            require_t = 0
            for i in range(n):
                # next_finish_t = finish_t[i] + sum(skill[j] for j in range(i, n)) * mana[j]
                next_finish_t = finish_t[i] + (presum_skill[n]-presum_skill[i]) * mana[j]
                require_t = max(require_t, next_finish_t)
            
            finish_t[-1] = max(finish_t[-1], require_t)
            for i in range(n-2, -1, -1):
                finish_t[i] = finish_t[i+1] - skill[i+1] * mana[j]

        return finish_t[-1]