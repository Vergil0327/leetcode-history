class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # dp[state]: the minimum possible size of sufficient team to satisfy state
        # use binary to represent current req_seills. 1001 means [req_skills[0], req_skills[3]]

        n, m = len(req_skills), len(people)
        dp = [inf] * (1<<n)
        dp[0] = 0

        skill2idx = {skill: i for i, skill in enumerate(req_skills)}
        peopleSkills = []
        for p in people:
            state = 0
            for skill in p:
                state |= (1<<skill2idx[skill])
            peopleSkills.append(state)

        res = defaultdict(set)
        for state in range(1<<n):
            for i, personSkills in enumerate(peopleSkills):
                next_state = state | personSkills
                if dp[state]+1 < dp[next_state]:
                    dp[next_state] = dp[state]+1
                    res[next_state] = res[state] | {i}
        return list(res[(1<<n)-1])