# hashset
class Solution:
    def isHappy(self, n: int) -> bool:
        def sumDigit(n):
            total = 0
            while n:
                num = n%10
                total += num ** 2
                n //= 10
            return total

        visited = set()
        while n > 1:
            if n in visited:
                return False
            visited.add(n)
            n = sumDigit(n)

        return True

# floyd algorithm, slow-fast pointer
class Solution:
    def isHappy(self, n: int) -> bool:
        def sumDigit(n):
            total = 0
            while n:
                num = n%10
                total += num ** 2
                n //= 10
            return total

        slow = fast = n
        slow = sumDigit(slow)
        fast = sumDigit(sumDigit(fast))
        while slow != fast:
            slow = sumDigit(slow)
            fast = sumDigit(sumDigit(fast))

        # detect cycle
        if slow == 1:
            return True
        else:
            return False