# Intuition


`A XOR B XOR C` => duplicate will be removed by XOR

001
010
011
100
101
110
111

let's see number in 2-based.
since XOR will eliminate duplicate bit, we only need to consider how many permutations in current bit_length

2 possible bit (0|1) for each bit position => `answer = pow(2, bit_length())`
edge case: for n < 3: it'll have duplicate bit, therefore, answer = 2 for n < 3