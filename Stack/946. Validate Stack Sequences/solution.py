class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        m, n = len(pushed), len(popped)
        stack = []
        i = j = 0
        while pushed or popped:
            if stack and stack[-1] == popped[j]:
                  stack.pop()
                  j += 1
            elif i < m:
                    stack.append(pushed[i])
                    i += 1
            else:
                break
        return i == m and j == n

