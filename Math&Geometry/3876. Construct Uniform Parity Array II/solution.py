"""
由於只要i != j 而且 nums1[i] - nums1[j] >=1
代表只要我們維護SortedList並找出相減大於0的(odd, odd), (even, odd) pair的話
我們就能利用odd組出even, 抑或even組出odd

在看這個例子: `nums1 = [12,9], expected = True`

因為只要i!=j就能拿來組nums2, 所以我們可以先對nums1排序, 然後再利用上述討論方式來找出
最終能不能組出 n個odd 或 n個even
"""
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        if n == 1: return True
    
        nums1.sort()

        sl_odd = SortedList()
        odd = even = 0
        for num in nums1:
            if num%2 == 0:
                even += 1
                i = sl_odd.bisect_left(num)
                if i > 0:
                    odd += 1
            else:
                odd += 1
                i = sl_odd.bisect_left(num)
                if i > 0:
                    even += 1
                sl_odd.add(num)

        return odd >= n or even >= n
    

"""
但其實還能更優化, 我們不需要維護奇數跟偶數兩種SortedList
由於我們想知道能不能兩數相減是>=1, 所以對於當前nums1[i]來說, 我們只要維護minimum odd即可

- minimum even不用是因為, 不管奇數或偶數, 相減都不會改變parity

"""

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        if n == 1: return True
    
        nums1.sort()

        min_odd = float('inf')
        odd = even = 0
        for num in nums1:
            if num%2 == 0:
                even += 1
                
                if num - min_odd > 0:
                    odd += 1

            else:
                odd += 1
                
                if num - min_odd > 0:
                    even += 1
                min_odd = min(min_odd, num)

        return odd >= n or even >= n
    