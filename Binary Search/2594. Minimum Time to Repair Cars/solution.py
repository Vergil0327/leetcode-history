class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        counter = Counter(ranks)
        def check(timeLimit):
            fixed = 0
            for r in counter.keys():
                n = int(sqrt(timeLimit//r))
                fixed += n * counter[r]
            return fixed >= cars

        l, r = 0, int(1e14)
        while l < r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid
            else:
                l = mid+1
        return l