class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def ispal(s):
            return s == s[::-1]

        def constructPalindrome(num, typ):
            right = num
            if typ == "even":
                while right:
                    num = num*10 + right%10
                    right //= 10
                return num
            
            if typ == "odd":
                right //= 10
                while right:
                    num = num*10 + right%10
                    right //= 10
                return num
            return 0

        lo, hi = int(left), int(right)
        res = 0
        start, end = max(1, pow(10, len(left)//4-1)), max(1, pow(10, len(right)//4+1))
        for num in range(start, end+1):
            for typ in ["even", "odd"]:
                palindrome = constructPalindrome(num, typ)
                superPal = palindrome * palindrome
                if lo <= superPal <= hi and ispal(str(superPal)):
                    res += 1
        return res

# 分開處理 + early break if super palindrome is greater than int(high)
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        # Function to check if a string is a palindrome
        def is_palindrome(s):
            return s == s[::-1]
        
        L = int(left)
        R = int(right)
        upperbound = pow(10, len(right)//4+1) + 1
        res = 0
        
        # Generate all odd length palindrome
        for x in range(upperbound):
            s = str(x)
            pal = s + s[-2::-1]
            v = int(pal)
            v *= v
            if v > R: break
            if v >= L and is_palindrome(str(v)):
                res += 1
        
        # Generate all even length palindrome
        for x in range(upperbound):
            s = str(x)
            pal = s + s[::-1]
            v = int(pal)
            v *= v
            if v > R: break
            if v >= L and is_palindrome(str(v)):
                res += 1

        return res