"""
The Logic - Monotonic Pass:

1. Delete a character only if it is strictly greater than the next character ($S[i] > S[i+1]$) AND it has a duplicate later. This handles cases like accb $\rightarrow$ acb.
2. Deduplication Pass: If the string still contains duplicates, we only delete them if they are identical to the character before them ($S[i] == S[i-1]$) AND that character is the last of its kind in the string.

ex.

- s="aba", expected: "ab"
- s="aa", expected: "a"
- s="aaccb", expected: "aacb"
"""

from collections import Counter

class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        # 1. Count frequencies
        counts = Counter(s)
        stack = []
        
        # 2. Monotonic Step: Remove 'heavy' characters followed by 'lighter' ones
        for char in s:
            while stack and stack[-1] > char and counts[stack[-1]] > 1:
                counts[stack.pop()] -= 1
            stack.append(char)
        
        # 3. Shortening Step: If we have duplicates left, 
        # only remove from the very end to satisfy "aa" -> "a" 
        # and "aba" -> "ab" without breaking "aacb".
        while len(stack) > 1:
            last_char = stack[-1]
            # If the last character appears earlier in the stack, 
            # deleting it always makes the string lexicographically smaller.
            
            # Check if last_char exists in stack[0...-2]
            exists_earlier = False
            for i in range(len(stack) - 1):
                if stack[i] == last_char:
                    exists_earlier = True
                    break
            
            if exists_earlier:
                stack.pop()
            else:
                break
                
        return "".join(stack)
    
"""
Optimized

Intuition

We are allowed to delete extra occurrences of any character, but at least one occurrence must remain.
So for every character, we can choose how many times it appears, as long as it appears at least once.

Our goal is to build the lexicographically smallest possible string while respecting the original order of characters.

This is similar in spirit to monotonic stack problems:

We want smaller characters earlier

But we can only remove a character if another copy still exists later

So the key idea:

While building the result from left to right, remove previously added characters if:

1. They are lexicographically larger than the current character

2. They appear again later, so deleting one copy is safe
"""
class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        count = Counter(s)
        stack = []

        for ch in s:
            while (stack and stack[-1] > ch and count[stack[-1]] >= 2):
                count[stack[-1]] -= 1
                stack.pop()

            stack.append(ch)

        while(count[stack[-1]] >= 2):
            count[stack[-1]] -= 1
            stack.pop()

        return "".join(stack)