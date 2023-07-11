class Solution:
    def canConvert(self, str1, str2):
        m, n = len(str1), len(str2)
        if m != n: return False

        mapping = {}
        for i in range(n):
            if str1[i] in mapping and mapping[str1[i]] != str2[i]: return False
            mapping[str1[i]] = str2[i]
            
        return True