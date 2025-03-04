# Intuition

1 2 3 4 5

以1為開頭:
- 5: 有5//2個位置
- 4: 有4//2個位置
- 3: 有3//2個位置
- 2: 有2//2個位置

1. if n is **odd**, the first element can only be **odd**
    - odd -> even -> odd .... -> odd: fact(oddNum) x fact(evenNum)
2. if n is **even**, the first element can be **odd** or **even**
    - odd -> even -> ... -> even or even -> odd .... -> odd

3. At position i, the remaining valid permutations if it is already decided which parity is to be placed here (even or odd): fact(oddNumLeft) x fact(evenNumLeft)
   - If n - i numbers are left, the count of permutations is: fact((n - i) / 2) x fact((n - i - 1) / 2)