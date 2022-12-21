# Greedy

## Intuition

首先對`startTime`由小到大排序，再對`endTime`由大到小排序
對區間排序後，每次都往後從所有重疊的區間裡，找出`endTime`最大的區間作為下一個選擇

## Approach

因為我們有對`endTime`做排序，所以保證取的第一個一定`endTime`最大，然後再以第一個區間用while-loop往後從重疊區間中找出下一個`endTime`最大的區間

如果找不到下個重疊區間可以擴展我們想cover的區間，那就直接返回-1

```python
if currMaxEndTime != -inf:
    coverEndTime = currMaxEndTime
else:
    # 找不到下個重疊區間可以延展coverEndTime，代表區間有斷層
    # 那就直接返回-1
    return -1
```

如果cover的區間已經包含目標`Time`，直接返回計數

```python
if coverEndTime >= time: return cnt
```

## Complexity

- time complexity:

$$O(nlogn)$$

- space complexity:

$$O(1)$$

## Further

另外這題還有DP的解法 [here](https://leetcode.com/problems/video-stitching/solutions/707876/c-dp-solution-explained-thoroughly/?orderBy=most_votes)