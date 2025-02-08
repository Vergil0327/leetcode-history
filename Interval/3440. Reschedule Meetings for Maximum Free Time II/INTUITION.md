# Intuition

從example 3可看出, 我們要做的就是挑出一個時間區段, 然後:
1. 如果前後有任何一段gap可以容納, 那移走後當前能騰出的`free time gap = gap_before + (endTime[i]-startTime[i]) + gap_after`
2. 如果沒地方能移, 那當前就只能將前後兩個gap相連, free time gap = gap_before + gap_after

因此, 最簡單的做法就是用兩個`SortedList`去儲存前後兩端的gap
並在遍歷每段時間時維護並計算即可

```py
def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
    startTime += [eventTime]
    endTime += [eventTime]
    n = len(startTime)

    gaps = SortedList()
    gaps_after = SortedList()
    for i in range(n-1):
        gaps_after.add(startTime[i+1] - endTime[i])

    res = prev = 0
    for i in range(n):
        duration = endTime[i] - startTime[i]
        gap = startTime[i] - prev
        
        if i+1<n:
            gaps_after.remove(startTime[i+1]-endTime[i])

        if gaps.bisect_left(duration) < len(gaps) or gaps_after.bisect_left(duration) < len(gaps_after):
            res = max(res, gap + duration + (startTime[i+1]-endTime[i] if i+1<n else 0))
        else:
            res = max(res, gap + (startTime[i+1]-endTime[i] if i+1<n else 0))

        gaps.add(gap)
        prev = endTime[i]
    return res
```

time: O(nlogn)
space: O(n)

# Optimization

但仔細觀察會發現還有可以優化的地方
由於對於任何一個時間區間[startTime[i], endTime[i]], 我們關注的只有前後有沒有能容納的gap
所以其實我們並不需要排序, 我們只需要知道prefix max gap跟suffix max gap即可

```py
def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
    gaps = [startTime[i] - (endTime[i-1] if i > 0 else 0) for i in range(len(startTime))]
    gaps.append(eventTime - endTime[-1])
    
    prefix_max = [0]
    for gap in gaps[:-1]:
        prefix_max.append(max(prefix_max[-1], gap))
    
    suffix_max = [0]
    for gap in reversed(gaps[1:]):
        suffix_max.append(max(suffix_max[-1], gap))
    suffix_max = suffix_max[::-1]
    
    max_gap = max(gaps)
    for i in range(len(startTime)):
        duration = endTime[i] - startTime[i]
        left_gap = gaps[i]
        right_gap = gaps[i+1]
        max_gap = max(max_gap, left_gap + right_gap)
        if max(prefix_max[i], suffix_max[i+1]) >= duration:
            max_gap = max(max_gap, left_gap + right_gap + duration)
    return max_gap
```

time: O(n)
space:O(n)