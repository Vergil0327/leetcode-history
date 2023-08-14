# Intuition

一開始直覺想到的是:

對於`getTweetCountsPerFrequency`
- 我們共有`res = [0] * ((endTime-startTime)//duration+1)`這麼多結果
- 如果我們有個hashmap儲存每個時間點的各個tweetName有幾個的話, 我們就能遍歷`t` from startTime to endTime, 更新res[(t-startTime)//duration] += self.hashmap[t][tweetName]

- 所以我們的`recordTweet`就必須更新`self.timeline[time][tweetName] += 1`

但由於`0 <= time, startTime, endTime <= 10^9`, 這樣會MLE
所以我們必須反過來, 我們的hashmap紀錄每個tweet出現在哪些時間點, 所以對於:
- `recordTweet`, 我們更新`self.tweets[tweetName].append(time)`
- `getTweetCountsPerFrequency`, 我們就能藉由`[t for t in self.tweets[tweetName] if startTime <= t <= endTime]`找出所有時間, 並更新`res[(t-startTime)//duration] += 1`