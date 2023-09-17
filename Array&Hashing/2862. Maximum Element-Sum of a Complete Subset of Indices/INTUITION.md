# Intuition

[Solution by @lee215](https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/solutions/4053876/java-c-python-square-factorization-o-n/)

這題是個觀察題，最關鍵的地方是:

*A set of numbers is complete if the product of every pair of its elements is a perfect square.*

所以我們的complete set是1-indexed的index, 任兩個配對相乘後為perfect square, 這時的subset sum即為合法解
目標是找出globally maximum valid subset sum

所以對於一個complete subset來說, 我們可以將每個nums[i]的square number都先除掉
這樣剩下來的prime factor, 必定每個都相等 => 因為這樣任兩個相乘才會是perfect square, 才會是complete subset
這就代表每個nums[i]除掉所有perfect square後, 剩下的就是他們的key

所以對於一個complete subset, 裡面每個element的key都會是相等的
因此我們可以用hashmap來用這個key來儲存每個complete subset的subset sum

```py
for i, num in enumerate(nums, start=1):
    for p in range(2, int(sqrt(i))+1):
        square = p*p
        while i%square == 0:
            i //= square

    # key = i
    # continue...
```

由於nums[i]除掉所有perfect square後, 最後剩下的prime factor就是每個nums[i]的key
因此我們可以遍歷每個nums[i], 找出key後用hashset記錄每個key的subset sum, 其中每個key都代表一個complete subset

```py
count[key] += num
```