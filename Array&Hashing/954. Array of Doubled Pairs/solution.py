class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        arr.sort()

        # [-4,-2,2,4]
        for num in arr:
            if counter[num] == 0: continue
            if num > 0:
                if counter[num * 2] == 0: return False
                counter[num] -= 1
                counter[num * 2] -= 1
            else:
                if num % 2 != 0: return False
                if counter[num//2] == 0: return False
                counter[num] -= 1
                counter[num // 2] -= 1

        
        return all(v == 0 for v in counter.values())

# Optimized
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter = Counter(arr)

        for num in sorted(counter.keys(), key=abs):
            counter[2*num] -= counter[num]
            if counter[2*num] < 0: return False
        return True