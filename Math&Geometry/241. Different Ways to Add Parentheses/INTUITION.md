### Divide & Conquer

let's see this example, `expr = "2*3-4*5"`

if we try to add parenthesis to it, it can be:

```
(2)*(3-4*5)
    (2)*([3]-[4*5])
    (2)*([3-4]*[5])
(2*3)-(4*5)
(2*3-4)*(5)
    ([2*3]-4)*(5)
    (2*[3-4])*(5)
```

it looks like a recursion problem

we need to add parenthesis to **left portion** and **right portion** whenever we iterate at `+`, `-` or `*`

and the **base case** of recursion would be whenever **there is no operator in expr[i:j+1]**

thus, we can use a recursion function accepts `i` & `j` to express `expr[i:j+1]` and add split left portion and right portion whenver we encounter operator


#### Altorithm - Divide & Conquer

step 1-3 is divide
step 4 is merge & conquer

1. iterate through `expr[i:j+1]`

    ```python
    for k in range(i, j+1):
    ```

2. if there is a operator, split left & right portion and handle recursively

    ```python
    if expr[k] in {"+","-","*"}:
        left = recursion(i, k-1)
        right = recursion(k+1, j)
    ```

3. base case

    if i == j, which means only one numeric character

    ex. expr[i:j+1]="2"

    ```python
    res.append(int(expr[i:j+1]))
    ```

    special case, if there is no operator, we still need to append to results

    ex. expr[i:j+1]="21"

    ```python
    res.append(int(expr[i:j+1]))
    ```

4. at post-order cursion position

    we'll get our left portion of numeric values & right portion of numeric values

    base on current operator, calculate & append to results, like merge sort

#### Optimization

if expr = "1+1+1+1+1", we'll get these two and compute same result twice

("1+1") + ("1+1+1")
("1+1+1") + ("1+1")

thus, we can use memorization technique to cache result

```python
if expr[i:j+1] in memo:
    return memo[expr[i:j+1]]

...

memo[expr[i:j+1]] = res
return res
```

or just use python built-in decorator `@functools.lru_cache(None)`