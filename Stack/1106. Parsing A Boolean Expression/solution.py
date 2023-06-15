class Solution:
    def parseBoolExpr(self, expr: str) -> bool:
        n = len(expr)
        stack = []
        op = []
        values = []
        i = res = 0
        while i < n:
            if expr[i] == "&" or expr[i] == "|" or expr[i] == "!":
                op.append(expr[i])
                stack.append(values)
                values = []
                i += 1 # skip "("

            elif expr[i] == ")":
                operator = op.pop()

                # evaluate current values
                res = self.evaluate(values, operator)
                    
                # pop stack and merge to previous stack
                values = stack.pop()
                values.append(res)

            elif expr[i] == "t" or expr[i] == "f": # v,v,v,...
                values.append(1 if expr[i] == "t" else 0)

            i += 1
        return res == 1

    def evaluate(self, nums, op):
        v = nums.pop()
        if op == "!":
            return v^1
        elif op == "&":
            for num in nums:
                v &= num
            return v
        else:
            for num in nums:
                v |= num
            return v