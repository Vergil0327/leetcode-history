# Intuition

用`stack`模擬整個過程, 並同時紀錄每次放入新的callstack時的當前時間去計算每次的interval

- 如果當前tag是"start", 那麼只是起始時間改變
  - 區間為: timestamp - current_t 
  - current_t = timestamp
- 如果當前tag是"end", 那麼是整段時間都是區間
  - 區間為: timestamp - current_t + 1
  - current_t = timestamp + 1