class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        n = len(coins)

        def countMultiples(state, m):
            lcm = 1
            for i in range(n):
                if (state>>i)&1:
                    lcm = lcm*coins[i]//gcd(lcm, coins[i])
            
            return m // lcm

        def count(m):
            count = 0
            for i in range(1, n+1):
                state = (1<<i)-1
                while state < (1<<n):
                    if i%2 == 1:
                        count += countMultiples(state, m)
                    else:
                        count -= countMultiples(state, m)
                    c = state & -state
                    r = state+c
                    state = (((r^state)>>2)//c) | r

            return count

        l, r = coins[0], coins[-1]*k
        while l < r:
            mid = l + (r-l)//2
            if count(mid) < k:
                l = mid+1
            else:
                r = mid
        return l
