class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        n = len(clips)
        clips.sort(key=lambda x:(x[0], -x[1]))
        coverEndTime = -inf
        count = 0

        i = 0
        while i < n:
            if coverEndTime == -inf:
                if clips[i][0] != 0: return -1 # 沒cover 0，直接返回-1
                coverEndTime = clips[i][1]
                i += 1
            else:
                # find largest endTime within overlapping intervals
                currMaxEndTime = -inf
                enterLoop = False
                while i < n and clips[i][0] <= coverEndTime:
                    enterLoop = True
                    if clips[i][1] > currMaxEndTime:
                        currMaxEndTime = clips[i][1]
                    i += 1

                if currMaxEndTime != -inf:
                    coverEndTime = currMaxEndTime

                # 如果有進去while-loop，跳出來後會是下個要比對的區間
                # 但如果沒有進去while-loop，如果不移動i的話會無限死循環
                if not enterLoop: i += 1 # avoid dead-loop
            count += 1
            if coverEndTime >= time: return count
        return -1

# Optimzed, without checking enterloop
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        n = len(clips)
        clips.sort(key=lambda x:(x[0], -x[1]))
        coverEndTime = -inf
        cnt = 0

        i = 0
        while i < n:
            if coverEndTime == -inf:
                if clips[i][0] != 0: return -1
                coverEndTime = clips[i][1]
                i += 1
            else:
                # find largest endTime within overlapping intervals
                currMaxEndTime = -inf
                while i < n and clips[i][0] <= coverEndTime:
                    if clips[i][1] > currMaxEndTime:
                        currMaxEndTime = clips[i][1]
                    i += 1

                if currMaxEndTime != -inf:
                    coverEndTime = currMaxEndTime
                else:
                    # 找不到下個重疊區間可以延展coverEndTime，代表區間有斷層
                    # 那就直接返回-1
                    return -1

            cnt += 1
            if coverEndTime >= time: return cnt
        return -1

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # dp[t]: minimum number of clips needed so that we can cover time interval [0, t]
        dp = [inf] * (time+1)
        dp[0] = 0

        for t in range(1, time+1):
            for start, end in clips:
                if start <= t <= end: # 代表我們可以選擇他來cover[start:t]，所以對dp[t]與dp[start]+1取最小次數
                    dp[t] = min(dp[t], dp[start]+1)
        return dp[time] if dp[time] != inf else -1