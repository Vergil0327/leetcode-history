[282. Expression Add Operators](https://leetcode.com/problems/expression-add-operators/description/)

`Hard`

Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

```
Example 1:
Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.

Example 2:
Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.

Example 3:
Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
```

Constraints:

- 1 <= num.length <= 10
- num consists of only digits.
- -2^31 <= target <= 2^31 - 1

<details>
<summary>Hint 1</summary>

Note that a number can contain multiple digits.

</details>

<details>
<summary>Hint 2</summary>

Since the question asks us to find **all** of the valid expressions, we need a way to iterate over all of them. (Hint: Recursion!)

</details>

<details>
<summary>Hint 3</summary>

We can keep track of the expression string and evaluate it at the very end. But that would take a lot of time. Can we keep track of the expression's value as well so as to avoid the evaluation at the very end of recursion?

</details>

<details>
<summary>Hint 4</summary>

Think carefully about the multiply operator. It has a higher precedence than the addition and subtraction operators.
1 + 2 = 3
1 + 2 - 4 --> 3 - 4 --> -1
1 + 2 - 4 * 12 --> -1 * 12 --> -12 (WRONG!)
1 + 2 - 4 * 12 --> -1 - (-4) + (-4 * 12) --> 3 + (-48) --> -45 (CORRECT!)

</details>

<details>
<summary>Hint 5</summary>

We simply need to keep track of the last operand in our expression and reverse it's effect on the expression's value while considering the multiply operator.

</details>