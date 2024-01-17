# Greedy - Priority Queue

## Intuition

根據題目敘述，如果我們數值大過鄰居的話，糖果數必須比鄰居還多
因此我們可以優先找出最小rating，然後從小到大依序發放糖果，逐漸遞增上去

**因此我們需要能夠快速找到目前最小值的方法**

每次發放糖果時，跟左右鄰居數值做比較：
- 如果數值比鄰居大，那糖果必須比`糖果數最多的鄰居`再多`1`，如果左右鄰居數值皆小於我們，那糖果數就是取`max(neighbors)+1`
- 但如果鄰居的數值比我們大或是相等，那我們就不需要拿得比鄰居多，如果左右鄰居數值皆比我們大或相等，那就是拿最基本的`1`顆糖果

由於必須高校地找出`最小值`並且還要跟左右鄰居比對，也就是還需要知道`index`
因此，我們可以用`min heap`同時儲存`[rating, index]`來達到我們的需求

建立好`min heap`後，就開始rating由小到大發放糖果:
```python
candies = 0
while minHeap:
    _, i = heapq.heappop(minHeap)
    
    # 如果鄰居rating比我們大再加入到neighbors中，最後取max+1. (max的預設值為0)
    neighbors = []
    if i-1 >= 0 and ratings[i] > ratings[i-1]:
        neighbors.append(idx2candy[i-1])
    if i+1 < n and ratings[i] > ratings[i+1]:
        neighbors.append(idx2candy[i+1])

    # 更新目前index拿到的糖果，並記錄總數
    idx2candy[i] = max(neighbors or [0])+1
    candies += idx2candy[i]
```

## Complexity

- time complexity

$$O(nlogn)$$

- space complexity

$$O(n)$$

# Greedy - O(N) time Optimized

## Intuition

第一輪發放糖果:
首先由左往右遍歷，對每個`i`跟左鄰居相比來發放糖果，保證每個`i`都拿到合理且最少的糖果數

第二輪發放糖果:
再來由右往左遍歷，對每個`i`跟右鄰居相比來發放糖果，保證每個`i`也拿到合理的糖果數

這樣兩輪後每個`i`對左右鄰居都會是最少且合理的糖果數

## Complexity

- time complexity

$$O(n)$$

- space complexity

$$O(n)$$