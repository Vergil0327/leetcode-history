class Solution:
    def largestPalindrome(self, n: int) -> int:
        MOD = 1337

        def formatPalindrome(num):
            s = str(num)
            return int(s + s[::-1])

        # enumerate palindromic integer from largest to lowest
        # since we format palindromic integer by concatenating 2 str, we enumerate 2-digit-atleast palindrome
        # exclude 0, 1, 2, 3, 4, 5, 6, 7 8, 9 which single number is also a palindrome
        lo = 10**(n-1)
        hi = 10**n - 1
        for num in range(hi, lo-1, -1):
            pal = formatPalindrome(num)
            for divisor in range(hi, int(sqrt(pal))-1, -1):
                # find two n-digits product
                # n-digits num must >= lo (lo is minimum n-digit number) and <= hi (hi is maximum n-digit number)
                if pal%divisor == 0 and hi >= pal//divisor >= lo and hi >= divisor >= lo:
                    return pal%1337

        return 9 # 9 is maximum palindromic integer when n = 1

