class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        res = -inf
        for odd in "01234": 
            for even in "01234": 
                if odd == even: continue

                # Sliding Window with Prefix Sums
                seen = defaultdict(lambda : inf)
                presum_odd = [0]
                presum_even = [0]
                l = r = 0
                while r < n:
                    presum_odd.append(presum_odd[-1])
                    presum_even.append(presum_even[-1])
                    
                    # expands the window by adding new characters and updating their frequencies.
                    ch = s[r]
                    if ch == odd:
                        presum_odd[-1] += 1
                    elif ch == even:
                        presum_even[-1] += 1
                    r += 1

                    # Window Size Constraint
                    # seen[key]: minimum previous frequencies with complementary parities
                    # The condition r-l >= k is crucial because:
                    # - We want substrings of size AT LEAST k
                    # - We don't need to consider windows larger than necessary
                    # - `presum_odd[l] < presum_odd[-1] and presum_even[l] < presum_even[-1]` conditions ensure we only process prefixes that actually contain both characters
                    while r-l >= k and presum_odd[l] < presum_odd[-1] and presum_even[l] < presum_even[-1]:
                        key = (presum_odd[l] % 2, presum_even[l] % 2) # parity of odd & even
                        diff = presum_odd[l] - presum_even[l]
                        seen[key] = min(seen[key], diff)
                        l += 1

                    key = (1 - presum_odd[-1] % 2, presum_even[-1] % 2) # wanted parity of odd & even
                    current = presum_odd[-1] - presum_even[-1]

                    res = max(res, current - seen[key])
        return res