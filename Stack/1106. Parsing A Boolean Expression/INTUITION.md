# Intuition

這題跟拆括號進行四則運算很像

他會是個遞歸運算, 同時也代表可以用stack來模擬
首先先判斷出什麼時候:
- 將手邊的工作append stack
- 以及什麼時候pop stack

1. 首先先找到append stack的時機:
這題可以發現當遇到運算符`&`, `|`, `!`時我們要把括號內的(v1,v2,v3,....)加入到stack裡
然後再進行一個新的運算

2. 再來在找出pop stack的時機
這邊唯一要pop stack的時機就是當遇到")"的時候
所以每當遇到")"時, 我們要:
- 處理手上的values
- 將當前結果append到前一個stack
- pop 當前stack, 然後繼續處理