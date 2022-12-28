class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)

        dp = []
        tails = []
        for obstacle in obstacles:
            i = bisect.bisect_right(tails, obstacle)
            dp.append(i+1)

            if i == len(tails):
                tails.append(obstacle)
            else:
                tails[i] = obstacle
        return dp
