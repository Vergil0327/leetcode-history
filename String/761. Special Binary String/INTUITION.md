# Intuition

s = 1 XXXXXXX 0
目的是盡可能找到相鄰special binary string交換成lexicographically largest
s自身肯定是由多個special substring組合而成, 我們目的就是找出這些substring
其中special string必定是1開頭0結尾 (因為兩邊個數要一樣並且prefix的1要至少有跟0一樣的個數)
所以我們每找到一個special string, 就再從special_string[1:-1]裡找出有沒有special substring
由於我們要lexicographically largest, 所以我們就將這些special substring由大到小排序
最後在遞歸地組成最終string即可

1. split s into many special substring (greedily)
2. 由於必定是1開頭0結尾, 就再從中間部分找出special substring
3. 依照字典順序由的到小排列
4. 組回最終result string