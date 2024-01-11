class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        index = defaultdict(lambda: [n, -1]) # s[i]: [l, r]
        for i, ch in enumerate(s):
            index[ch][0] = min(index[ch][0], i)
            index[ch][1] = max(index[ch][1], i)

        def expand(ch, l, r):
            ll, rr = l, r
            seen = set([ch])
            for i in range(l, r+1):
                if s[i] in seen: continue
                seen.add(s[i])
                left, right = index[s[i]][0], index[s[i]][1]
                ll = min(ll, left)
                rr = max(rr, right)

            while l > ll or r < rr:
                nextL, nextR = ll, rr
                for i in range(ll, l):
                    if s[i] in seen: continue
                    seen.add(s[i])
                    left, right = index[s[i]][0], index[s[i]][1]
                    nextL = min(nextL, left)
                    nextR = max(nextR, right)

                for i in range(r+1, rr+1):
                    if s[i] in seen: continue
                    seen.add(s[i])
                    left, right = index[s[i]][0], index[s[i]][1]
                    nextL = min(nextL, left)
                    nextR = max(nextR, right)
                l, r = ll, rr
                ll, rr = nextL, nextR
            return r-l+1, s[l:r+1]

        valid = set()
        for ch, (l, r) in index.items():
            length, substr = expand(ch, l, r)
            valid.add((length, substr))
        
        res = []
        arr = sorted(list(valid))
        seen = set()
        for _, substr in arr:
            SET = set(substr)
            if any(ch in seen for ch in SET): continue
            seen |= SET
            res.append(substr)

        return res