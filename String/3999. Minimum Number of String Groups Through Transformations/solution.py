"""
核心思維

獨立性分解：
根據題目定義，偶數索引子序列 $E$ 與奇數索引子序列 $O$ 可以獨立進行任意次數的右移循環旋轉。因此，兩個字串等價的充要條件是：
- 它們的 $E$ 子序列互為循環移位(Cyclic Shift)。
- 它們的 $O$ 子序列互為循環移位。

規範化代表元（Canonical Representative）：
為了判定兩個字串是否屬於同一組，我們只需要為每個子序列求出其字典序最小的循環旋轉(Lexicographically Smallest Cyclic Rotation)：
- 將 $E$ 轉為其字典序最小的循環旋轉 $E_{min}$。
- 將 $O$ 轉為其字典序最小的循環旋轉 $O_{min}$。
- 這對元組 $(E_{min}, O_{min})$ 即為該字串的唯一特徵簽名（Signature）。

Duval / 雙指標極速演算法：
求長度為 $N$ 的字串之字典序最小循環旋轉，若使用暴搜需要 $O(N^2)$。使用 Duval 雙指標算法可以在 $O(N)$ 時間與 $O(N)$ 空間內求出答案。

統計不重覆簽名數：
將所有字串轉換為特徵簽名，將簽名存入集合 set 中，集合的大小即為最小分組數。
"""
class Solution:
    def minimumGroups(self, words: list[str]) -> int:
        def get_min_cyclic_rotation(s: str) -> str:
            n = len(s)
            if n <= 1: return s
            
            # Duval 雙指標演算法求字典序最小的循環旋轉
            s_dup = s + s
            i, j, k = 0, 1, 0
            
            while i < n and j < n and k < n:
                if s_dup[i + k] == s_dup[j + k]:
                    k += 1
                else:
                    if s_dup[i + k] > s_dup[j + k]:
                        i += k + 1
                    else:
                        j += k + 1
                    if i == j:
                        j += 1
                    k = 0
                    
            start = min(i, j)
            return s_dup[start:start + n]

        signatures = set()
        
        for w in words:
            # 提取偶數索引與奇數索引子序列
            even_subseq = w[::2]
            odd_subseq = w[1::2]
            
            # 分別求出最小循環旋轉
            min_e = get_min_cyclic_rotation(even_subseq)
            min_o = get_min_cyclic_rotation(odd_subseq)
            
            # 將特徵簽名存入集合
            signatures.add((min_e, min_o))
            
        return len(signatures)