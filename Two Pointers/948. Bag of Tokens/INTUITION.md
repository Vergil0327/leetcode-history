# Intuition

可以任意選擇tokens[i]:
1. 如果power >= tokens[i] => power-tokens[i] and score += 1
2. 如果score >= 1 => power += tokens[i] and score -= 1

所以如果要轉power成分數的話, 肯定是選最小的tokens[i]
如果要轉分數為token的話, 肯定是選最大的tokens[i]

所以我們可以先對tokens排個序, 然後從兩邊用雙指針試試?

```
tokens = X X X X X X X X X X X X
         l                     r
```

每當移動左邊界`l`, 我們就能持續移動右邊界獲得tokens[r]
然後就又能持續移動左邊界`l`獲得分數, 持續repeat
greedily用分數獲得最多token並花費最少token獲得分數, 紀錄每一回合的分數找出全局最大

# Complexity

- time complexity: $O(nlogn)$
- space complexity: $O(1)$