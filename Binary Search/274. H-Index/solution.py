class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        
        def isValidH(mid):
            return citations[mid] >= (n-mid)

        l, r = 0, len(citations)-1
        while l < r:
            mid = l + (r-l)//2
            if isValidH(mid):
                r = mid
            else:
                l = mid+1
        return n-l if isValidH(l) else 0