class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        def parse(s):
            arr = []
            i = 0
            while i < len(s):
                if s[i].isalpha():
                    arr.append(s[i])
                else:
                    j = i
                    while j < len(s) and s[j].isdigit():
                        j += 1
                    arr.append(s[i:j])
                    i = j-1
                i += 1
            return arr
        s, t = parse(s1), parse(s2)

        def getNum(s):
            num = int(s)

            if len(s) == 1:
                return [num]
            elif len(s) == 2:
                a, b = num//10, num%10
                return [a+b, num]
            else:
                a, b, c = num//100, (num//10)%10, num%10
                return [a+b+c, a*10+b+c, a+b*10+c, num]
        
        m, n = len(s), len(t)

        @cache
        def dfs(i, prefix_free_match1, j, prefix_free_match2):
            if i == m and j == n: return prefix_free_match1 == prefix_free_match2
            if (i == m and prefix_free_match1 == 0) or (j == n and prefix_free_match2 == 0): return False

            if i < m and s[i].isdigit(): # 拆分出free_match1
                nums = getNum(s[i])
                for num in nums:
                    if dfs(i+1, prefix_free_match1+num, j, prefix_free_match2): return True
                return False

            if j < n and t[j].isdigit(): # 拆分出free_match1
                nums = getNum(t[j])
                for num in nums:
                    if dfs(i, prefix_free_match1, j+1, prefix_free_match2+num): return True
                return False

            # 消掉開頭的"*"
            if prefix_free_match1 > 0 and prefix_free_match2 > 0:
                common = min(prefix_free_match1, prefix_free_match2)
                return dfs(i, prefix_free_match1-common, j, prefix_free_match2-common)
            elif prefix_free_match1 > 0:
                return dfs(i, prefix_free_match1-1, j+1, prefix_free_match2)
            elif prefix_free_match2 > 0:
                return dfs(i+1, prefix_free_match1, j, prefix_free_match2-1)
            else:
                if s[i] != t[j]: return False
                return dfs(i+1, 0, j+1, 0)
        return dfs(0, 0, 0, 0)

