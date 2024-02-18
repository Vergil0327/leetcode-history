# Intuition

arr1跟arr2數據量都頗大
一開始先想數字開頭就0-9, 我們可以先分門別類加到hashmap理

MAP1[arr1[i][0]] = [arr1[i], arr1[j], arr1[k], ...]
MAP2[arr2[i][0]] = [arr2[i], arr2[j], arr2[k], ...]

那同一組分門別類後, 發現在繼續比較下個字母是不是同個group
=> 那這其實不就是Trie ?

所以我們可以分別建立Trie of arr1 and arr2

然後我們再用DFS遍歷 "0123456789" 去找出longest common prefix即可