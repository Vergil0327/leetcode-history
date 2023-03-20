class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)

        # 1-indexed, dp[i]: the minimum number of trips for first i boxes
        dp = [inf] * (n+1)
        
        # base case: minimum number of 0 trip
        dp[0] = 0
        
        # shift boxes to 1-indexed match with dp
        boxes = [[-1, 0]] + boxes

        j = trips = weight = 0
        lastPort, lastJ = -1, 0
        for i in range(1, n+1):
            # 1. ship boxes as many as possible
            while j+1 <= n and weight + boxes[j+1][1] <= maxWeight and (j+1)-i+1 <= maxBoxes:
                j += 1
                weight += boxes[j][1]
                if boxes[j][0] != boxes[j-1][0]:
                    trips += 1
                if lastPort != boxes[j][0]:
                    lastPort = boxes[j][0]
                    lastJ = j

            # dp[j] = dp[i] + trips[i:j]
            dp[j] = min(dp[j], dp[i-1] + trips + 1)

            # 2. if boxes[i][0] is same with boxes[i+1][0], we can try to group them together to next trip
            if j+1 <= n and boxes[j][0] == boxes[j+1][0]:
                # dp[lastj-1] = dp[i-1] + trips[i:lastj-1]
                dp[lastJ-1] = min(dp[lastJ-1], (dp[i-1] + trips + 1) - 1) # 最後面跟下一趟併再一起，所以-1
                
            weight -= boxes[i][1]
            if i+1 <= n and boxes[i][0] != boxes[i+1][0]:
                trips -= 1
                
        return dp[n]        

# 1. ship boxes as many as possible
# 2. if boxes[i][0] is same with boxes[i+1][0], we can try to group them together to next trip

# [X] X X X X X
#  i
# [X X] X X X X
#  i
# [X X X] X X X
#  i
# [X X Y] Y Y X
#  i
# [X X] [Y Y Y] X
#  i
