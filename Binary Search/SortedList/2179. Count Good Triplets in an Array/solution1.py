class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        mapping = {nums1[i]: i for i in range(n)}
        for i in range(n):
            nums2[i] = mapping[nums2[i]]
        original = nums2.copy()
        v2idx = {nums2[i]: i for i in range(n)}

        # count smaller before self
        smallerBeforeSelf = [0] * n
        tmp = [0] * n
        def mergesort(l, r):
            if l >= r: return

            mid = l + (r-l)//2
            mergesort(l, mid)
            mergesort(mid+1, r)

            tmp[l:r+1] = nums2[l:r+1].copy()
            i, j = l, mid+1
            for k in range(l, r+1):
                if i == mid+1:
                    # X X X X X X X X
                    #      i/m    j
                    idx = v2idx[tmp[j]]
                    smallerBeforeSelf[idx] += i-l

                    nums2[k] = tmp[j]
                    j+=1
                elif j == r+1:
                    nums2[k] = tmp[i]
                    i += 1
                elif tmp[i] > tmp[j]:
                    # X X X X X X X X
                    # i    m    j
                    idx = v2idx[tmp[j]]
                    smallerBeforeSelf[idx] += i-l

                    nums2[k] = tmp[j]
                    j += 1
                else:
                    nums2[k] = tmp[i]
                    i += 1

        mergesort(0, n-1)

        res = 0
        for i in range(n):
            smallerAfterSelf = original[i] - smallerBeforeSelf[i]
            largerAfterSelf = n-i-1 - smallerAfterSelf
            res += smallerBeforeSelf[i] * largerAfterSelf
        return res
