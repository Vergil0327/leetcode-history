class FenwickTree:
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def add(self, i: int, delta: int):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

class Solution:
    """
    ===================================================================
      Count Subarrays With Even Odd Ratio II - Core Logic & Thought
    ===================================================================

    【1. Mathematical Transformation】
    For a subarray with x even elements and y odd elements:
    Condition: y > 0 and x / y <= a / b

    Multiply both sides by y * b (since y > 0 and b > 0):
    => b * x <= a * y
    => b * x - a * y <= 0


    【2. Automatic Guarantee of y > 0】
    If a non-empty subarray contains ONLY even elements (y = 0, x > 0):
    The transformed sum is: b * x - a * 0 = b * x > 0 (since b >= 1, x >= 1).
    A purely even subarray can NEVER satisfy (transformed sum <= 0).
    Conclusion: Any subarray with (transformed sum <= 0) naturally guarantees y > 0.


    【3. Array Value Mapping】
    Transform the original array:
    - Even numbers  ->  +b
    - Odd numbers   ->  -a

    Now, the sum of any subarray nums[l...r] equals:
    b * x - a * y

    The problem reduces to:
    Find the number of subarrays with sum <= 0.


    【4. Prefix Sum & Fenwick Tree (BIT)】
    Define prefix sum array P, where P[0] = 0 and P[i] is prefix sum up to index i-1:
    Subarray sum nums[l...r] = P[r+1] - P[l] <= 0
    => P[l] >= P[r+1]

    Algorithm:
    1. Build transformed prefix sum array P of length N + 1.
    2. Coordinate compress (discretize) the unique values in P.
    3. Iterate through P from left to right:
        - Use a Fenwick Tree (BIT) to maintain frequencies of prefix sum values seen so far.
        - For current prefix sum P[j], count how many previous P[l] satisfy P[l] >= P[j].
        - Add this count to the answer.
        - Insert P[j] into the Fenwick Tree.


    【5. Complexity】
    - Time Complexity: O(N log N) for coordinate compression & Fenwick Tree operations.
    - Space Complexity: O(N) for prefix sums and BIT storage.
    """
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n = len(nums)
        
        # 1. 建立轉換後的前綴和陣列 P
        P = [0] * (n + 1)
        for i in range(n):
            val = b if nums[i] % 2 == 0 else -a
            P[i + 1] = P[i] + val

        # 2. 座標壓縮 (離散化)
        sorted_unique_P = sorted(list(set(P)))
        rank = {val: i + 1 for i, val in enumerate(sorted_unique_P)}
        
        # 3. 遍歷前綴和，使用 Fenwick Tree 統計滿足 P[l] >= P[r+1] 的數量
        bit = FenwickTree(len(sorted_unique_P))
        ans = 0
        
        # 放入初始狀態 P[0]
        bit.add(rank[P[0]], 1)
        
        for j in range(1, n + 1):
            curr_rank = rank[P[j]]
            
            # 目前 BIT 中已有 j 個前綴和
            # 嚴格小於 P[j] 的數量為 bit.query(curr_rank - 1)
            # 大於等於 P[j] 的數量即為 j - bit.query(curr_rank - 1)
            ge_count = j - bit.query(curr_rank - 1)
            ans += ge_count
            
            # 將當前 P[j] 加入 BIT
            bit.add(curr_rank, 1)
            
        return ans