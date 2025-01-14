class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        nums.reverse()

        res = 0
        window = deque()
        l = 0
        for r in range(len(nums)):
            # reversed_nums=[6, 4, 8]
            # 實際上原本是: [8, 4, 6] => non-decreasing => [8,8,8]
            # 所以這邊做的事情是: [6,6,8] => [8,8,8], 先計算(6,4), 再來這段會全變成6, 然後再計算(6,8), 將全部6轉成8的操作數
            while window and nums[window[-1]] < nums[r]:
                rr = window.pop()
                ll = window[-1] if window else l - 1
                cnt = rr - ll
                k -= cnt * (nums[r] - nums[rr])
            window.append(r)

            # nums[window[0]]是目前max, max-nums[l]就會是滑窗左端點移動後所返回的操作數
            while k < 0:
                k += nums[window[0]] - nums[l]
                if window[0] == l:
                    window.popleft()
                l += 1
            res += r - l + 1
        return res