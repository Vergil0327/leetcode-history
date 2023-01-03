# Intuition

這題如果另外儲存一個**O(mn)**的空間的話就遍歷一遍取得新的Game of Life，然後再遍歷一遍更新即可

但若要用**O(1)**空間的話，就必須稍微觀察一下了

由於Game of Life中每一格不是`0`就是`1`，因此正好可以用二進位來表示，
再加上如果要用**O(1)**空間的話，代表每一格必須同時儲存更新前後的資訊
因此我們用2個bit來分別表示更新前後:

Two Bit: **[next state, current state]**

因此會產生四種情況

- 原本為0
  1. 0 -> 00
  2. 0 -> 01, 當周遭live正好為3
- 原本為1
  1. 1 -> 11, 周遭live等於2或3
  2. 1 -> 01, 之外的情況

因此當我們在考慮每個`board[i][j]`的周遭8格時, 可以用`board[i'][j']&1`來取的原本的state來判斷原本state為`0`或`1`

也就是當`board[i'][j']&1==1`時，代表原本的state為1
而當`board[i'][j']&1==0`時，代表原本的state為0

當我們判斷並更新完每一格後，再遍歷一次並透過`board[i][j] <<= 1`即可更新state

# Complexity

- time complexity

$$O(mn)$$

- space complexity

$$O(1)$$

# Further

但其實也可以不需要用到Bit Manipulation，僅需而外兩個變數儲存即可

因為只會從 `1 -> dead`, `0 -> live`
因此用另外兩個`0`, `1`之外的變數代表這兩種情況，一樣可反推回去原本的狀態

```
class Solution {
    private int die = 2;
    private int live = 3;
    public void gameOfLife(int[][] board) {
        // we only flip the 1 to die and 0 to live
        // so when we find a die around, it must be a previous 1
        // then we can count the 1s without being affected
        int rows = board.length;
        int cols = board[0].length;
        for (int i=0;i<rows;i++){
            for (int j=0;j<cols;j++){
                int around = countLive(i,j,board);
                if (board[i][j] == 0 && around == 3)
                    board[i][j] = live;
                else if (board[i][j] == 1){
                    if (around == 2 || around ==3)
                        continue;
                    if (around < 2 || around > 3)
                        board[i][j] = die;
                }
            }
        }
        
          for (int i=0;i<rows;i++){
            for (int j=0;j<cols;j++){
                 if (board[i][j] == die)
                     board[i][j] = 0;
                 if (board[i][j] == live)
                     board[i][j] = 1;
                }
            }
        
    }
    
    private int countLive(int i, int j,int[][] board){
        int count = 0;
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1}};
        
        for (int[] dir:dirs){
            int x = i+dir[0];
            int y = j+dir[1];
            
            if (x>=0 && y>=0 && x < board.length && y<board[0].length ){
                
                if (board[x][y] == 1 || board[x][y] == die)
                    count ++;
            }
        }
        
        return count;
        
    }
}
```