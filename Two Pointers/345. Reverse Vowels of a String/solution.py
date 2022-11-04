# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = {'a','e','i','o','u', "A", "E", "I", "O", "U"}
        
        vowels = deque()
        for i in range(len(s)-1, -1, -1):
            if s[i] in VOWELS:
                vowels.append(s[i])
        
        arr = list(s)
        for i, ch in enumerate(arr):
            if ch in VOWELS:
                v = vowels.popleft()
                arr[i] = v
        return "".join(arr)

# time: O(n)
# space: O(1)
class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = {'a','e','i','o','u', "A", "E", "I", "O", "U"}
        
        arr = list(s)
        l, r = 0, len(arr)-1
        
        while l < r:
            if arr[l] in VOWELS and arr[r] in VOWELS:
                arr[l], arr[r] = arr[r], arr[l]
                l, r = l+1, r-1
            
            if arr[l] not in VOWELS:
                l += 1
            elif arr[r] not in VOWELS:
                r -= 1
        return "".join(arr)