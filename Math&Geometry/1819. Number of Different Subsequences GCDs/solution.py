class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        nums = list(set(nums))

        def findFactors(num):
            facs = set()
            for x in range(1, int(sqrt(num))+1):
                if num%x == 0:
                    facs.add(x)
                    facs.add(num//x)
            return facs

        factors = defaultdict(list)
        for num in nums:
            for f in findFactors(num):
                if not factors[f]:
                    factors[f].append(num)
                else:
                    factors[f][0] = gcd(factors[f][0], num)

        def check(target):
            arr = factors[target]
            if not arr: return False

            return arr[0] == target

        res = 0
        for target_gcd in range(1, max(nums)+1):
            if check(target_gcd):
                res += 1
        return res
    

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        mx_num = max(nums)
        seen = set(nums)

        res = 0
        for target_gcd in range(1, mx_num+1):
            gcd = 0
            for num in range(target_gcd, mx_num+1, target_gcd):
                if num in seen:
                    gcd = math.gcd(gcd, num)
                    if gcd == target_gcd:
                        res += 1
                        break
        return res