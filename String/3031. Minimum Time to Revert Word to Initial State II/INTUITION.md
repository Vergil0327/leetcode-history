# Intuition

abacaba
aba | caba + bac
cab | abac + aba
abacaba

for i in range(k, n, k):
    word[i:] + ANY_SUFFIX

t=1, prefix = word[k:]
t=2, prefix = word[k*2:]
at time = t, prefix = word[k*t:]
一但prefix == word[:len(prefix)], 我們就能停止
如果一直都沒找到, 由於suffix可以任意組成, 最終也肯定能組成一開始的word
那這樣會是個O(n^2)

所以重點在於我們能不能快速在word裡找到一段word[k*t:] == word[:n-k*t]
=> 也就是找到一段prefix == suffix 且長度為k的倍數

那這樣肯定得先對word進行預處理, 好讓我們能在O(1)時間確認`word[k*t:] == word[:n-k*t]`

Z-function for a string returns an array z of the same size.
z[i] tells us how many characters, starting from the position i, match with the first characters of the string.

那這樣我們只要確認從position `k*t`開始`z[k*t]`有沒有至少`n-k*t`個letters即可, 有的話代表suffix word[k*t:]與prefix word[:n-k*t]相等