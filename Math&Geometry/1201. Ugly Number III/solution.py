class Solution:
    def gcd(self, a, b):
        if a < b:
            return self.gcd(b, a)

        # a > b
        while b:
            a, b = b, a%b 
        return a

    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:        
        def lcm(x, y):
            return x * y // self.gcd(x, y)
        
        def countUgly(k):
            setA = k // a
            setB = k // b
            setC = k // c
            setAB = k // lcm(a,b)
            setAC = k // lcm(a,c)
            setBC = k // lcm(b,c)
            setABC = k // lcm(lcm(a,b), c)
            nums = [setA, setB, setC, -setAB, -setAC, -setBC, setABC]

            return sum(nums)
        
        l, r = 1, int(2e9)
        while l < r:
            mid = l + (r-l)//2
            cnt = countUgly(mid)
            if cnt < n:
                l = mid+1

            # ! we can't directly return mid if cnt == n
            # ex. if cnt = k when mid=6 [2,3,4]
            # mid=7 [2,3,4], cnt is still k
            # ? what we want is first occurence
            # ? thus, we need to find lowerbound
            else:
                r = mid
        return l

# Brute Force
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        nums = []
        i = 2
        while len(nums) < n:
            if i%a == 0:
                if not nums or nums[-1] != i:
                    nums.append(i)
            if i%b == 0:
                if not nums or nums[-1] != i:
                    nums.append(i)
            if i%c == 0:
                if not nums or nums[-1] != i:
                    nums.append(i)
            i += 1

        return nums[n-1]