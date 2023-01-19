# Intuition

這題其實就是暴力搜索

我們有兩種方式:

1. 枚舉所有 n-digit的 n1 * n2 看是不是 palindrome
時間複雜度會是$O(n^2)$，而且由於我們要找的是最大palindromic integer

n1 * n2, (n1-1) * n2, n1 * (n2-1)，這類的細微差異所得到的乘積不好判斷是不是最大的palindrome

2. 從最大可能的palindrome開始枚舉，看能不能被因式分解

首先兩個n位數乘積會是個`2n`位數，由於palindrome前後相反，因此我們以`O(n)`時間由大到小枚舉所有可能，並加上自身翻轉即得`2n`位數的palindrome

```py
for num in range(upper_bound, lower_bound-1, -1):
    palindrome = str(num) + reversed(str(num))
    palindrome = int(palindrome)
```

再來我們在看他有沒有因數能分解即可，由於因數是兩兩乘積，因此找尋因數僅需要`O(sqrt(num))`的時間

所以總時間複雜度為 O(n * sqrt(n))，明顯比第一種的O(n^2)來得好

**Edge Case**

由於我們組成palindrome時是兩個n位數string組成，因此至少會是2位數的回文數

我們並沒有涵蓋到一位數的回文數，所有的一位數本身都是回文數，當中`9`是最大的

因此假如我們整個for-loop都沒找到答案的話，代表palindormic integer 落在個位數，那就最終返回`9`即可

# Approach

n位數的最小值為: $10^{n-1}$

n位數最大值為: n個9 也就是 $10^n$-1

- 從大到小產生回文數，並且判斷能不能被分解
- 由於我們要找的兩個數乘積，那兩個因數也必須是 n 位數，因此我們從 n位數的最大值往下枚舉到sqrt(palindromic integer)
