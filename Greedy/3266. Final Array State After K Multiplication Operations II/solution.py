from sortedcontainers import SortedList
class Solution:
    def getFinalState(self, nums: List[int], k: int, mul: int) -> List[int]:
        if mul == 1: return nums

        mod = 10**9 + 7
        sl = SortedList([num, i] for i, num in enumerate(nums))

        mnIdx, mxIdx = sl[0][1], sl[-1][1]
        def check(sl):
            if sl[0][1] != mnIdx: return True

            target = -1
            for num, i in sl:
                if i == mxIdx:
                    target = num
                    break
            return sl[0][0] * mul <= target
            
        while k and check(sl):
            k -= 1
            num, i = sl.pop(0)
            sl.add([num*mul, i])


        if k == 0:
            for num, i in sl:
                nums[i] = num%mod
            return nums

        order = []
        while k:
            k -= 1
            num, i = sl.pop(0)
            sl.add([num*mul, i])
            order.append(i)

            if len(order)%2 == 0 and order[:len(order)//2] == order[len(order)//2:]:
                break
        if k == 0:
            for num, i in sl:
                nums[i] = num%mod
            return nums

        order = order[:len(order)//2]
        n = len(order)

        q, r = divmod(k, n)
        for _ in range(r):
            num, i = sl.pop(0)
            sl.add([num*mul, i])
        
        for num, i in sl:
            nums[i] = num * pow(mul, q, mod) % mod
        return nums