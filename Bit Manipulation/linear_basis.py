# explanation: leetcode 3681 for example (https://www.youtube.com/watch?v=M4UMLvrEh-A)
# construct basis:
# ```
# basis = []
# for x in nums:
#     for b in basis:
#         x = min(x, x^b)
#     if x > 0:
#         basis.append(x)
# ```

# 有了xor basis後
# ex. nums = [9,11,12,14], 他的XOR basis=[12,5,2] (=[0b1100, 0b0101, 0b0010])
# 可透過greedy algorithm 找出max xor value: res = max(res, res^b) where b in basis
def find_max_xor(nums):
    basis = []
    for x in nums:
        for b in basis:
            x = min(x, x^b)
        if x > 0:
            basis.append(x)

    res = 0
    basis.sort(reverse=True)
    for b in basis:
        res = max(res, res^b)
    return res

# basis有點單位向量的感覺, 找出每個高位bit的basis value
# 互不衝突 (basis[i]的最高位bit, leading 1, 會位於i位)
# basis[1] = 0b1X
# basis[2] = 0b1XX
# basis[3] = 0b1XXX
# ...
# 找到後就利用greedy的方式, 每個可取或不取, 去找出最大max XOR value
def find_max_xor(nums):
    basis = [0] * 32
    for num in nums:
        # find leading 1
        for i in range(31, -1, -1):
            if ((num>>i)&1) == 0: continue
            if basis[i] == 0:
                basis[i] = num
                break

            num ^= basis[i]

    res = 0
    for i in range(31, -1, -1):
        res = max(res, res^basis[i])
    return res