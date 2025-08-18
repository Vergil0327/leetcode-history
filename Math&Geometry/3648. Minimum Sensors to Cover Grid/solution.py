class Solution:
    """
    The Chebyshev distance between two cells (r1, c1) and (r2, c2) is max(|r1 - r2|,|c1 - c2|).

    sensor 會涵蓋上下左右四個方向k個距離:

    example 1. n=5,m=5,k=1
    X X X X X
    X O X O X
    X X X X X
    X O X O X
    X X X X X
    
    example 2. n=2,m=2,k=2
    O X
    X X

    example 3. n=6,m=5,k=1

    X X X X X X
    X X X X X X
    X X X X X X
    X X X X X X
    X X X X X X

    或許試著等距離放?
    兩sensor間隔`d = 2*k+1`距離

    所以每個row要放置: ceil(n/d)
    每個column要放置: ceil(m/d)
    用ceil是為了怕長度要覆蓋到全部, 避免無法整除的情況
    所以總共sensor數量為: ceil(n/d) * ceil(m/d)
    """
    def minSensors(self, n: int, m: int, k: int) -> int:
        distance = 2*k+1
        return ceil(n/distance) * ceil(m/distance)