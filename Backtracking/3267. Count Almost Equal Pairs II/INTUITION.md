# Intuition

這題為[3265. Count Almost Equal Pairs I](https://leetcode.com/problems/count-almost-equal-pairs-i/)的follow-up
我們可以進行**至多**兩次的操作使得nums[i]跟nums[j]是**almost equal**

我們觀察一下會得到以下幾種情況, 唯一個想法就是用O(n^2)時間去檢查每個pair, 並分成以下幾種情況討論

**情況1**
diff=0 => equal

**情況2**
"12345"
"12355" => 不可能透過swap讓兩邊相等

**情況3**
"12345"
"12354" => diff=2, swap=1

**情況4**
"12345"
"12534" => diff=3, swap=2

**情況5**
"12345"
"21354" => diff=4, swap=2

**情況6**
diff > 5 => invalid

```py
class Solution:
    def countPairs(self, nums: List[int]) -> int:
        n = len(nums)

        return sum(int(self.almostEqual(nums[i], nums[j])) for i in range(n) for j in range(i+1, n))

    def almostEqual(self, a, b):
        arr1, arr2 = [], []
        while a > 0 or b > 0:
            if (a%10 != b%10):
                arr1.append(a%10)
                arr2.append(b%10)
            a //= 10
            b //= 10

            if len(arr1) >= 4: break

        if len(arr1) <= 1: return len(arr1) == 0
        if len(arr1) == 2 or len(arr1) == 3:
            arr1.sort()
            arr2.sort()
            return a == b and arr1 == arr2 # remaining part equals and swap digits equal

        for i in range(3):
            for j in range(i+1, 4):
                if arr1[i] == arr2[j] and arr1[j] == arr2[i]:
                    arr1.sort()
                    arr2.sort()
                    return a == b and arr1 == arr2
        return False
```

但python時間壓得很緊, 這樣會TLE
還不如單純brute force, see [[Python3] Brute Force by @awice](https://leetcode.com/problems/count-almost-equal-pairs-ii/solutions/5686824/python3-brute-force/)

