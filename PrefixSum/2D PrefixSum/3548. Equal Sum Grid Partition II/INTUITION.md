# Intuition

基本上延續`3548. Equal Sum Grid Partition I`的思維, 從2D prefix sum出發
只是多了一個操作是可以從較大matrix sum那邊移除掉一個格子, 使得兩邊相同

但移除的這個格子有個限制, 那就是移除後的那個行列不可以是disconnected, 並且只能移除一個
那基本上代表這個格子只可能是該section的四個角落

我們就判斷四個角落是不是我們所需要移除的數即可