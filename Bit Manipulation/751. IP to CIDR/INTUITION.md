# Intuition

example 1: ip = "255.0.0.7", n = 10

255.0.0.7  -> 11111111 00000000 00000000 00000111

255.0.0.8  -> 11111111 00000000 00000000 00001000
255.0.0.9  -> 11111111 00000000 00000000 00001001
255.0.0.10 -> 11111111 00000000 00000000 00001010
255.0.0.11 -> 11111111 00000000 00000000 00001011
255.0.0.12 -> 11111111 00000000 00000000 00001100
255.0.0.13 -> 11111111 00000000 00000000 00001101
255.0.0.14 -> 11111111 00000000 00000000 00001110
255.0.0.15 -> 11111111 00000000 00000000 00001111

255.0.0.16 -> 11111111 00000000 00000000 00010000

首先觀察看最後一位1, 如果最後是`100`, 那麼他可以cover:
100
101
110
111

所以我們如果找到LSB (least significant bit) 並且 LSB <= n
那麼我們就能有個CIDR cover這四位

因此首先我們把ip轉換回32-bit value
```py
# ip to value: ip = 8-bit + 8-bit + 8-bit + 8-bit
x = 0
for v in ip.split("."):
    x = x*256 + int(v)
```

再來我們目標是找到CIDR剛好cover n個ip, i.e. [ip, ip+n-1]
所以根據前面所述, 我們先找到`LSB = x & -x`, LSB同時也代表他可以cover的ip數目

由於題目限制說我們必須包含剛剛好n個ip
所以當LSB = cover = `1000`, 如果 LSB = cover > n, 那麼我們就必須right-shift直到cover <= n
等到LSB = cover <= n, 代表這時CIDR = ip/32-cover 可以代表前`cover`個IP

所以接下來ip從ip+cover開始, 也就是:
`x += cover`
並且剩餘的ip數目剩下:
`n -= cover`
同時這時必須把現在的CIDR加入到res當中
`res.append(ipToCIDR(x, cover))`