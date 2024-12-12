# Intuition

從後往前, 找到一個arr[i]並且arr[i+1:]存在一個arr[j]只剛好比arr[i]小一點, 但是是arr[i+1:]裡最大的數交換
如果arr[j]有複數個, 那就是跟由左往右遍歷的第一個交換