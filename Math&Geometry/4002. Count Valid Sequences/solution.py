class Solution:
    """
    我們可以用排容原理（全部可能組合 - 乘積為奇數的組合）在 $O(n)$ 時間內解決：
    1. 全部可能的序列數量
        將 $n$ 分拆成 $k$ 個正整數的總方法數，即為經典的隔板法（Stars and Bars）：
            $$\text{Total} = \binom{n-1}{k-1}$$

    2. 乘積為「奇數」的序列數量
        乘積為奇數的充要條件是：序列中的每一個數都是奇數。
        設每個數字為 $a_i = 2x_i + 1$（其中 $x_i \ge 0$ 為非負整數）：
            $$\sum_{i=1}^k (2x_i + 1) = n \implies 2 \sum_{i=1}^k x_i + k = n \implies \sum_{i=1}^k x_i = \frac{n - k}{2}$$
        
        - 若 $n - k$ 為奇數或 $n < k$，不可能所有數都是奇數，此時奇數乘積組合數為 $0$。
        - 若 $n - k$ 為非負偶數，令 $S = \frac{n - k}{2}$，求非負整數解個數（非負隔板法）：
            $$\text{Odd} = \binom{S + k - 1}{k - 1}$$

    3. 乘積為「偶數」的序列數量
        $$\text{Answer} = (\text{Total} - \text{Odd}) \bmod (10^9 + 7)$$
    """
    def countValidSequences(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # 預計算階乘與逆元以支援快速 O(1) 組合數計算
        fact = [1] * (n + 1)
        inv = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = (fact[i - 1] * i) % MOD

        inv[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            inv[i] = (inv[i + 1] * (i + 1)) % MOD

        def nCr(N: int, R: int) -> int:
            if R < 0 or R > N:
                return 0
            return fact[N] * inv[R] % MOD * inv[N - R] % MOD

        # 1. 計算所有總和為 n 的 k 個正整數組合數
        total = nCr(n - 1, k - 1)

        # 2. 計算乘積全為奇數的組合數
        odd_seqs = 0
        if (n - k) % 2 == 0 and n >= k:
            S = (n - k) // 2
            odd_seqs = nCr(S + k - 1, k - 1)

        # 3. 至少有一個偶數 (乘積為偶數) = 全部 - 全奇數
        return (total - odd_seqs + MOD) % MOD