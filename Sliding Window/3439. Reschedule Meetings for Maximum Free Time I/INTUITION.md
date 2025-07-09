# Intuition

`meetings`頭尾加上起點與終點時間`0`, `eventTime`後把所有間隔時間找出來
我們要找的就是連續**k+1**個間隔的最大長度(自身一段時間, 加上k次挪用來的時間)
用sliding window去找即可