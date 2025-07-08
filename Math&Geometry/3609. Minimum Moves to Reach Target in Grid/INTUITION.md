# Intuition

從起點出發有多種可能:

start = (sx, sy)

-> (sx+max(sx, sy), y) -> (sx+max(sx, sy) + max(sx+max(sx, sy), y), y)
                       -> (sx+max(sx, sy), y + max(sx+max(sx, sy), y))

-> (sx, y+max(sx, sy)) -> ...
                       -> ...


但逆向思考, 反過來從(tx, ty)回到(sx, sy)的話, 只會有一條路


(tx, ty) -> (x+max(x,y), y) or (x, y+max(x,y)) 乍看有兩種選擇, 但由於x, y, max(x,y)都為正數, 所以必定越加越大
那麼也就是說:

- if tx > ty: (tx, ty), then it's from (x+max(x,y), y)
    - 再來分情況討論max(x,y):
        1. if max(x,y) = x --> x >= y and tx = 2x --> x = tx/2, and ty = y, also means tx%2 == 0 --> 同時也必須符合x >= y, 所以tx/2 >= y
            - 因此, if tx%2==0 and tx >= 2*ty: 1 + minMoves(sx, sy, tx//2, ty)
        2. if max(x,y) = y --> x <= y --> (x=tx-ty, y=ty)
            - 1 + minMoves(sx, sy, tx-ty, ty)
        
- if tx < ty: return minMoves(sy, sx, ty, tx)  -->由於操作上完全對稱, 所以在這條件下把(sx,sy), (tx,ty)對調不影響結果

- if tx == ty: (x,y) = (x,x) --> 這時判斷不出來所以兩種情況都討論
    1. x = x + max(x,x), x=y --> x=0, y=x
        - return 1 + minMoves(sx, sy, 0, tx)
    2. x=y, y=y+max(x,y) --> y=0, x=y
        - return 1 + minMoves(sx, sy, tx, 0)


並且由於Constraints:
- 0 <= sx <= tx <= 10^9
- 0 <= sy <= ty <= 10^9

所以回頭走時, 必定越走越小, 且不會是負數, 一但越過邊界變成負數, 代表此路不通 => 所以這可以作為邊界條件`if sx>tx or sy>ty: return -1`

再來就是成功抵達的狀況: `if sx==tx and sy==ty: return 0`

推薦[影片詳解](https://www.youtube.com/watch?v=rdhWlz01oyE&ab_channel=HuifengGuan)