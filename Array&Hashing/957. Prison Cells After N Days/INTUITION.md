# Intuition

看起來會是有規律地在變化, 並且由於cells.length == 8
所以我們用bitmask來表示當前cells的狀態並變化, 然後試著找出loop的大小來加速變化