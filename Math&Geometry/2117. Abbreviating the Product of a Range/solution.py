class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        pre = suf = 1
        zeros = 0
        mod = pow(10, 16)
        total_digits = 0

        for num in range(left, right+1):
            # suf & trailing zeros
            suf *= num
            while suf%10 == 0:
                suf //= 10
                zeros += 1

            suf %= mod

            pre *= num
            while pre%10 == 0:
                pre //= 10
                total_digits += 1
            
            while pre >= mod:
                pre //= 10
                total_digits += 1

                
        suf = str(suf)[-5:]
        pre = str(pre)
        total_digits += len(pre)
        digit_len = total_digits - zeros

        pre = pre[:min(5, max(0, total_digits-zeros-5))]
        if digit_len <= 5:
            return f"{suf}e{zeros}"
        elif digit_len <= 10:
            return f"{pre}{suf}e{zeros}"
        else:
            return f"{pre}...{suf}e{zeros}"
