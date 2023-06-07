class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def calculate(first):
            res = 0
            stack = []
            for ch in s:
                if not stack:
                    stack.append(ch)
                elif stack[-1] == first[0] and ch == first[1]: # ba
                    stack.pop()
                    res += (y if first == "ba" else x)
                else:
                    stack.append(ch)

            stack2 = []
            for ch in stack:
                if not stack2:
                    stack2.append(ch)
                elif stack2[-1] == first[1] and ch == first[0]: # ab
                    stack2.pop()
                    res += (x if first == "ba" else y)
                else:
                    stack2.append(ch)
            return res

        return max(calculate("ab"), calculate("ba"))