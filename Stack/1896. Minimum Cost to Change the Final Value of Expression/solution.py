class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        def evalValue(left, right, operator):
            if operator == "&":
                return left[0]&right[0]
            elif operator == "|":
                return left[0]|right[0]
            else:
                return right[0]

        def evalCost(left, right, operator):
            if operator == "&":
                if left[0]+right[0] == 2: # 1&1
                    return min(left[1], right[1])
                if left[0]+right[0] == 1: # 1&0 or 0&1
                    return 1
                if left[0]+right[0] == 0: # 0&0
                    return min(left[1], right[1]) + 1
            elif operator == "|":
                if left[0]+right[0] == 2: # 1|1
                    return min(left[1], right[1])+1
                if left[0]+right[0] == 1: # 1|0 or 0|1
                    return 1
                if left[0]+right[0] == 0: # 0|0
                    return min(left[1], right[1])
            else:
                return right[1]
        
        stack = []
        operator = ""
        cur = (0, inf) # value, flip_cost

        for ch in expression:
            # expression only contains '1','0','&','|','(', and ')'
            if ch.isdigit():
                v = (int(ch), 1)
                val = evalValue(cur, v, operator)
                flip_cost = evalCost(cur, v, operator)
                cur = (val, flip_cost)
            else:
                if ch == "(":
                    stack.append([cur, operator])
                    operator = ""
                    cur = (0, inf)
                elif ch == ")":
                    v, op = stack.pop()
                    val = evalValue(v, cur, op)
                    flip_cost = evalCost(v, cur, op)
                    cur = (val, flip_cost)
                else:
                    operator = ch
        return cur[1]
