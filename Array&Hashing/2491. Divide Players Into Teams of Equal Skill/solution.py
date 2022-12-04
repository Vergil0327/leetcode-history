# count & find its complement
# O(n)
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        groups = len(skill)//2
        total = sum(skill)
        if total % groups != 0: return -1
        
        target = total // groups
        counter = Counter(skill)

        res = 0
        for i in range(len(skill)):
            num = skill[i]
            if counter[num] == 0: continue
            counter[num] -= 1
            
            other = target-num
            if counter[other] < 1: return -1
            counter[other] -= 1

            res += num * other

        return res


# Two-Pointer Solution: solution by hints
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        groups = len(skill)//2
        total = sum(skill)
        if total % groups != 0: return -1
        
        target = total // groups

        skill.sort()
        l, r = 0, len(skill)-1
        res = 0
        while l < r:
            if skill[l] + skill[r] != target: return -1
            res += skill[l] * skill[r]
            l, r = l+1, r-1
        return res