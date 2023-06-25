# Intuition
由題意我們可知:
```
2^a + num2 + 2^b + num2 + 2^c + num2 = num1
 => {2^a+2^b+2^c+...} + n * num2 = num1
       n elements
=> {2^a+2^b+2^c+...} = num1 - n * num2
       n elements
```

並且{a, b, c, ...}範圍介於[0,60], 所以多項式最高位最多就到2^60 + ...
而且左邊為2的倍數相加，可看作二進位制11001010

所以:
1次operation: 2^a == num1 - 1 * num2, 此時左邊bit_count() 必須 <= 1
2次operation: 2^a+2^b == num1 - 2 * num2, 此時左邊bit_count() 必須 <= 2
...
n次operation: (num1-n*num2).bit_count()必須 <= n

所以就是n=1開始, 找出num1-num2*n 是不是可以表達成一連串2倍數的相加
其中:
定義 num = num1-n*num2

最低operations為num可以表達成一個二進位表達式
=> n >= num.bit_count()

最多operations為num表達成 2^0+2^0+...+2^0 = num * 1
=> n <= num
所以如果n能滿足 `num.bit_count() <= n <= num` 的話, n就是個合法操作數
所以我們可以由小到大遍歷n, 並且n最多到61

因為二進位多項式最高位為2^60, 所以最多操作數會發生在每一個二進位位置都為1的情況
2^60 + 2^59 + ... + 2^1+2^0
代表最多就61個elements, 所以我們遍歷n [0,61]這範圍找出第一個合法解即為答案