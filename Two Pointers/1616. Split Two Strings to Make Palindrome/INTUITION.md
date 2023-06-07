# Intuition

first of all, if either of a or b is palindrome, we can return True directly,
because we can split into a palindrome with emtpy string:

```
a = palindrome + ""
b = b + ""
then, we got palindrome + "" = palindrome
```

if neither of both isn't palindrome, we can move two pointer to check a[l] == b[r] or b[l] == a[r].
greedily shrink middle part, the shorter the middle part is the higher chance to be palindrome the middle part can have
once two pointers break early, check if a[l:r] or b[l:r] is palindrome or not

```
X | XXXXX
Y | YYYYY
=> X[YYYY]Y -> if it's palindrome, X==Y and [YYYY] is palindrome
=> Y[XXXX]X

XX | XXXX
YY | YYYY
=> XX[YY]YY -> XX == YY and [YY] is palindrome
=> YY[XX]XX

XXX | XXX
YYY | YYY
=> XXXYYY
=> YYYXXX

XXXX | XX
YYYY | YY
=> XX[XX]YY -> XX == YY and [XX] is palindrome
=> YY[YY]XX

XX|xx|XX
   l
YY|yy|YY
    r
```

we can see that we can compare two end of a and b first by using two pointers `l` & `r`
then, middle part will be a[l:r] or b[l:r] (both inclusive), it's symmetric.

once a[l:r] or b[l:r] is palindrome, return True
