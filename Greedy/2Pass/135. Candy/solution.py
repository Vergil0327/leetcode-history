# Greedy - Priority Queue
class Solution:
    def candy(self, ratings: List[int]) -> int:
        idx2candy = defaultdict(int)

        minHeap = [[rating, i] for i, rating in enumerate(ratings)]
        heapq.heapify(minHeap)

        n = len(ratings)
        candies = 0
        while minHeap:
            _, i = heapq.heappop(minHeap)
            neighbors = []
            if i-1 >= 0 and ratings[i] > ratings[i-1]:
                neighbors.append(idx2candy[i-1])
            if i+1 < n and ratings[i] > ratings[i+1]:
                neighbors.append(idx2candy[i+1])

            minimum = max(neighbors or [0]) # or minimum = max(neighbors, default=0)
            idx2candy[i] = minimum+1
            candies += idx2candy[i]
        return candies

# Greedy - O(N) time Optimized
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = max(1, candies[i-1]+1)
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)

        return sum(candies)
