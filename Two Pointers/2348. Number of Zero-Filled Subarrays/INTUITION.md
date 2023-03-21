# Intuition

只要是要找subarray, 我們可以試著找出固定左右邊界的方法
只要鎖定左右邊界，定義出subarray

用Two Pointers [l:r]，從左往右移動
每當nums[r]不為0, `l`也跟著移動，
每當nums[r]等於0, `l`便先不移動
如此一來，我們便會維護一個[l:r]區間其中包含的數都是0

# Optimized

另外，這題也可以更簡化來計算，並不需要two pointers

X X X X 0 0 0 0 X X X X
        i

我們紀錄當前連續0的個數 `zeros`
- 我們每當`nums[i] == 0`, `zeros += 1`, 此時subarray也就 += `zeros`
- 每當`nums[i] != 0`, `zeros = 0`

如此一來時間複雜度便從O(2n)變為O(n)