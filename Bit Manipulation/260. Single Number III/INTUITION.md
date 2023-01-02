# Intuition

if we XOR every num together, the final result `XOR` we get means:

let's say `num1` and `num2` are our targets
1. XOR = num1 ^ num2
2. if XOR = 100010, every `1` bit position means `num1` and `num2` differ at this bit position

ex. num1 = 111111, num2 = 011101 -> num1 ^ num2 = 100010

once we get this `XOR` information, we can split `nums` into two set

let's pick any bit with value `1` in `XOR`.

ex. use `XOR & -XOR` to get LSB (least significant bit)

1. every num & LSB = 1, `num` can be possible target `num1`
2. every num & LSB = 0, `num` can be possible target `num2`

and we XOR every possible `num1` and every possible `num2` separately,
we can remove duplicate and get our target `num1` and `num2`

# Apporoach

therefore, we can XOR every num together and we get the information:

XOR_RESULT = num1 ^ num2
let's pick LSB (least significant bit) to split nums into two sets:
1. one is num & LSB = 1
2. the other is num & LSB = 0

and we XOR these two set separately.

the final num in these two set are our target `num1` and `num2` since duplicate will be removed after XOR operation