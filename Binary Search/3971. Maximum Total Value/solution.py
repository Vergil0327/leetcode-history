class Solution:
    def maxTotalValue(self, value: list[int], decay: list[int], m: int) -> int:
        MOD = 10**9 + 7

        # 輔助功能：給定一個门槛值 g，計算有多少個元素 >= g 以及它們的總和
        def get_count_and_sum(g: int) -> tuple[int, int]:
            total_count = total_sum = 0
            for v, d in zip(value, decay):
                if v >= g:
                    # 計算該等差數列中有多少項 >= g
                    t = (v - g) // d + 1
                    total_count += t
                    # 使用等差數列求和公式：t * (首項 + 末項) / 2
                    total_sum += t * (2 * v - (t - 1) * d) // 2
            return total_count, total_sum

        # 特判：如果把所有大於等於 1 的正數都拿完，總數量還不夠 m
        # 那我們就全拿，不需要做多餘的二分搜尋
        total_pos_count, total_pos_sum = get_count_and_sum(1)
        if total_pos_count <= m:
            return total_pos_sum % MOD

        # 二分搜尋最優門檻 g
        l = 1
        r = max(value)
        best_g = 1

        while l <= r:
            mid = (l + r) // 2
            count, _ = get_count_and_sum(mid)
            
            # 如果大於等於 mid 的元素太充足（>= m），說明 mid 可以再提高
            if count >= m:
                best_g = mid
                l = mid + 1
            else:
                r = mid - 1

        # 拿到 best_g 後，為了保險起見（避免剛好等於 best_g 的元素拿太多超標）
        # 我們先精準拿完所有 >= (best_g + 1) 的頂級好料
        next_count, next_sum = get_count_and_sum(best_g + 1)

        # 剩下還不夠的部分 (m - next_count)，全部用剛好等於 best_g 的次級好料補齊
        rem_count = m - next_count
        final_sum = next_sum + rem_count * best_g

        return final_sum % MOD
    

class Solution:
    def maxTotalValue(self, value: list[int], decay: list[int], m: int) -> int:
        MOD = 10**9 + 7

        def count_ge(x: int) -> int:
            total = 0
            for a, d in zip(value, decay):
                if a >= x:
                    total += (a - x) // d + 1
            return total

        lo, hi = 1, max(value)
        while lo <= hi:
            mid = (lo + hi) // 2
            if count_ge(mid) >= m:
                lo = mid + 1
            else:
                hi = mid - 1

        t = hi  # largest threshold with at least m terms >= t

        cnt_gt = 0
        sum_gt = 0

        for val, dec in zip(value, decay):
            if val <= t: continue

            cnt = (val - (t + 1)) // dec + 1  # terms strictly greater than t
            last = val - (cnt - 1) * dec

            cnt_gt += cnt
            sum_gt += cnt * (val + last) // 2

        ans = sum_gt + (m - cnt_gt) * t
        return ans % MOD