class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        def XOR(arr):
            for i in range(1, len(arr)):
                arr[0] ^= arr[i]
            return arr[0]

        # perm = [1,2,3,...,len(encoded)+1]
        n = len(encoded)+1
        perm0 = XOR([i for i in range(1, n+1)]) ^ XOR([encoded[i] for i in range(1, len(encoded), 2)])
        perm = [perm0]
        for i in range(1, n):
            # encoded[i] = perm[i] XOR perm[i+1] => perm[i] = encoded[i-1] XOR perm[i-1]
            perm.append(encoded[i-1]^perm[i-1])
        return perm
