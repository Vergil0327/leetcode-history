# Intuition

sort by -growTime[i]
由於在生長的時候可以同步種植, 所以優先種植growTime較久的, 然在生長期間繼續種植其他盆

所以我們用time紀錄當前必須花費的sum(plantTime[:i])
然後再另外紀錄最晚的開花時間: lastGrowTime
所以對於第i-th盆花:

- time += plantTime[i]
- 真正開花時間為: lastGrowTime = max(lastGrowTime, time + growTime[i])

最後就看每盆花都種完後的lastGrowTime