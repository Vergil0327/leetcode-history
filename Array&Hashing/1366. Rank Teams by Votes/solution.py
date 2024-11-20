class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        rank = defaultdict(lambda: [0] * n)
        
        for v in votes:
            for i in range(n):
                rank[v[i]][i] += 1

        # If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.
        # => sort in alphabetically first
        teams = sorted(rank.keys())
        
        return "".join(sorted(teams, key=lambda x:rank[x], reverse=True))
                