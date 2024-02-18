class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        m, n = len(arr1), len(arr2)
        
        tri1, tri2 = {}, {}
        for num in arr1:
            s = str(num)
            t = tri1
            for ch in s:
                if ch not in t:
                    t[ch] = {}
                t = t[ch]
                
        for num in arr2:
            s = str(num)
            t = tri2
            for ch in s:
                if ch not in t:
                    t[ch] = {}
                t = t[ch]

        def dfs(tri1, tri2):
            length = 0
            for d in "0123456789":
                if d in tri1 and d in tri2:
                    length = max(length, dfs(tri1[d], tri2[d])+1)
            return length
        return dfs(tri1, tri2)
