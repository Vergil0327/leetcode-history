# Intuition

```
ex.1 nums=[3,2,4,6] => to binary:

nums = [011,
        010,
        100,
        110,]
```

要達到maximum possible bitwise XOR => 每個bit位上都必須是奇數
既然我們能任意 nums[i] & (nums[i] XOR x)
代表每個bit都能任意調整到奇數個
所以我們就看有哪些bit有值即可 => 亦即我們將每個bit都 OR 在一起即可
=> 所以也就是將整個nums都OR在一起