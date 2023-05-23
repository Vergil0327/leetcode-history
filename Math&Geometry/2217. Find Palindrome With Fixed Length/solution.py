class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        def flip(num, n):
            res = 0
            while num:
                mod = num%10
                num //= 10
                
                res += mod * 10**(n-1)
                n -= 1
            return res

        res = []
        for i in range(len(queries)):
            if intLength%2 == 0:
                n = intLength//2
                
                # 100-999 -> 900 valid
                # 100 -> 100001
                # 999 -> 999999
                if queries[i] > 9 * 10**(n-1):
                    res.append(-1)
                    continue

                first_half = 10**(n-1) + (queries[i]-1)
                second_half = flip(first_half, n)
                res.append(first_half * 10**n + second_half)
            else:
                # 100-999 -> 900 valid
                # 100 -> 10001
                # 999 -> 99999
                n = intLength//2+1
                if queries[i] > 9 * 10**(n-1):
                    res.append(-1)
                    continue

                first_half = 10**(n-1) + (queries[i]-1)
                second_half = flip(first_half//10, n-1)
                
                # n=4: first_half = XXXY, second_half=XXX
                res.append(first_half * 10**(n-1) + second_half)
        return res

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        res=[]
        isEven = intLength%2 == 0
        n = intLength//2 if isEven else intLength//2+1
        limit = 9 * 10**(n-1)
        for i in range(len(queries)):
            if queries[i] > limit:
                res.append(-1)
                continue
            
            first_half = str(10**(n-1) + (queries[i]-1))
            if isEven:
                second_half = first_half[::-1]
            else:
                second_half = first_half[::-1][1:]
            res.append(int(first_half + second_half))
        return res
