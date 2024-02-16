# Intuition

we can transfer negative sign:

```
step1:
1 -1
0 1

step2:
-1 -1
-0 1

step3:
1 1
-0 1
```

we can combine above to do sth. like example 1

```
1 -1 1
1  1 1
-1 1 1

1 -1 1
-1 1 1
 1 1 1

-1 1 1
-1 1 1
 1 1 1

 1 1 1
 1 1 1
 1 1 1
```

**Conclusion**

1. if even number of negative sign => we can change all of them to be positive
2. if odd number of negative sign => we can leave only 1 negative sign and transfer negative sign to minimum abs(matrix[i][j])