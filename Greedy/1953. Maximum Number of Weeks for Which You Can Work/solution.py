class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total = sum(milestones)
        mx = max(milestones)
        
        if mx > total//2:
            return (total-mx)*2+1
        else:
            return total