from sortedcontainers import SortedList
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def kMirror(num: int):
            arr = []
            while num:
                arr.append(num%k)
                num //= k

            l, r = 0, len(arr)-1
            while l < r:
                if arr[l] != arr[r]: return False
                l, r = l+1, r-1

            return True

        def genOddPalindrome(num):
            # abc => cba
            # abc*pow(10, 3)+cba
            cur = num
            rev = digits = 0
            while cur > 0:
                rev = rev*10 + cur%10
                cur //= 10
                digits += 1
            return (num//10) * pow(10, digits) + rev
            
        def genEvenPalindrome(num):
            # abc => cba
            # abc //= 10 => ab
            # ab*pow(10, 3)+cba
            cur = num
            rev = digits = 0
            while cur > 0:
                rev = rev*10 + cur%10
                cur //= 10
                digits += 1
            return num * pow(10, digits) + rev
            
        length = 1
        res = cnt = 0
        while cnt < n:
            start = pow(10, length-1)
            end = pow(10, length)
            for num in range(start, end):
                val = genOddPalindrome(num)
                if kMirror(val):
                    cnt += 1
                    res += val
                    if cnt == n: return res

            for num in range(start, end):
                val = genEvenPalindrome(num)
                if kMirror(val):
                    cnt += 1
                    res += val
                    if cnt == n: return res
            length += 1
        return res
