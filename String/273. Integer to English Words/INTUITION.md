# Intuition

英文是每三位數一個level, ex. "Thousand", "Million", "Billion"
因此我們把`num`轉為string後，從個位數開始從後往前每三個數分成一組來處理.(分成數個chunks)

再依照chunks的size來個別處理

1. size = 3
每個數個字mapping到百位, 十位, 個位數

2. size = 2
每個數個字mapping到十位, 個位數

3. size = 1
每個數個字mapping到十位, 個位數

這其中要注意的Special Case是:
`當十位數是1時，有獨自一套規則結尾為 XXX-teen`

等到全部mapping完後，再對每個chunks依序加上"Thousand", "Million", "Billion"等分隔即可