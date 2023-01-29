# Intuition

全部有$2^n$種可能，其中只有兩種是不會互撞的(全都順時針或全都反時針)
因此答案為 2^n - 2, 由於n到$10^9$
因此我們取 fast power with modulo: `pow(2, n, MOD)-2`
由於 `pow(2, n, MOD)-2` 可能為負數，因此`(pow(2, n, MOD)-2 + MOD)%MOD`