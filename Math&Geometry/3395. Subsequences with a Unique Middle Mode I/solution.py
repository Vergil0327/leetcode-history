class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        
        @cache
        def comb_2(num):
            return comb(num, 2)

        def calc_2(elem, first_counter, second_counter, first_other_cnt, second_other_cnt):
            # count include
            result = first_other_cnt * comb_2(second_other_cnt)

            for k, v in first_counter.items():
                if k == elem: continue

                vv = second_counter[k]
                # count exclude triples -- [0 1] 1 [0 0]
                result -= v * comb_2(vv)
                # count exclude doubles -- [0 1] 1 [0 2] / [0 1] 1 [2 0]
                result -= v * vv * (second_other_cnt - vv)
            
            for k, v in second_counter.items():
                if k == elem: continue

                # count exclude doubles -- [0 1] 1 [2 2]
                result -= comb_2(v) * (first_other_cnt - first_counter[k])
            
            return result

        result = 0
        left = Counter()
        right = Counter(nums)

        for i in range(n):
            right[nums[i]] -= 1
            if right[nums[i]] == 0:
                del right[nums[i]]
            
            left_cnt = left[nums[i]]
            right_cnt = right[nums[i]]
            left_other = i - left_cnt
            right_other = n - i - 1 - right_cnt

            result = (
                result
                # [1 1] 1 [1 1] - 5 elements
                + comb_2(left_cnt) * comb_2(right_cnt) % mod
                # [1 1] 1 [0 1] - 4 elements
                + comb_2(left_cnt) * right_cnt * right_other % mod
                # [0 1] 1 [1 1] - 4 elements
                + left_cnt * comb_2(right_cnt) * left_other % mod
                # [1 1] 1 [0 0] - 3 elements
                + comb_2(left_cnt) * comb_2(right_other) % mod
                # [0 0] 1 [1 1] - 3 elements
                + comb_2(right_cnt) * comb_2(left_other) % mod
                # [0 1] 1 [0 1] - 3 elements
                + left_cnt * right_cnt * left_other * right_other % mod
                # [0 1] 1 [0 0] - 2 elements
                + left_cnt * calc_2(nums[i], left, right, left_other, right_other) % mod
                # [0 0] 1 [0 1] - 2 elements
                + right_cnt * calc_2(nums[i], right, left, right_other, left_other) % mod
            ) % mod
            
            # add elem to left counter
            left[nums[i]] += 1
        
        return result % mod
