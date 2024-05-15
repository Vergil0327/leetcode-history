class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n = len(target)

        def check(target, start):
            valid = False
            for i in range(len(stamp)):
                if start+i >= n: return False
                if target[start+i] == "*": continue
                if target[start+i] != stamp[i]: return False
                valid = True
            return valid

        def dfs(s):
            if s[0] == "*" and len(set(s)) == 1: return []

            for i in range(n):
                if check(s, i):
                    arr = dfs(s[:i] + "*"*len(stamp) + s[i+len(stamp):])
                    if arr and arr[0] == "RETURN": return ["RETURN"]
                    return arr + [i]

            return ["RETURN"] # 代表無解
            
        ans = dfs(target)
        return ans if ("RETURN" not in ans) and (len(ans) <= 10*n) else []
