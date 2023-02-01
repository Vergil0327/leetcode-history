class Solution:
    def smallestSubsequence(self, s: str) -> str:
        counter = Counter(s)

        has = set()
        stack = []
        for ch in s:
            if not stack:
                has.add(ch)
                counter[ch] -= 1
                stack.append(ch)
            elif ch > stack[-1] and ch not in has:
                has.add(ch)
                counter[ch] -= 1
                stack.append(ch)
            elif ch in has:
                counter[ch] -= 1
            else:
                while stack and stack[-1] > ch and counter[stack[-1]] > 0:
                    has.remove(stack.pop())
                has.add(ch)
                counter[ch] -= 1
                stack.append(ch)
        return "".join(stack)

# Concise
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        counter = Counter(s)

        has = set()
        stack = []
        for ch in s:
            if ch in has:
                counter[ch] -= 1
            else:
                while stack and stack[-1] > ch and counter[stack[-1]] > 0:
                    has.remove(stack.pop())
                stack.append(ch)
                has.add(ch)
                counter[ch] -= 1
        return "".join(stack)