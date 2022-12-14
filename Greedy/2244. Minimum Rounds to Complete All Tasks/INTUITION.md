# Intuition

我們一次可以拿`2`個或`3`個
若要達到最少次數，那肯定是盡量能3個3個拿最好

拿到最後勢必只會剩3種情況
- 全拿完
- 餘1
- 餘2

仔細觀察可發現
- 如果餘2的話，就再多一次拿兩個的操作
- 如果餘1的話，代表只要上一次操作改拿2個，那麼這次最後就會剩下2個。也一樣只要再多一次拿兩個的操作即可。
  - 這是因為3 mod 2 = 1，代表如果最後一次3個拿到最後如果餘1的話，可以將上一個`拿3個的操作`改為拿兩個，這樣就會有兩個`餘為1`的操作。最後只要再一次把兩個拿走即可
所以仔細觀察可以發現，除了一開始數就只有`1個`的情況外，所有的數都可以透過:
  1. 剛好是3的倍數 一次拿完
  2. 一次三個拿到最後，餘2，再多一次`拿兩個`
  3. 一次三個拿到最後，餘1，上個操作改為拿兩個，最後一樣再多一次`拿兩個`即可
因此，最佳解為:
  - 如果一開始數只出現一次，那無解，直接返回`-1`
  - 其他情況，都只要拿`ceil(cnt/3)`即可
    - ex. 444，出現`3`次，最佳解是拿 3 = ceil(3/3) = 1
    - ex. 4444，出現`4`次，最佳解是拿 2+2 = ceil(4/3) = 2
    - ex. 44444，出現`5`次，最佳解是拿 3+2 = ceil(5/3) = 2

# Complexity

- time complexity

$$O(n)$$

- space complexity

$$O(1)$$