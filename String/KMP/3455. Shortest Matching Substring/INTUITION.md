# Intuition

這題題目敘述給的思路很清晰

由於星號`"*"`確定有兩個, 代表可以將pattern分出3個part
那我們就用這三個part先找出所有substring occurence後
我們可以遍歷第一個合法occurence, 再透過binary search找出下個合法occurence位置
如果能找出所有合法substring occurence, 便更新minimum length

所以分兩個部分

1. substring occurence: 可以利用KMP algorithm
2. binary search
