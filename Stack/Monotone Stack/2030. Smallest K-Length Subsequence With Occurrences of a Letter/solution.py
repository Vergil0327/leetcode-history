class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        n = len(s)

        numLetters = sum(1 for ch in s if ch == letter)
        upperbound1, upperbound2 = n-k, numLetters-repetition
        deleted = letterDeleted = 0

        stack = []
        for i in range(n):
            while (stack and stack[-1] > s[i]
                         and deleted < upperbound1
                         and (letterDeleted < upperbound2 if stack[-1] == letter else True)):
                deleted += 1
                letterDeleted += int(stack.pop() == letter)
            
            stack.append(s[i])

        res = ""
        for i in range(len(stack)-1, -1, -1):
            if deleted == upperbound1: # can't delete anymore
                res = stack[i] + res
            elif stack[i] == letter and letterDeleted == upperbound2:
                res = stack[i] + res
            else:
                deleted += 1
                letterDeleted += int(stack[i] == letter)
        return res
                