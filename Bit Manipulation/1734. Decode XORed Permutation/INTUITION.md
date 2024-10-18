# Intuition


n = len(encoded)+1
perm = permutation of [1,2,3,...,n]

再來觀察一下:
encoded[i] = perm[i] XOR perm[i+1]
encoded[i+1] = perm[i+1] XOR perm[i+2]
encoded[i+2] = perm[i+2] XOR perm[i+3]

encode[i] XOR encoded[i+1] XOR ... XOR encoded[n-1] = perm[i] XOR perm[n-1]
encoded[i] XOR encoded[i+1] = perm[i] XOR perm[i+2]
encoded[i] XOR encoded[i+3] = perm[i] XOR perm[i+2] XOR perm[i+2] XOR perm[i+3]

XOR(perm) = XOR([1,2,3,...,n])
XOR(encoded[1],encoded[3],...,encoded[-1]) = XOR([2,3,4,...,n])

=> perm[0] = XOR(i in range(1, n+1)) XOR (encoded[i] for i in range(0, len(encoded), 2))

那在有了perm[0]之後, 後續只需要:
- `encoded[i] = perm[i] XOR perm[i+1]`
- => `perm[i+1] = encoded[i] XOR perm[i]`
- => `perm[i] = encoded[i-1] XOR perm[i-1]`