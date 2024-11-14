class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        occupied = defaultdict(int)
        for r, c in reservedSeats:
            r, c = r-1, c-1
            occupied[r] |= (1<<c)

        total = n * 2
        for state in occupied.values():
            seat2 = (state>>1)&1
            seat3 = (state>>2)&1
            seat4 = (state>>3)&1
            seat5 = (state>>4)&1
            seat6 = (state>>5)&1
            seat7 = (state>>6)&1
            seat8 = (state>>7)&1
            seat9 = (state>>8)&1

            seat23, seat45, seat67, seat89 = seat2+seat3, seat4+seat5, seat6+seat7, seat8+seat9

            if seat45 == seat67 == 0:
                if seat23 > 0 or seat89 > 0:
                    total -= 1
            elif seat45 == 0:
                if seat23 > 0:
                    total -= 2
                else:
                    total -= 1
            elif seat67 == 0:
                if seat89 > 0:
                    total -= 2
                else:
                    total -= 1
            else:
                total -= 2
        return total

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = defaultdict(int)
        for i, j in reservedSeats:
            if 2 <= j <= 5:
                seats[i] |= 1
            if 4 <= j <= 7:
                seats[i] |= 2
            if 6 <= j <= 9:
                seats[i] |= 4

        res = 2 * n
        for occupied in seats.values():
            if occupied == 7:
                res -= 2
            elif occupied:
                res -= 1

        return res