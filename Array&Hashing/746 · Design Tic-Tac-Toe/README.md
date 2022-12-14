[746 · Design Tic-Tac-Toe](https://www.lintcode.com/problem/design-tic-tac-toe/description)

`Hard`

Description
Design `Tic-Tac-Toe` game that is played between two players on a n x n grid

You may assume the following rules:

  - A move is guaranteed to be valid and is placed on an empty block
  - Once a winning condition is reached, no more moves is allowed
  - A player who succeeds in placing n of their marks in a horizontal, vertical or diagonal row wins the game


```
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

toe = NewTicTacToe(3)
toe.move (0,0,1) -> Return false (no one wins)
X| | |
 | | |
 | | |

toe.move (0,2,2) -> Return false
X| |O|
 | | |
 | | |
```