# Intuition

不確定想法是不是正確，但我是這樣想的
想法是三層for-loop循環找出nums[i], nums[j], nums[k]有這些可能

前三層循環都不同數:
nums[i] != nums[j] != nums[k]
(nums[i] | nums[j]) & nums[k] ^
(nums[i] | nums[k]) & nums[j] ^
(nums[i] | nums[j]) & nums[k] ^
(nums[j] | nums[k]) & nums[i] ^
(nums[i] | nums[k]) & nums[j] ^
(nums[j] | nums[k]) & nums[i] ^
-> all cancel

前兩層循環同數:
(nums[i] | nums[i]) & nums[j] ^
(nums[i] | nums[i]) & nums[k] ^
(nums[j] | nums[j]) & nums[i] ^
(nums[j] | nums[j]) & nums[k] ^
(nums[k] | nums[k]) & nums[i] ^
(nums[k] | nums[k]) & nums[j] ^
equals:
  nums[i] & nums[j] ^
  nums[i] & nums[k] ^
  nums[j] & nums[i] ^
  nums[j] & nums[k] ^
  nums[k] & nums[i] ^
  nums[k] & nums[j] ^
-> all cancel

擴增到任兩層
(nums[i] | nums[j]) & nums[i] ^
(nums[i] | nums[k]) & nums[i] ^
(nums[j] | nums[i]) & nums[j] ^
(nums[j] | nums[k]) & nums[j] ^
(nums[k] | nums[i]) & nums[k] ^
(nums[k] | nums[j]) & nums[k] ^
-> all cancel

三層循環都同個數:
(nums[i] | nums[i]) & nums[i] ^
(nums[j] | nums[j]) & nums[j] ^
(nums[k] | nums[k]) & nums[k] ^
equals:
  nums[i] ^
  nums[j] ^
  nums[k] ^

所以最後就同等於每個`num` in `nums` XOR

I'm not sure if I'm correct or not, but this is what I come up with.

```
if we brute force with 3 nested for-loop:

each loop find different nums[i], nums[j], nums[k]
nums[i] != nums[j] != nums[k]
(nums[i] | nums[j]) & nums[k] ^
(nums[i] | nums[k]) & nums[j] ^
(nums[i] | nums[j]) & nums[k] ^
(nums[j] | nums[k]) & nums[i] ^
(nums[i] | nums[k]) & nums[j] ^
(nums[j] | nums[k]) & nums[i] ^
-> all cancel

2 loop with same num and 1 different
(nums[i] | nums[i]) & nums[j] ^
(nums[i] | nums[i]) & nums[k] ^
(nums[j] | nums[j]) & nums[i] ^
(nums[j] | nums[j]) & nums[k] ^
(nums[k] | nums[k]) & nums[i] ^
(nums[k] | nums[k]) & nums[j] ^

(nums[i] | nums[j]) & nums[i] ^
(nums[i] | nums[k]) & nums[i] ^
(nums[j] | nums[i]) & nums[j] ^
(nums[j] | nums[k]) & nums[j] ^
(nums[k] | nums[i]) & nums[k] ^
(nums[k] | nums[j]) & nums[k] ^
-> all cancel

three for-loop with same num
(nums[i] | nums[i]) & nums[i] ^
(nums[j] | nums[j]) & nums[j] ^
(nums[k] | nums[k]) & nums[k] ^

equals:
  nums[i] ^
  nums[j] ^
  nums[k] ^
```

therefore, we only need to XOR every num together

[same idea with mine](https://leetcode.com/problems/find-xor-beauty-of-array/solutions/3015014/why-just-xor-of-all-numbers-works/?orderBy=most_votes)

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(1)$$
