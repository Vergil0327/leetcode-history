"""
班次處理邏輯：
對於每個班次的時間 shift_time，我們先將其累加至 cur_work：

- 狀況 A：
    - cur_work >= S（所有任務皆已完成）所有任務全部完成，未完成的任務數為 0。
    - 依據題目規則「Discard & Restart」，該班次剩餘時間捨棄，下一個班次重新從任務 0 開始，因此將 cur_work 重置為 0。
- 狀況 B：
    - cur_work < S（任務尚未全數完成）使用二分搜尋 bisect_right(pref, cur_work)，快速找出當前已有多少個任務已被完全完成（記為 $c$ 個）。
    - 未完成的任務數即為 $N - c$（包含了進行中與尚未開始的任務）。
    - cur_work 保持現狀，接續到下一個班次。
"""
class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        pref = list(accumulate(tasks))
        total_time = pref[-1]
        n = len(tasks)
        
        ans = []
        cur_work = 0
        for shift_time in shifts:
            cur_work += shift_time
            
            if cur_work >= total_time:
                # 所有任務皆完成，重置進度
                ans.append(0)
                cur_work = 0
            else:
                # 使用二分搜尋找出已完全完成的任務數量
                completed = bisect_right(pref, cur_work)
                ans.append(n - completed)
                
        return ans