# Intuition

以中心點做鏡像讓後半部對稱前半部即可得到smaller palindrome or greater palindrome其中之一
ex. 12345 => 12321 (smaller palindrome) => 他的greater palindrome為12421
ex. 931 => 939 (greater palindrome) => 他的smaller palindrome為929

而答案就是兩者之中, 離**n**最近的那個palindrome

由於後半部的palindrome鏡像於前半部, 所以我們如果直接讓後半部對前半部做鏡像後
如果得到的是greater palindrome, 那就讓前半部的prefix palindrome `-= 1`即可
ex. 931 => 939 => 將prefix "93" - 1變為"92"得到929

反之如果得到的是smaller palindrome, 那就讓前半部的prefix palindrome `+= 1`即可
ex. 12345 => 12321 => 讓prefix "123" += 1變為 12421即可得到greater palindrome

##edge case
但要注意`+= 1`, `-= 1`操作可能會讓數字進位或退一位

如果原本是"99", 然後要找greater palindrome => 會進位成"100", 此時的greater palindrome其實就是"10001"或"100001"
所以就是進位後的字串長度全補為0, 然後首尾改為1
ex. 999XX => 1000XX => 要比999XX更大一點的palindrome其實就是 100001

反之如果原本是"100", 那`-= 1`後會變成"99", 此時的smaller palindrome其實就是退位後的位數全部補"9"
ex. 100XX => 99XX => 9999是smaller palindrome
