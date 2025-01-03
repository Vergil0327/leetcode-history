# Intuition-1

pow(2, x) = one of permutations(n)
取log2: x = log2(perm) for perm in permutations(n)

n <= 10^9 => 9位數的permutations時間上為 9! = 362880
數字規模可接受, 因此直接遍歷permutations即可

time: O(str(n).length !)

# Intuition-2

反過來想, 遍歷power of 2然後看能不能對應到n

time: O(log2(10**9) * str(n).length)