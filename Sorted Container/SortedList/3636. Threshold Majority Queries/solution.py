# Time Limit Exceeded 556 / 559 testcases passed
class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        count = Counter()
        sl = SortedList()
        offline_queries = []
        threshold = [0] * len(queries)
        for i, (l, r, t) in enumerate(queries):
            offline_queries.append((l, r, i))
            threshold[i] = t

        block_size = max(1, len(nums) // sqrt(len(queries)))

        def mo_cmp(query):
            L, R, idx = query
            block_id = L // block_size
            return (block_id, R)

        offline_queries.sort(key=mo_cmp)

        res = [0] * len(offline_queries)

        def add(pos):
            x = nums[pos]
            if x in count:
                sl.discard((count[x], -x))
            count[x] += 1
            sl.add((count[x], -x))

        def rem(pos):
            x = nums[pos]
            sl.discard((count[x], -x))
            count[x] -= 1
            if count[x] > 0:
                sl.add((count[x], -x))

        currL = currR = 0
        for L, R, idx in offline_queries:
            while currR <= R:
                add(currR)
                currR += 1

            while currL > L:
                currL -= 1
                add(currL)
            while currR > R + 1:
                currR -= 1
                rem(currR)

            while currL < L:
                rem(currL)
                currL += 1

            if not sl:
                res[idx] = -1
            else:
                cnt, x = sl[-1]
                if cnt < threshold[idx]:
                    res[idx] = -1
                else:
                    res[idx] = -x
        return res