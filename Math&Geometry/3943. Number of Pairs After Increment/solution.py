import math
from collections import Counter
from typing import List

class Solution:
    """
    在Square Decomposition中，我們把這 $20000$ 個數字每 $250$ 個切成一塊。遇到完整區塊加值：我們絕不去動內部的字典，而是把區塊的 lazy 變數加值，$O(1)$。
    遇到不完整區塊加值：我們只去動那零星的幾個數字，最多重新計算一個大小僅為 $250$ 的小字典，速度極快。
    """
    def numberOfPairs(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n2 = len(nums2)
        count1 = Counter(nums1)
        
        # 1. 動態計算最佳區塊大小 (Block Size)
        block_size = int(math.sqrt(n2)) if n2 > 0 else 1
        num_blocks = (n2 + block_size - 1) // block_size
        
        lazy = [0] * num_blocks
        blocks_counts = [Counter() for _ in range(num_blocks)]
        
        # 填入初始數據
        for i, val in enumerate(nums2):
            blocks_counts[i // block_size][val] += 1
            
        res = []
        
        # 2. 高效處理查詢
        for query in queries:
            if query[0] == 1:
                _, ql, qr, val = query
                
                start_block = ql // block_size
                end_block = qr // block_size
                
                if start_block == end_block:
                    b = start_block
                    # 局部暴力更新：快取該 Block 的 Counter 引用以加快速度
                    b_count = blocks_counts[b]
                    for i in range(ql, qr + 1):
                        old_val = nums2[i]
                        b_count[old_val] -= 1
                        # 提早清除頻率為 0 的 Key，防止 Dict 虛胖、維持查詢極速
                        if b_count[old_val] == 0:
                            del b_count[old_val]
                        nums2[i] += val
                        b_count[nums2[i]] += 1
                else:
                    # 處理左邊緣不完整區塊
                    b_start = blocks_counts[start_block]
                    for i in range(ql, (start_block + 1) * block_size):
                        old_val = nums2[i]
                        b_start[old_val] -= 1
                        if b_start[old_val] == 0:
                            del b_start[old_val]
                        nums2[i] += val
                        b_start[nums2[i]] += 1
                        
                    # 處理中間完整區塊 (超級 O(1) 核心)
                    for b in range(start_block + 1, end_block):
                        lazy[b] += val
                        
                    # 處理右邊緣不完整區塊
                    b_end = blocks_counts[end_block]
                    for i in range(end_block * block_size, qr + 1):
                        old_val = nums2[i]
                        b_end[old_val] -= 1
                        if b_end[old_val] == 0:
                            del b_end[old_val]
                        nums2[i] += val
                        b_end[nums2[i]] += 1
                        
            else:
                _, total = query
                ans = 0
                
                # 因為 len(nums1) <= 5，最外層迴圈次數極少
                for num1, freq1 in count1.items():
                    target = total - num1
                    
                    # 巡檢所有區塊，利用快取的 lazy 直接查表
                    for b in range(num_blocks):
                        orig_target = target - lazy[b]
                        # 字典使用 get 來防範 Key 遺失的開銷
                        ans += freq1 * blocks_counts[b].get(orig_target, 0)
                            
                res.append(ans)
                
        return res

# !!! TLE
# class SegmentTree:
#     def __init__(self, arr: List[int]):
#         self.n = len(arr)
#         self.arr = arr
#         # tree[tree_idx] 儲存該節點區間內，各數字的頻率 Counter
#         self.tree = [Counter() for _ in range(4 * self.n)]
#         # lazy[tree_idx] 儲存該節點的延遲加值
#         self.lazy = [0] * 4 * self.n
#         if self.n > 0:
#             self._build(0, 0, self.n - 1)

#     def _build(self, tree_idx: int, l: int, r: int):
#         """建立線段樹初始狀態"""
#         if l == r:
#             self.tree[tree_idx][self.arr[l]] = 1
#             return
#         mid = (l + r) // 2
#         left_idx = 2 * tree_idx + 1
#         right_idx = 2 * tree_idx + 2
        
#         self._build(left_idx, l, mid)
#         self._build(right_idx, mid + 1, r)
        
#         # 合併左右子節點的 Counter
#         self.tree[tree_idx] = self.tree[left_idx] + self.tree[right_idx]

#     def _push_down(self, tree_idx: int):
#         """將 Lazy 標記下傳給左右子節點，並更新子節點的 Counter 鍵值"""
#         if self.lazy[tree_idx] == 0:
#             return
            
#         val = self.lazy[tree_idx]
#         left_idx = 2 * tree_idx + 1
#         right_idx = 2 * tree_idx + 2
        
#         # 更新左子節點
#         self.lazy[left_idx] += val
#         self.tree[left_idx] = Counter({k + val: v for k, v in self.tree[left_idx].items()})
        
#         # 更新右子節點
#         self.lazy[right_idx] += val
#         self.tree[right_idx] = Counter({k + val: v for k, v in self.tree[right_idx].items()})
        
#         # 清空當前節點的 Lazy 標記
#         self.lazy[tree_idx] = 0

#     def update_range(self, tree_idx: int, l: int, r: int, ql: int, qr: int, val: int):
#         """區間更新：將 nums2[ql..qr] 每個元素都加上 val"""
#         if ql <= l and r <= qr:
#             self.lazy[tree_idx] += val
#             # 將當前節點 Counter 內的所有 Key 都加上 val
#             self.tree[tree_idx] = Counter({k + val: v for k, v in self.tree[tree_idx].items()})
#             return
            
#         self._push_down(tree_idx)
#         mid = (l + r) // 2
#         left_idx = 2 * tree_idx + 1
#         right_idx = 2 * tree_idx + 2
        
#         if ql <= mid:
#             self.update_range(left_idx, l, mid, ql, qr, val)
#         if qr > mid:
#             self.update_range(right_idx, mid + 1, r, ql, qr, val)
            
#         self.tree[tree_idx] = self.tree[left_idx] + self.tree[right_idx]

#     def query_val(self, tree_idx: int, l: int, r: int, ql: int, qr: int, target: int) -> int:
#         """區間查詢：查詢 nums2[ql..qr] 區間內有多少個元素等於 target"""
#         if ql <= l and r <= qr:
#             return self.tree[tree_idx].get(target, 0)
            
#         self._push_down(tree_idx)
#         mid = (l + r) // 2
#         left_idx = 2 * tree_idx + 1
#         right_idx = 2 * tree_idx + 2
        
#         res = 0
#         if ql <= mid:
#             res += self.query_val(left_idx, l, mid, ql, qr, target)
#         if qr > mid:
#             res += self.query_val(right_idx, mid + 1, r, ql, qr, target)
            
#         return res

# class Solution:
#     def numberOfPairs(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
#         n2 = len(nums2)
#         count1 = Counter(nums1)
        
#         # 初始化線段樹
#         st = SegmentTree(nums2)
#         res = []
        
#         for query in queries:
#             if query[0] == 1:
#                 _, x, y, val = query
#                 st.update_range(0, 0, n2 - 1, x, y, val)
#             else:
#                 _, total = query
#                 ans = 0
#                 # 枚舉 nums1 的去重組合（最多 5 個）
#                 for num1, freq1 in count1.items():
#                     target = total - num1
#                     # 查詢整個 nums2 區間 (0 到 n2-1) 中有多少個數字等於 target
#                     count_target = st.query_val(0, 0, n2 - 1, 0, n2 - 1, target)
#                     ans += freq1 * count_target
#                 res.append(ans)
                
#         return res