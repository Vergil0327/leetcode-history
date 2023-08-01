class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.stack = stack = [] # [time, winner]

        votes = defaultdict(int)
        mx = -1
        for i in range(len(times)):
            votes[persons[i]] += 1

            if votes[persons[i]] > mx:
                mx = votes[persons[i]]
                stack.append([times[i], persons[i]])
            elif votes[persons[i]] == mx:
                stack.append([times[i], persons[i]])
            else:
                stack.append([times[i], stack[-1][1]])
        

    def q(self, t: int) -> int:
        i = bisect.bisect_right(self.times, t)
        
        return self.stack[i-1][1]
