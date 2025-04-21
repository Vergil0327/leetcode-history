class SegTree:
    def __init__(self, nums: List[int], k: int):
        self.k = k
        n = len(nums)
        size = 1
        while size < n:
            size <<= 1
        self.size = size

        self.tree = [([0]*k, 1) for _ in range(2 * size)]
        for i in range(n):
            r = nums[i] % k
            cnt = [0]*k
            cnt[r] = 1
            self.tree[size + i] = (cnt, r)

        for p in range(size - 1, 0, -1):
            self.tree[p] = self.merge(self.tree[p<<1], self.tree[p<<1|1])

    def merge(self, l, r):
        cnt_l, prod_l = l
        cnt_r, prod_r = r
        k = self.k
        
        count = cnt_l.copy()
        for r in range(k): # append suffix (segment `r`) to each prefix of `l`
            if cnt_r[r]:
                x = (prod_l * r) % k
                count[x] += cnt_r[r]

        prod = (prod_l * prod_r) % k
        return count, prod

    def update(self, idx, val):
        pos = self.size + idx

        r = val % self.k
        cnt = [0] * self.k
        cnt[r] = 1
        self.tree[pos] = (cnt, r)
        
        # keep update from leaf to the root
        pos >>= 1
        while pos:
            self.tree[pos] = self.merge(self.tree[2 * pos], self.tree[2 * pos + 1])
            pos >>= 1

    # query [l,r) right-exclusive
    def query(self, l, r):
        l += self.size
        r += self.size
        cnt_l, prod_l = [0]*self.k, 1
        cnt_r, prod_r = [0]*self.k, 1
        while l < r:
            if l & 1:
                cnt_l, prod_l = self.merge((cnt_l, prod_l), self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                cnt_r, prod_r = self.merge(self.tree[r], (cnt_r, prod_r))
            l, r = l>>1, r>>1

        return self.merge((cnt_l, prod_l), (cnt_r, prod_r))

    # query [l,r] both-exclusive
    def query2(self, l, r):
        l += self.size
        r += self.size
        cnt_l, prod_l = [0]*self.k, 1
        cnt_r, prod_r = [0]*self.k, 1
        while l <= r:
            if l == r:
                cnt_l, prod_l = self.merge((cnt_l, prod_l), self.tree[l])
                break

            if l & 1:
                cnt_l, prod_l = self.merge((cnt_l, prod_l), self.tree[l])
                l += 1
            if r & 1 == 0:
                cnt_r, prod_r = self.merge(self.tree[r], (cnt_r, prod_r))
                r -= 1
            l, r = l>>1, r>>1

        return self.merge((cnt_l, prod_l), (cnt_r, prod_r))

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        st = SegTree(nums, k)
        
        res = []
        for idx, val, start, x in queries:
            st.update(idx, val)
            # cnt, _ = st.query(start, len(nums))
            cnt, _ = st.query2(start, len(nums)-1)
            res.append(cnt[x])
        return res