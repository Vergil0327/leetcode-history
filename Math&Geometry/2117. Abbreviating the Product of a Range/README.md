[2117. Abbreviating the Product of a Range](https://leetcode.com/problems/abbreviating-the-product-of-a-range/)

`Hard`

You are given two positive integers left and right with left <= right. Calculate the product of all integers in the inclusive range [left, right].

Since the product may be very large, you will abbreviate it following these steps:

Count all trailing zeros in the product and remove them. Let us denote this count as C.
For example, there are 3 trailing zeros in 1000, and there are 0 trailing zeros in 546.
Denote the remaining number of digits in the product as d. If d > 10, then express the product as <pre>...<suf> where <pre> denotes the first 5 digits of the product, and <suf> denotes the last 5 digits of the product after removing all trailing zeros. If d <= 10, we keep it unchanged.
For example, we express 1234567654321 as 12345...54321, but 1234567 is represented as 1234567.
Finally, represent the product as a string "<pre>...<suf>eC".
For example, 12345678987600000 will be represented as "12345...89876e5".
Return a string denoting the abbreviated product of all integers in the inclusive range [left, right].

```
Example 1:
Input: left = 1, right = 4
Output: "24e0"
Explanation: The product is 1 × 2 × 3 × 4 = 24.
There are no trailing zeros, so 24 remains the same. The abbreviation will end with "e0".
Since the number of digits is 2, which is less than 10, we do not have to abbreviate it further.
Thus, the final representation is "24e0".

Example 2:
Input: left = 2, right = 11
Output: "399168e2"
Explanation: The product is 39916800.
There are 2 trailing zeros, which we remove to get 399168. The abbreviation will end with "e2".
The number of digits after removing the trailing zeros is 6, so we do not abbreviate it further.
Hence, the abbreviated product is "399168e2".

Example 3:
Input: left = 371, right = 375
Output: "7219856259e3"
Explanation: The product is 7219856259000.
``` 

Constraints:

- 1 <= left <= right <= 10^4

<details>
<summary>Hint 1</summary>

Calculating the number of trailing zeros, the last five digits, and the first five digits can all be done separately.

</details>
<details>
<summary>Hint 2</summary>

Use a prime factorization property to find the number of trailing zeros. Use modulo to find the last 5 digits. Use a logarithm property to find the first 5 digits.

</details>
<details>
<summary>Hint 3</summary>

The number of trailing zeros C is nothing but the number of times the product is completely divisible by 10. Since 2 and 5 are the only prime factors of 10, C will be equal to the minimum number of times 2 or 5 appear in the prime factorization of the product.

</details>
<details>
<summary>Hint 4</summary>

Iterate through the integers from left to right. For every integer, keep dividing it by 2 as long as it is divisible by 2 and C occurrences of 2 haven't been removed in total. Repeat this process for 5. Finally, multiply the integer under modulo of 10^5 with the product obtained till now to obtain the last five digits.

</details>
<details>
<summary>Hint 5</summary>

The product P can be represented as P=10^(x+y) where x is the integral part and y is the fractional part of x+y. Using the property "if S = A * B, then log(S) = log(A) + log(B)", we can write x+y = log_10(P) = sum(log_10(i)) for each integer i in [left, right]. Once we obtain the sum, the first five digits can be represented as floor(10^(y+4)).

</details>