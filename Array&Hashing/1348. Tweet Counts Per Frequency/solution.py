MINUTE, HOUR, DAY = 60, 3600, 86400
class TweetCounts:

    def __init__(self):
        # self.timeline = defaultdict(lambda: defaultdict(int))
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        # self.timeline[time][tweetName] += 1
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        duration = MINUTE
        if freq == "hour":
            duration = HOUR
        elif freq == "day":
            duration = DAY

        res = [0] * ((endTime-startTime)//duration+1)
        # for t in range(endTime-startTime+1):
        #     res[t//duration] += self.timeline[t+startTime][tweetName]
        # return res

        for t in self.tweets[tweetName]:
            if startTime <= t <= endTime:
                res[(t-startTime)//duration] += 1
        return res
