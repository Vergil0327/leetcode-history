[Original Post](https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/solutions/2899594/python-3-solution-with-explanation-heap-binary-search/)

# Intuition

主要概念是我們預先計算，透過一次的BFS獲得所有資訊

單次query來看，分數必須strictly greater than才能計算進去，因此我們這邊改用`min heap`來進行BFS，這樣我們的BFS在遍歷過程中會由小到大前進，並將結果存進`order` array裡

例如 example 1.
grid = [[1,2,3],[2,5,7],[3,5,1]]
queries = [5,6,2]

```python
order = [1, 2, 2, 3, 3, 5, 5, 1, 7]
```

當`query＝2`時，我們只有idex=0是合法的，因此`ans=1`
當`query=5`時，index從0-4是合法的，因此`ans=5`
當`query=6`時，index從0-7是合法的，`order[:8]`都小於query，因此`ans=8`

那這邊我們會看到這是個linear search，
我們可以`order`轉化成紀錄直到該index的最大值，因為假如你query=4，即使後面有個1你也BFS遍歷不到，所以我們只關心極值

轉化後`order`變為一個單調遞增的array
```python
order = [1, 2, 2, 3, 3, 5, 5, 5, 7]
```

如此一來我們便可以透過binary search，以O(logn)的時間找到有多少數值符合該次query

當`query=2`，`bisect.bisect_left=1`
當`query=5`，`bisect.bisect_left=5`
當`query=6`，`bisect.bisect_left=8`

## further reading

[BFS + PrefixSum](https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/solutions/2899355/bfs-prefix-sum/?orderBy=most_votes)