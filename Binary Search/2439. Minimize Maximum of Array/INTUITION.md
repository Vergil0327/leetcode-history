# Intuition

由於只能右邊往左邊送，最左邊nums[0]無法減少，所以最少只能是nums[0]
看起來可以用二分搜值，threshold越大，越容易達成
越小越難，看起來有單調性

檢查一下這個想法:
如果threshold可以是5，那6也肯定可以
如果無法每個都<=4，那麼threshold也肯定不能是3
