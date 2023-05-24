# Intuition

```
arr1 = A B C
arr2 = X Y Z

pairs:
AX AY AZ
BX BY BZ
CX CY CZ

if:
    AX XOR AY

then:
    A AND X
        - 如果包含 A AND Y, 會在XOR操作被消掉
    A AND Y
        - 如果包含 A AND X, 會在XOR操作被消掉

=> AX XOR AY = A AND (X XOR Y)
=> 代表可以提出共同項
```

thus:

```
AX XOR AY XOR AZ = (A AND (X XOR Y)) XOR AZ
                 = A(X^Y) XOR AZ
                 = A AND (X^Y XOR Z)
                 = A AND (X^Y^Z)

BX XOR BY XOR BZ = B AND (X^Y^Z)
CX XOR CY XOR CZ = C AND (X^Y^Z)
```

```
answer = (AX XOR AY XOR AZ) XOR (BX XOR BY XOR BZ) XOR (CX XOR CY XOR CZ) 
       = (A AND (X^Y^Z)) XOR (B AND (X^Y^Z)) XOR (C AND (X^Y^Z))
       = (X^Y^Z) AND (A XOR B XOR C) # 提出共同項
       = XOR_SUM(arr1) AND XOR_SUM(arr2)
```