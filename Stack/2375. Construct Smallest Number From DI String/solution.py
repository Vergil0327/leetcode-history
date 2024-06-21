from sortedcontainers import SortedList
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        stack1, stack2 = [], []

        num = 1
        for i in range(n):
            if pattern[i] == "I":
                stack1.append(str(num))
                while stack2:
                    stack1.append(stack2.pop())
            else:
                stack2.append(str(num))
            num += 1

        stack2.append(str(num))
        while stack2:
            stack1.append(stack2.pop())
        return "".join(stack1)
