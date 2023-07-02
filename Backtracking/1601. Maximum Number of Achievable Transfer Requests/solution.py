class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)

        def check(bitmask, n, requests):
            netTransfer = [0] * n # netTransfer[i] = net transfer of building_i
            for i in range(m):
                if (bitmask>>i)&1:
                    u, v = requests[i]
                    netTransfer[u] -= 1
                    netTransfer[v] += 1
            if any(num != 0 for num in netTransfer): return False
            return True

        res = 0
        for state in range(1<<m):
            if check(state, n, requests):
                res = max(res, state.bit_count())
        return res
