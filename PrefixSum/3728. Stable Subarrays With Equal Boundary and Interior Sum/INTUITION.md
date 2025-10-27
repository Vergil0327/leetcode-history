# Intuition

搜尋合法subarray => 想到prefix sum + hashmap

以1-indexed prefix sum為例:

條件是: capacity[i] = capacity[j] = (presum[i+1]-capacity[i]) - presum[j+1] = presum[i] - presum[j+1]
所以目標`presum[j+1] = presum[i] - capacity[i]`

由於要符合capacity[i] = capacity[j], 所以我們hashmap的target為`(capacity[i], presum[j+1]) = (capacity[i], presum[i] - capacity[i])`才能確保subarray sum符合的同時, 頭跟尾都是capacity[i]

再來由於`subarray length is at least 3`, 所以對於`i`來說, `i-2`位置才是合法開始位置
所以每次遍歷, `hashmap[(capacity[i-2], presum[(i-2)+1])] += 1`