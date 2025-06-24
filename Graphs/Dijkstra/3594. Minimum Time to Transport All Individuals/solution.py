class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        pq = [(0,0,0)] # (current_time, current_stage, bitmask_of_people_on_destination)
        minTime = [[float('inf')] * m for _ in range(1 << n)]
        minTime[0][0] = 0

        final_state = (1 << n) - 1  # All individuals have crossed the river
        while pq:
            t, stage, state = heapq.heappop(pq)
            if minTime[state][stage] < t: continue
            if state == final_state: return t

            remaining = (~state) & final_state
            
            # find subset state
            submask = remaining
            while submask > 0:
                if submask.bit_count() <= k:
                    # Calculate crossing time
                    crossing_time = max(time[i] for i in range(n) if submask & (1 << i)) * mul[stage]
                    new_state = state | submask
                    new_stage = (stage + int(crossing_time)) % m
                    new_time = t + crossing_time

                    if new_state == final_state:
                        if new_time < minTime[new_state][new_stage]:
                            minTime[new_state][new_stage] = new_time
                            heapq.heappush(pq, (new_time, new_stage, new_state))

                    else:
                        # If there are still individuals left, one must return
                        for i in range(n):
                            if new_state & (1 << i):
                                return_time = time[i] * mul[new_stage]
                                return_stage = (new_stage + int(return_time)) % m
                                new_state_with_return = new_state - (1 << i)
                                new_time_with_return = new_time + return_time

                                if new_time_with_return < minTime[new_state_with_return][return_stage]:
                                    minTime[new_state_with_return][return_stage] = new_time_with_return
                                    heapq.heappush(pq, (new_time_with_return, return_stage, new_state_with_return))
                
                # Move to the next subset
                submask = (submask-1)&remaining
        return -1.0
