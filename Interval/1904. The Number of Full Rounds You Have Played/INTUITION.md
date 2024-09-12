# Intuition

換算成分鐘制來計算即可
- 找出離loginTime最近的下個棋局開始時間點
- 找出離logoutTime最近的棋局結束時間點
- 棋局開始與結束的時間點換算成分鐘制計算duration, 最後再除以一場棋局的時間, 15分, 即可

edge cases:
- 最後注意如果logoutTime早於loginTime, 代表有過夜, 棋局結束時間必須在加24 * 60分
- Note that if logoutTime and loginTime are in the same 15-minute round, the above returns -1
  - 所以我們取`max(0, ...)`