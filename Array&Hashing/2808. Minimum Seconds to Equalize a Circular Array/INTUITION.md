# Intuition

```
nums = X X num X X X X num X X X num X X num X X
```

對於num來說, 他可以將i-1跟i+1位置的X轉換成num
所以對於任意兩個num所形成的區間:
`[num X X X X X X X X X X num]`
要將他們中間的X轉換成num所需的秒數為ceil(中間X個數/2)

所以對於num來說, 要讓全部nums都轉換成num的話
那就是從每個由num所形成的區間中, 找出所需時間最久的那個區間的秒數, 也就是:
`max(ceil(中間X個數/2) for every interval where left-most and right-most element is num)`
*note. 另外別忘記這是個環形array, 最後一個num作為左端點, 第一個num作為右端點也是一個區間*

最後再遍歷每個可能num作為final value, 找出全局最小的所需秒數即為答案
        