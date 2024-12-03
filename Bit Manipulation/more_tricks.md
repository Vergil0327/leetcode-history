[Basic Tricks](https://www.informit.com/articles/article.aspx?p=1959565)


gray code: https://cp-algorithms.com/algebra/gray-code.html

```py
def grayCode(n):
    return n ^ (n >> 1)
```
