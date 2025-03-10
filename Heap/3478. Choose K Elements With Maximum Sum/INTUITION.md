# Intuition

1. sort nums1 in increasing order
2. for nums1[i'], we know nums1[:i'] are all the possible indices `j` we need
3. keep adding nums1[j] to min heap while j < i' and nums1[j] < nums1[i']
    - also need to maintain current max sum
4. pop out smallest nums2[j] using min heap whenever len(heap) > k and update max sum
5. in each iteration, we know nums1[originalIdx[i']] = current max sum