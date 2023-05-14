class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        original0 = [0]
        original1 = [1]
        for i in range(n):
            num = derived[i]
            if num == 0:
                # original[i] == original[i+1]
                original0.append(original0[i])
                original1.append(original1[i])
                if i == n-1:
                    if original0[i] == original0[0]: return True
                    if original1[i] == original1[0]: return True
            else:
                # original[i] != original[i+1]
                original0.append(1-original0[i])
                original1.append(1-original1[i])
                if i == n-1:
                    if original0[i] != original0[0]: return True
                    if original1[i] != original1[0]: return True
            
        return False
