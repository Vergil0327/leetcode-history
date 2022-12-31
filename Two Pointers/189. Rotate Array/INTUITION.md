# Space O(1)

## Intuition

這題的O(1)解法很巧妙，做法是:

1. 先反轉整個`nums`
2. 對`前k個`數反轉回來
3. 對`後k個`數反轉回來
4. 即為所求


ex. k = 2, nums = [1,2,3,4,5]

1. [5,4,3,2,1]
2. [4,5,3,2,1]
3. [4,5,1,2,3] -> Answer

ex. nums = "----->-->"; k =3
target = "-->----->";

reverse "----->-->" we can get "<--<-----"
reverse "<--" we can get "--><-----"
reverse "<-----" we can get "-->----->"