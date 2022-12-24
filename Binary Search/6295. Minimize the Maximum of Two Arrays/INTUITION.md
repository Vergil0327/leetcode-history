# Binary Search

## Intuition

我們能加入到`arr1`或`arr2`的只有數字不能被`divisor1`或`divisor2`整除的數
代表`1`到`n`裡, 我們必須扣除掉**最小公倍數(LCM)及其倍數**，因為公倍數不能加入到任一arr中

而`1`到`n`裡:
- 能加入到`arr1`的數有 `n//divisor1` 這麼多個
- 能加入到`arr2`的數有 `n//divisor2` 這麼多個

由於能放入`arr1`與`arr2`的數是隨著`n`增加而增加的，單調遞增的性質代表我們可以使用`binary search`來找出極值

我們的目標就是要找到一個最小的`n`來滿足:
- 加入到`arr1`, `arr2`的數必須不能分別被`divisor1`, `divisor2`整除
  - 代表`n`扣掉LCM及其倍數後須**大於等於**`uniqueCnt1+uniqueCnt2`
  - `n-n//LCM >= uniqueCnt1+uniqueCnt2`
- 並且`len(arr1)==uniqueCnt1` 且 `len(arr2)==uniqueCnt2`

透過 `n-n//LCM >= uniqueCnt1+uniqueCnt2` 確保足夠數量分給`arr1`與`arr2`
再透過 `n-n//divisor1 >= uniqueCnt1` 及 `n-n//divisor2 >= uniqueCnt2`共三個條件
即可透過**binary search**找出最小的n (也就是找出upperbound)