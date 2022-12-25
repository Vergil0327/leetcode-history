[2517. Maximum Tastiness of Candy Basket](https://leetcode.com/problems/maximum-tastiness-of-candy-basket/description/)

`Medium`

You are given an array of positive integers price where price[i] denotes the price of the ith candy and a positive integer k.

The store sells baskets of k distinct candies. The tastiness of a candy basket is the smallest absolute difference of the prices of any two candies in the basket.

Return the maximum tastiness of a candy basket.

```
Example 1:
Input: price = [13,5,1,8,21,2], k = 3
Output: 8
Explanation: Choose the candies with the prices [13,5,21].
The tastiness of the candy basket is: min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8.
It can be proven that 8 is the maximum tastiness that can be achieved.

Example 2:
Input: price = [1,3,1], k = 2
Output: 2
Explanation: Choose the candies with the prices [1,3].
The tastiness of the candy basket is: min(|1 - 3|) = min(2) = 2.
It can be proven that 2 is the maximum tastiness that can be achieved.

Example 3:
Input: price = [7,7,7,7], k = 2
Output: 0
Explanation: Choosing any two distinct candies from the candies we have will result in a tastiness of 0.
```

Constraints:

- 1 <= price.length <= 10^5
- 1 <= price[i] <= 10^9
- 2 <= k <= price.length

<details>
<summary>Hint 1</summary>

The answer is binary searchable.

</details>

<details>
<summary>Hint 2</summary>

For some x, we can use a greedy strategy to check if it is possible to pick k distinct candies with tastiness being at least x.

</details>

<details>
<summary>Hint 3</summary>

Sort prices and iterate from left to right. For some price[i] check if the price difference between the last taken candy and price[i] is at least x. If so, add the candy i to the basket.

</details>

<details>
<summary>Hint 4</summary>

So, a candy basket with tastiness x can be achieved if the basket size is bigger than or equal to k.

</details>