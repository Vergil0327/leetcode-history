# Intuition

分別對`x`, `y`排序, 然後**以平行x軸為底**以及**以平行y軸為底**
找出最左及最右的頂點位置
如此一來便能計算: area = base * height

其中base可以透過雙指針找出相同x(或y)的所有coords[i]並計算出來
而height則是找出最左最右頂點後即可計算出來, 透過右往左遍歷, 我們可以提前處理maxRight[i], minRight[i]

如此一來在由左往右遍歷同時, 我們在維護好`minLeft`以及`minRight`兩個變數
即可找出coords[i:j]這段相同x(或y)的區間的最左及最右頂點, 並計算出height

