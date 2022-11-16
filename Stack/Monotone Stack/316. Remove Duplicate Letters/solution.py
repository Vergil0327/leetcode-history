# Monotonic Stack
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        has = Counter()
        
        # monotonically lexicographically increasing stack
        stack = []
        for ch in s:
            if has[ch] > 0:
                counter[ch] -= 1
            elif not stack or stack[-1] < ch:
                stack.append(ch)
                has[ch] += 1
            else:
                while stack and ch < stack[-1] and has[stack[-1]] < counter[stack[-1]]:
                    top = stack.pop()
                    counter[top] -= 1
                    has[top] -= 1
                stack.append(ch)
                has[ch] += 1
        return "".join(stack)

# Similar Approach
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastOccurence = {}
        for i, ch in enumerate(s):
            lastOccurence[ch] = i
        
        # monotonically lexicographically increasing stack
        visited = set()
        stack = []
        for i, ch in enumerate(s):
            if ch not in visited:
                while stack and stack[-1] > ch and i < lastOccurence[stack[-1]]:
                    visited.remove(stack.pop())
                
                visited.add(ch)
                stack.append(ch)
        return "".join(stack)