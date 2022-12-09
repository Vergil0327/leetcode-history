class FollowUpSolution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        divisor = 5
        while divisor <= n:
            cnt += n // divisor
            divisor *= 5
        return cnt

class BetterSolution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0: return 0

        cnt = 0
        for num in range(1, n+1):
            if num%5 == 0:
                count5 = 0
                while num >= 5 and num%5==0:
                    count5 += 1
                    num //= 5
                cnt += count5
        return cnt

# Brute Force: O(n)
class AcceptedSolution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0: return 0
        def fact(n):
            num = 1
            for i in range(1, n+1):
                num *= i
            return num
        num = fact(n)
        
        cnt = 0
        while num>0:
            if num%10 == 0:
                cnt += 1
            else:
                break
            num //= 10
        return cnt
