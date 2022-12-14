# Stack

## Intuition

use `left` & `right` stack to trace `"("` and `")"`

- when current character is `"("`, check if single right `")"` exists:

  - if exists, `count+1` and keep checking if left parenthesis `"("` exists to pair with
    - if `"("` did not exists, count+1
    - else pop out

- when current character is `")"`, check if single right `")"` exists:

  - if exists, pair up and keep checking if left parenthesis `"("` also exists to pair with
    - if `"("` did not exists, `count+1`
    - else pop out

- after iteration, check `left` & `right` again

  - check `right` first, if `right` is not empty

    it's only possible to have one sigle `")"`, `count+1`, and keep checking `left`:
    - if `"("` didn't exist to pair with, `count+1` 
    - else pop out

  - check `left`, if `left` is not empty

    each `"("` needs 2 `")"` to pair with, `count+2` per each


## Complexity
- Time complexity:

$$O(n)$$

- Space complexity:

$$O(n)$$