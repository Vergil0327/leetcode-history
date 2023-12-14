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

<!-- 2023/12/14 -->

# Intuition

index subset {1, 2, 3, ..., n}, 要找出個subset使得任意配對的乘積為perfect square
代表{i, j, k, ...} = {
    i = a * x^2 * y^2,
    j = b * x^2,
    k = c * d * y^2 * z^2,
}

其中的完全平方項是完全可以去除的, 我們真正關注的就只有那些非完全平方向的係數
所以可轉化成{
    i = a
    j = b
    k = c*d
}
那這個subset如果要任意乘績皆為完全平方向的話, 代表:
a*b, b*(c*d), a*(c*d)都必須是完全平方
也就代表必須滿足 a=b, b=c*d, a=c*d, 這樣通通都能轉成k^2
所以對於每個index來說, 他們的質因數乘積就是key, 同樣的key會落在同個complete subset裡
我們計算這些subset的總和, 取全局最大即為答案