from sortedcontainers import SortedList
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.prices = defaultdict(dict) # shop: {movie: price}
        self.sl = sl = defaultdict(SortedList)
        for shop, movie, price in entries:
            sl[movie].add((price, shop))
            self.prices[shop][movie] = price

        self.rented = defaultdict(dict) # {[shop][movie]: price}
        self.rep = SortedList()
    def search(self, movie: int) -> List[int]:        
        return [self.sl[movie][i][1] for i in range(min(5, len(self.sl[movie])))]

    def rent(self, shop: int, movie: int) -> None:
        price = self.prices[shop][movie]
        self.sl[movie].remove((price, shop))
        self.rented[shop][movie] = price
        self.rep.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.rented[shop][movie]
        self.sl[movie].add((price, shop))
        del self.rented[shop][movie]
        self.rep.remove((price, shop, movie))

    def report(self) -> List[List[int]]:
        res = [] # shop, movie
        for i in range(min(5, len(self.rep))):
            _, shop, movie = self.rep[i]
            res.append([shop, movie])
        
        return res
