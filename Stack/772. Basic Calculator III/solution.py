from collections import deque
from typing import Deque


class Solution:
    def calculate(self, s: str) -> int:
        # remove empty
        S = ""
        for ch in s:
            if ch != " ":
                S += ch

        def compute(s: Deque[str]):
            stack = []
            sign = "+"
            curr = 0

            while s:
                ch = s.popleft()
                if ch.isdigit():
                    curr = int(ch) + curr * 10

                # start compute recursively
                if ch == "(":
                    curr = compute(s)

                # not s: means end of s -> last calculation
                if not ch.isdigit() or not s:
                    if sign == "+":
                        stack.append(curr)
                    elif sign == "-":
                        stack.append(-curr)
                    elif sign == "*":
                        stack[-1] *= curr
                    elif sign == "/":
                        # python strange behavior, -3/2 = -2 but we want -1
                        # this is work around
                        stack[-1] = int(stack[-1]/curr)
                    sign = ch
                    curr = 0
                
                if ch == ")": # end recursion
                    break
            return sum(stack)
        return compute(deque(S))



