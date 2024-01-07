class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        x1 = set(nums1)
        x2 = set(nums2)

        if len(x1) <= n//2 and len(x2) <= n//2:
            return len(x1|x2)

        distinct1 = x1-x2
        distinct2 = x2-x1
        if len(distinct1) >= n//2:
            return n//2 + min(n//2, len(x2))

        if len(distinct2) >= n//2:
            return n//2 + min(n//2, len(x1))

        # 先拿distinct1, distinct2
        # 剩下的空位, 例如
        # distinct1 = [X X X _ _ _]
        # distinct2 = [Y Y _ _ _ _]
        # nums1還可以再塞3個, nums2還可以再放4個
        # 我們看還剩下幾個數是兩邊都有的, 我們就任意放置
        # 所以我們總共能貢獻: `len(distinct1) + len(distinct2) + len(common)`
        # 但common個數有可能超出剩餘空格, 別忘記最多就只能貢獻`n`個distinct number
        # 所以加個上限min(n, len(distinct1) + len(distinct2) + len(common))
        common = x1&x2
        return min(n, len(distinct1) + len(distinct2) + len(common))
