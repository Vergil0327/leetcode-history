# Intuition

題意看起來主要目的是找出k個合法interval

1. 找出每個character的最小/最大index, 來定義出interval. interval = [minIdx, maxIdx, ch]
2. 再來, 我們需要判斷intervals是否足夠cover k個interval
 
但首先, 對於a-z開頭的interval, 我們必須判斷區間內是否有包含其他字母, 如果有可能會需要merge, 例如:

1. a ...b a .. b => 實際上合法substring為 [a ... b]
2. 但如果反過來是: b ... a b ... a => 那麼就變成[b ... a], 代表不存在a開頭的substring了

所以首先我們可以先遍歷a-z把該merge的interval全給merge起來, 形成self-contained substring (substring包含所有出現的字母)
那麼在有了所有合法interval後, 剩下的就是找出最多的non-overlapped interval個數
那就是對**右端點**排序, 找出最多的不重疊區間個數 (greedy algorithm)即可
