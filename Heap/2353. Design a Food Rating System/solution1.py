class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine2heap = {c:[] for c in cuisines}
        self.food_dict = {food: [c, -r] for food, c, r in zip(foods, cuisines, ratings)}
        for f, (c,r) in self.food_dict.items():
            heapq.heappush(self.cuisine2heap[c], (r, f))
            
        
    def changeRating(self, food: str, newRating: int) -> None: # O(1)
        self.food_dict[food][1] = -newRating
        cuisine = self.food_dict[food][0]
        heapq.heappush(self.cuisine2heap[cuisine], (-newRating, food))
        
    def highestRated(self, cuisine: str) -> str: #
        heap = self.cuisine2heap[cuisine]

        while heap[0][0] != self.food_dict[heap[0][1]][1]:
            heapq.heappop(heap)
        
        return heap[0][1]