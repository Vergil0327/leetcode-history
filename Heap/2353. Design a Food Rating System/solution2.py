from sortedcontainers import SortedSet
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food2cuisine, self.food2rating = dict(), dict()
        self.cuisine2foods = defaultdict(SortedSet) # key: (rating, food)

        for i in range(len(foods)):
            self.food2cuisine[foods[i]] = cuisines[i]
            self.food2rating[foods[i]] = ratings[i]
            self.cuisine2foods[cuisines[i]].add((-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        # remove old rating in sorted set
        self.cuisine2foods[self.food2cuisine[food]].remove((-self.food2rating[food], food))

        # update rating and sorted set
        self.food2rating[food] = newRating
        self.cuisine2foods[self.food2cuisine[food]].add((-self.food2rating[food], food))

    def highestRated(self, cuisine: str) -> str:
        # find highest rating food in target cuisine from sorted set
        return next(iter(self.cuisine2foods[cuisine]))[1]
