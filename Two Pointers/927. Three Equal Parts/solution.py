class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = len(arr)
        count1 = sum(arr)
        if count1 == 0: return [0, n-1]
        if count1%3 != 0: return [-1, -1]

        # find right part arr[j:]
        count1 //= 3
        j = n
        while count1:
            j -= 1
            if arr[j]:
                count1 -= 1

        # find left part arr[:i]
        i = 0
        while arr[i] == 0: # skip leading zeros
            i += 1

        jj = j
        while jj < n and arr[i] == arr[jj]:
            i, jj = i+1, jj+1

        if jj != n: return [-1, -1]
        
        # now:
        # 000 XXXXX 000[middle] 000 [right]
        #           i                j        jj
        ii = i
        while arr[ii] == 0: # skip leading zeros
            ii += 1

        jj = j
        while jj < n and arr[ii] == arr[jj]:
            ii, jj = ii+1, jj+1
        if jj != n: return [-1, -1]
        # now
        # 000 [left] 000[middle] 000 [right]
        #            i          ii    j     jj

        return [i-1, ii]