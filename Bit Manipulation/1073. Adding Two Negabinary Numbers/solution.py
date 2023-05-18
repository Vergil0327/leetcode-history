class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.reverse()
        arr2.reverse()

        res = [0] * 1005

        i = j = idx = 0
        m, n = len(arr1), len(arr2)
        while i < m or j < n:
            curr = res[idx]
            if i < m:
                curr += arr1[i]
                i += 1
            
            if j < n:
                curr += arr2[j]
                j += 1
            res[idx] = curr%2
            added = curr//2
            res[idx+1] += added
            res[idx+2] += added
            if res[idx+1] == 2 * res[idx+2]: # 相加為0
                res[idx+1] = res[idx+2] = 0
            
            idx += 1
        
        res.reverse()
        idx = 0
        while idx < len(res)-1 and res[idx] == 0:
            idx += 1
        return res[idx:]
    
# Concise Solution
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        
        carry = 0
        while arr1 or arr2 or carry:
            num1 = arr1.pop() if arr1 else 0
            num2 = arr2.pop() if arr2 else 0
            carry = carry + num1 + num2
            
            # res.append(carry%2)
            res.append(carry&1)

            # carry = -(carry//2)
            carry = -(carry>>1)
        
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return res[::-1]