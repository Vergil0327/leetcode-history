class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        group = defaultdict(list)
        for val, lim in zip(value, limit):
            group[lim].append(val)
        
        score = 0
        for lim in sorted(group.keys()):
            size = min(len(group[lim]), lim)
            values = list(sorted(group[lim], reverse=True))
            score += sum(values[:size])

            
        return score