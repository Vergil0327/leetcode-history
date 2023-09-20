# Intuition

首先就是循環小數跟非循環小數肯定是不相等的

所以如果兩者不同為循環小數或非循環小數, 我們直接返回False即可

再來就分兩類挑論:

1. 對於非循環小數的str來說, 我們可以直接`float(str)`然後兩者進行比對即可. 這樣可以簡化"1.0000"跟"1"這類型之間的比較
   - 這邊有個小地方要注意的是, **直接比較兩個float是否相等是很危險的**, 比較好的做法應該是要看他們之間的`abs(difference)`是否小於一個足夠小的數, ex. 1e-12

2. 對於循環小數的str來說, 我們把一個str分成`NonRepeatingPart`跟`RepeatingPart`

ex. 1.1234(999)
- NonRepeatingPart = 1.1234
- RepeatingPart = 999

再來要比較循環小數的話, 我們就把RepeatingPart延至足夠長, 然後比較兩者的prefix string即可
只要循環夠多次, 最終前面的prefix肯定是會相等的

ex. 
s = 1.1234(999) = "1.1234" + "999" + "999" + .....
t = 1.1234(9) = "1.1234" + "9" + "9" + .....

我們看直接看兩個string, s[:32] 跟 t[:32]有沒有相等即可


3. edge case for RepeatingPart:
    - 0.(9) == 1
    - 0.8(9) == 0.9
    - 0.001(9) == 0.002

    - 0.2(0) == 0.2
    - 1.(0) == 1.0 == 1

所以對於循環小數來說, 在額外判斷`RepeatingPart`是不是`(0)`或`(9)`即可
如果是, 那他其實是rational number, 我們處理完返回float(string)

- 如果`len(set(RepeatingPart)) == 1`而且裡面的值是"0", 那就返回float(NonRepeatingPart)
- 如果`len(set(RepeatingPart)) == 1`而且裡面的值是"9", 那就`NonRepeatingPart`最後一位數值+1, 再返回float(NonRepeatingPart).
  - 這邊注意"1.0(9)"跟"1.(9)"這個case, 如果NonRepeatingPart最後一位是"."那就是NonRepeatingPart[-2]的值+1, 不然就NonRepeatingPart[-1]+1

