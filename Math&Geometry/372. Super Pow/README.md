[372. Super Pow](https://leetcode.com/problems/super-pow/description/)

`Medium`

Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

```
Example 1:
Input: a = 2, b = [3]
Output: 8

Example 2:
Input: a = 2, b = [1,0]
Output: 1024

Example 3:
Input: a = 1, b = [4,3,3,8,5,2]
Output: 1
```

Constraints:

- 1 <= a <= 2^31 - 1
- 1 <= b.length <= 2000
- 0 <= b[i] <= 9
- b does not contain leading zeros.

<details>
<summary>Solution</summary>
这道题可以有三个难点：

一是如何处理用数组表示的指数，现在 b 是一个数组，也就是说 b 可以非常大，没办法直接转成整型，否则可能溢出。你怎么把这个数组作为指数，进行运算呢？

```
b = [1,5,6,4]
a ^ [1,5,6,4] = (a^4) * (a^[1,5,6,0]) = (a^4) * (a^[1,5,6])^10 # recursion
```

二是如何得到求模之后的结果？按道理，起码应该先把幂运算结果算出来，然后做 % 1337 这个运算。但问题是，指数运算结果肯定会大得吓人，也就是说，算出来真实结果也没办法表示，早都溢出报错了。

```
(a * b) % k = (a % k)(b % k) % k
```

三是如何高效进行幂运算

```markdown
a^b equals to:
- a * a^(b-1), b is odd
- (a^(b/2))^2, b is even
```

```java
int base = 1337;

int mypow(int a, int k) {
    if (k == 0) return 1;
    a %= base;

    if (k % 2 == 1) {
        // k 是奇数
        return (a * mypow(a, k - 1)) % base;
    } else {
        // k 是偶数
        int sub = mypow(a, k / 2);
        return (sub * sub) % base;
    }
}
```

[Chinese Explanation](https://labuladong.github.io/algo/4/32/117/)
</details>