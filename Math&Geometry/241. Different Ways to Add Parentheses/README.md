[241. Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/description/)

`Medium`

Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

```
Example 1:
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
```

Constraints:

- 1 <= expression.length <= 20
- expression consists of digits and the operator '+', '-', and '*'.
- All the integer values in the input expression are in the range [0, 99].

<details>
<summary>Solution</summary>

[Huifeng Guan-每日一題](https://www.youtube.com/watch?v=r2wZUlt2wJo&t=7s)

[labuladong - 分治法](https://labuladong.github.io/algo/4/33/122/)

对于运算表达式相关的问题，一般都会涉及括号以及优先级的问题，常用的技巧是分治算法，明确递归函数的定义，让递归函数去处理括号。

这题就要用分治思想解决，分而治之，先分后治：

1、明确函数定义，diffWaysToCompute 函数可以计算出输入算式的所有组合结果。

2、分，给某一个运算符左右加括号，将一个表达式分解成两个子表达式。

3、治，用 diffWaysToCompute 递归计算左右两个子表达式的所有结果。

4、用子表达式（子问题）的结果推导原表达式（原问题）的结果。

```java
class Solution {

    HashMap<String, List<Integer>> memo = new HashMap<>();

    public List<Integer> diffWaysToCompute(String input) {
        // 避免重复计算
        if (memo.containsKey(input)) {
            return memo.get(input);
        }
        List<Integer> res = new LinkedList<>();
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            // 扫描算式 input 中的运算符
            if (c == '-' || c == '*' || c == '+') {
                /******分******/
                // 以运算符为中心，分割成两个字符串，分别递归计算
                List<Integer>
                        left = diffWaysToCompute(input.substring(0, i));
                List<Integer>
                        right = diffWaysToCompute(input.substring(i + 1));
                /******治******/
                // 通过子问题的结果，合成原问题的结果
                for (int a : left)
                    for (int b : right)
                        if (c == '+')
                            res.add(a + b);
                        else if (c == '-')
                            res.add(a - b);
                        else if (c == '*')
                            res.add(a * b);
            }
        }
        // base case
        // 如果 res 为空，说明算式是一个数字，没有运算符
        if (res.isEmpty()) {
            res.add(Integer.parseInt(input));
        }
        // 将结果添加进备忘录
        memo.put(input, res);
        return res;
    }
}
```

</details>