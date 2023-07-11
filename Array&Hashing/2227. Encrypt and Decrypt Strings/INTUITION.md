# Intuition

想法是預先encrypt dictionary並計數, 這樣就能用O(1)時間找出decrypt(word2)
至於encrypt, 我們就用個hashmap來繼續key-value pair並轉換即可
其中題目說如果該字符沒辦法encrypt的話就, encrypt成""

但看這個case: [[["b"],["ca"],["aaa","cacbc","bbaba","bb"]],["bbb"],["cacaca"]]
bbaba -> cacaca
cacaca -> bbb 但bbb不在dictionary裡

所以為了讓decrypt(word2)的可能結果是出現在dictironary的, 我們的encrypt分成兩步驟
其中第一步是將所有不在key-value pair的字符encrypt成"$", "$"代表一個placeholder
我們將此function定義成`self._encrypt`

這樣我們就能預先處理所有dictionary並`_encrypt(dictionary[i])`成獨特的encryption string
這樣就能在decrypt以O(1)時間求出

至於encrypt就要將_encrypt(word1)的結果移除所有placeholder即可