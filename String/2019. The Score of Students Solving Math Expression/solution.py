class Solution:
    def basicCalculatorII(self, s: str) -> int:
        n = len(s)

        op = "+"
        cur = 0
        stack = []

        def calculate(ch):
            nonlocal op, cur
            if op == "+":
                stack.append(cur)
            elif op == "-":
                stack.append(-cur)
            elif op == "*":
                stack[-1] *= cur
            elif op == "/":
                # 需要python 除法向 0 取整
                # python strange behavior: -3 // 2 = -2
                stack[-1] = int(stack[-1] / cur)
            cur = 0
            op = ch

        for i in range(n):
            if s[i].isdigit():
                cur = int(s[i]) + cur * 10
            else:
                calculate(s[i])
        calculate("") # last round
        return sum(stack)
    
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        correct = self.basicCalculatorII(s)
        points = defaultdict(int)
        points[correct] = 5

        n = len(s)
        
        @cache
        def dfs(l, r):
            if l == r:
                return {num} if (num:=int(s[l:r+1])) <= 1000 else {}
            
            res = set()
            for i in range(l+1, r+1, 2):
                left = dfs(l, i-1)
                right = dfs(i+1, r)

                if s[i] == "+":
                    res |= {x+y for x in left for y in right if x+y <= 1000}
                elif s[i] == "*":
                    res |= {x*y for x in left for y in right if x*y <= 1000}
            
            # edge case: 代表沒有任何operator
            if not res and (num:=int(s[l])) <= 1000:
                res.add(num)
            
            return res

        possibles = dfs(0, n-1)
        for possible in possibles:
            if possible == correct: continue
            points[possible] = 2

        return sum(map(lambda x:points[x], answers))
