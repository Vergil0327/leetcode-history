"""
===================================================================
      Minimum Possible Maximum Waiting Time - Thought Process
===================================================================

【1. Key Invariants & Problem Observations】

1. Sequential Processing (Prefix Property):
   - Cars are allowed in strict index order: 0, 1, 2, ...
   - Refueling terminates as soon as a car cannot be served.
   - Therefore, any valid sequence of K served cars MUST be the exact prefix 
     demand[0 ... K-1]. We never skip cars.

2. Total Fuel Invariant:
   - At step i (before processing car i), the total remaining fuel across
     both dispensers is fixed:
       C_i = (fuel[0] + fuel[1]) - sum(demand[0 ... i-1])
   - Thus, if dispenser 0 has fuel `f0`, dispenser 1 MUST have fuel:
       f1 = C_i - f0
   - `f1` is not an independent state variable; it is uniquely determined by `f0`.

3. Bounded Busy Times:
   - When a car with demand `d` starts refueling at a dispenser, that dispenser 
     becomes busy for `d` seconds.
   - Since demand[i] <= 20, the remaining busy time of any dispenser at the 
     moment a new car becomes allowed is ALWAYS at most 20 (i.e., t0, t1 <= 20).


【2. Dynamic Programming State Design】

For step `i` (considering car `i` with demand `d = demand[i]`):
  State tuple: (f0, t0, t1)
    - f0: Remaining fuel in dispenser 0 (0 <= f0 <= fuel[0] <= 50).
    - t0: Remaining busy time of dispenser 0 (0 <= t0 <= 20).
    - t1: Remaining busy time of dispenser 1 (0 <= t1 <= 20).

  Stored Value: min_max_wait
    - The minimum possible value of the maximum waiting time encountered 
      among all served cars 0 ... i-1 to reach this state.

  State Space Upper Bound:
    - f0: 51 possible values
    - t0: 21 possible values
    - t1: 21 possible values
    - Max states per step = 51 * 21 * 21 = 22,491 (in practice, far fewer).


【3. State Transitions for Car i】

For a state `(f0, t0, t1)` with current maximum wait `max_w`:
Calculate `f1 = C_i - f0`.

Option A: Assign Car i to Dispenser 0 (Valid if f0 >= d)
  - Waiting time for car i: wait = t0
  - Car i starts refueling at time `t0` (which is when car i+1 becomes allowed).
  - Dispenser 0 busy time becomes `d`.
  - Dispenser 1 busy time decreases by `t0` (floored at 0): max(0, t1 - t0).
  - Next state: (f0 - d, d, max(0, t1 - t0))
  - Next max_w: max(max_w, t0)

Option B: Assign Car i to Dispenser 1 (Valid if f1 >= d)
  - Waiting time for car i: wait = t1
  - Car i starts refueling at time `t1` (when car i+1 becomes allowed).
  - Dispenser 1 busy time becomes `d`.
  - Dispenser 0 busy time decreases by `t1` (floored at 0): max(0, t0 - t1).
  - Next state: (f0, max(0, t0 - t1), d)
  - Next max_w: max(max_w, t1)


【4. Algorithm Outline】

1. Initialize `dp = {(fuel[0], 0, 0): 0}`.
2. Initialize `curr_fuel_sum = fuel[0] + fuel[1]`.
3. For i from 0 to N-1:
     Set `d = demand[i]`.
     Build `next_dp = {}`.
     For each `(f0, t0, t1), max_w` in `dp`:
       Compute `f1 = curr_fuel_sum - f0`.
       Try Option A (Dispenser 0 if f0 >= d) -> update `next_dp`.
       Try Option B (Dispenser 1 if f1 >= d) -> update `next_dp`.
     If `next_dp` is empty:
       Break loop (cannot serve car i).
     Else:
       `dp = next_dp`
       `curr_fuel_sum -= d`
4. If no cars were served (i == 0 and `next_dp` was empty):
     Return -1.
5. Otherwise:
     Return min(dp.values()).


【5. Complexity Analysis】

- Time Complexity: O(N * max_f0 * max_t0 * max_t1)
  With N <= 50, max_f0 <= 50, max_t <= 20:
  Total operations <= 50 * 22,491 * 2 ≈ 2.25 * 10^6, executing in < 0.1s.
- Space Complexity: O(max_f0 * max_t0 * max_t1)
  At most ~22,491 states stored per DP iteration.
"""
class Solution:
    def minMaxWaitingTime(self, demand: list[int], fuel: list[int]) -> int:
        # dp 記錄 (f0, t0, t1) -> 當前狀態下的最小「最大等待時間」
        # f0: 加油機 0 的剩餘油量
        # t0: 當當前車輛被允許加油時，加油機 0 剩餘的繁忙時間
        # t1: 當當前車輛被允許加油時，加油機 1 剩餘的繁忙時間
        dp = {(fuel[0], 0, 0): 0}
        curr_fuel_sum = fuel[0] + fuel[1]
        
        max_cars_served = 0
        
        for d in demand:
            next_dp = {}
            
            for (f0, t0, t1), max_w in dp.items():
                f1 = curr_fuel_sum - f0  # 依據油量守恆算出加油機 1 的剩餘油量
                
                # 選項 A：使用加油機 0
                if f0 >= d:
                    wait = t0
                    new_f0 = f0 - d
                    new_t0 = d
                    new_t1 = max(0, t1 - t0)  # 車輛 0 開始時（經過 t0 秒），加油機 1 也消磨了 t0 秒
                    new_max_w = max(max_w, wait)
                    
                    state0 = (new_f0, new_t0, new_t1)
                    if state0 not in next_dp or new_max_w < next_dp[state0]:
                        next_dp[state0] = new_max_w
                
                # 選項 B：使用加油機 1
                if f1 >= d:
                    wait = t1
                    new_f0 = f0
                    new_t0 = max(0, t0 - t1)  # 車輛 1 開始時（經過 t1 秒），加油機 0 也消磨了 t1 秒
                    new_t1 = d
                    new_max_w = max(max_w, wait)
                    
                    state1 = (new_f0, new_t0, new_t1)
                    if state1 not in next_dp or new_max_w < next_dp[state1]:
                        next_dp[state1] = new_max_w
            
            # 如果沒有任何狀態可以服務這台車，說明無法繼續服務更多車輛
            if not next_dp:
                break
                
            dp = next_dp
            curr_fuel_sum -= d
            max_cars_served += 1
            
        # 若連一台車都無法服務，回傳 -1
        if max_cars_served == 0:
            return -1
            
        # 在服務最多車輛的前提下，找到最小的最大等待時間
        return min(dp.values())