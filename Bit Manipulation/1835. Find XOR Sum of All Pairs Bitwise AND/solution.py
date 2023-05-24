class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        xor1 = arr1[0]
        for i in range(1, len(arr1)):
            xor1 = xor1^arr1[i]
        
        xor2 = arr2[0]
        for i in range(1, len(arr2)):
            xor2 = xor2^arr2[i]

        return xor1&xor2