class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        num1 = 0 # change nums1 to binary format
        for i, num in enumerate(nums1):
            if num == 1:
                num1 |= (num<<i)

        nums2sum = sum(nums2)
        for _type, a, b in queries:
            if _type == 1: # update nums1[a:b]
                # if we use binary format to represent nums1
                # we can use 2 bitmask to flip
                # ex.
                # 1[010110]11
                #   b    a
                # 0 111111 11 -> nums1 XOR this mask (mask2)
                #          11 -> nums1 XOR this mask (mask1)
                # 1 101001 11 -> target
                mask1 = (1<<a)-1
                mask2 = (1<<(b+1))-1
                num1 = num1^mask1^mask2

            elif _type == 2: # get range sum nums1[a:b] and add to nums2sum
                # nums2[i] = nums2[i] + nums1[i] * p
                # nums2[i] += nums1[i] * p
                # nums2sum += sum(nums1) * p
                nums2sum += num1.bit_count() * a

            else: # get sum(nums2)
                res.append(nums2sum)
        return res