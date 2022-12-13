#   123
# x 456
#   [1,8]
# [1,2]
# [6]
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        
        res = [0] * (m+n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                curr = int(num1[i]) * int(num2[j])
                digit10, digit = i+j, i+j+1
                res[digit] += curr
                res[digit10] += res[digit]//10
                res[digit] = res[digit]%10
        
        # remove leading zero
        i = 0
        while i<len(res) and res[i] == 0:
            i += 1

        if i == len(res): return "0"
        return "".join(map(str, res[i:]))

#   123
# x 456
# simulate human calculation
# its' work in Python but not other language. integer migh overflow
class Solution_unqualified:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        res = 0
        
        baseShift = 0
        for i in range(m-1, -1, -1):
            tmp = 0
            carry = 0
            base = 0 + baseShift
            for j in range(n-1, -1, -1):
                curr = int(num1[i]) * int(num2[j]) + carry
                tmp += (curr%10) * (10**base)
                carry = curr//10 # 進位
                base += 1 # 個位數 -> 十位數 -> 百位數
            res += tmp
            res += carry * (10**base) # don't forget to add carry at last round
            baseShift += 1 # 個位數 -> 十位數 -> 百位數
        return str(res)
