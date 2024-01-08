class Solution:
    def braceExpansionII(self, expr: str) -> List[str]:
        n = len(expr)

        def product(arr1, arr2):
            if not arr1: return arr2
            return [s1+s2 for s1 in arr1 for s2 in arr2]

        stack = []
        arr, cur = [], []
        for i in range(n):
            if expr[i] == "{":
                stack.append(arr)
                stack.append(cur)
                arr, cur = [], []
            elif expr[i] == "}":
                pre = stack.pop()
                preArr = stack.pop()
                cur = product(pre, arr+cur)
                arr = preArr
            elif expr[i] == ",":
                arr += cur
                cur = []
            else: # elif expr[i].isalpha():
                cur = product(cur, [expr[i]])

        return sorted(set(arr+cur))

# recursion
class Solution:
    def braceExpansionII(self, expr: str) -> List[str]:
        groups = [[]]
        level = 0
        for i, ch in enumerate(expr):
            if ch == "{":
                if level == 0:
                    start = i+1
                level += 1
            elif ch == "}":
                level -= 1
                if level == 0:
                    groups[-1].append(self.braceExpansionII(expr[start:i])) # remove outermost braces
            elif ch == "," and level == 0:
                groups.append([])
            elif level == 0:
                groups[-1].append([ch])

        def product(*arrs):
            res = arrs[0]
            for arr in arrs[1:]:
                tmp = []
                for s1 in res:
                    for s2 in arr:
                        tmp.append(s1+s2)
                res = tmp
            return set(res)

        res = set()
        for group in groups:
            res |= product(*group)

        return sorted(res)
