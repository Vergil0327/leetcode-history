class Solution:
    def nearestPalindromic(self, n: str) -> str:
        x = self.findGreaterPalindrome(n)
        y = self.findSmallerPalindrome(n)

        if int(x)-int(n) < int(n)-int(y):
            return x
        else:
            return y

    def findSmallerPalindrome(self, s):
        n = len(s)
        arr = list(s)
        l, r = 0, n-1
        while l < r:
            arr[r] = arr[l]
            l, r = l+1, r-1

        res = "".join(arr)
        if int(res) < int(s):
            return res

        # find greater
        
        mid = (n-1)//2 # 取中間靠左的middle, 奇偶數長度都適用
        carry = 1
        for i in range(mid, -1, -1):
            d = int(arr[i]) - carry
            if d >= 0: # 順利 -= 1
                arr[i] = str(d)
                carry = 0
            else:
                arr[i] = "9"

            arr[n-1-i] = arr[i]

        if arr[0] == "0":
            # edge case: example 2
            if n == 1: return "0"

            return "9" * (n-1)
        else:
            return "".join(arr)

    def findGreaterPalindrome(self, s):
        n = len(s)
        arr = list(s)
        l, r = 0, n-1
        while l < r:
            arr[r] = arr[l]
            l, r = l+1, r-1

        res = "".join(arr)
        if int(res) > int(s):
            return res

        # find smaller
        
        mid = (n-1)//2 # 取中間靠左的middle, 奇偶數長度都適用
        carry = 1
        for i in range(mid, -1, -1):
            d = int(arr[i]) + carry
            if d < 10: # 順利 += 1
                arr[i] = str(d)
                carry = 0
            else:
                arr[i] = "0"

            arr[n-1-i] = arr[i]

        if carry == 1:
            res = ["0"] * (n+1)
            res[0] = res[-1] = "1"
            return "".join(res)
        else:
            return "".join(arr)
