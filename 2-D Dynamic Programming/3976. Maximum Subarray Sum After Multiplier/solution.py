class Solution:
    """
    這道題可以使用修訂版的 Kadane 演算法（動態規劃） 來解決。

    由於我們必須選擇恰好一個子陣列進行乘法或除法操作，且計算總和的子陣列可以與操作的子陣列不同，我們可以將每個位置的狀態拆解為 4 種不同的階段：

    狀態 0 (dp[0])：目前子陣列尚未開始任何乘除操作。

    狀態 1 (dp[1])：目前子陣列正在進行乘大 (* k) 操作。

    狀態 2 (dp[2])：目前子陣列正在進行除小 (/ k) 操作。

    狀態 3 (dp[3])：乘除操作已經結束，目前子陣列繼續向後延伸（不進行任何變更）。

    在 Python 中，題目要求的「正數向下取整、負數向上取整」的除法行為，正好等價於向零截斷的 int(x / k) 運算。
    """

    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        # 初始化第一項的各種狀態
        val_mult = nums[0] * k
        val_div = int(nums[0] / k)  # Python 的 int(/) 自動向零截斷（正數 floor，負數 ceil）
        
        # dp[0]: 尚未操作, dp[1]: 正在乘, dp[2]: 正在除, dp[3]: 操作已結束
        dp = [nums[0], val_mult, val_div, float('-inf')]
        ans = max(dp)
        
        for i in range(1, len(nums)):
            x = nums[i]
            v_mult = x * k
            v_div = int(x / k)
            
            next_dp = [0] * 4
            
            # 狀態 0：可以自己獨立開頭，或者延續前一個未操作的狀態
            next_dp[0] = max(x, dp[0] + x)
            
            # 狀態 1：可以此時開始乘（自己開頭或從 dp[0] 接續），或者延續前一個正在乘的狀態
            next_dp[1] = max(v_mult, dp[0] + v_mult, dp[1] + v_mult)
            
            # 狀態 2：可以此時開始除（自己開頭或從 dp[0] 接續），或者延續前一個正在除的狀態
            next_dp[2] = max(v_div, dp[0] + v_div, dp[2] + v_div)
            
            # 狀態 3：操作必須在這一任之前結束（從 dp[1] 或 dp[2] 轉移而來），或延續已結束的狀態
            next_dp[3] = max(dp[1] + x, dp[2] + x, dp[3] + x)
            
            # 滾動更新狀態與全域最大值
            dp = next_dp
            ans = max(ans, max(dp))
            
        return ans