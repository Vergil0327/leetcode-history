# Intuition

為了滿足`nums[i]&nums[i+1]&nums[i+2]&...&nums[j] == k`

首先想到的是AND這操作只會讓值越來越小(單調遞減)
也就是對於subarray nums[i:j]來說, 隨著j=i開始往右, AND(subarray[i:j])只會愈來越小

> 每次進行AND, 各個bit上的1只會是不變或是減少
> 所以在值域上來看, 最多不超過30種變化 (因為nums[i], k <= 10^9 < 2^30)

所以對於一個nums[i]來說, 我們去看nums[i:j], 隨著j往右進行AND, bit上的1越來越少
最多就30種bit value, 因此我們可以用個hashmap將這些subarray nums[i:j]的值記錄下來

所以我們可以遍歷i, 範圍[0, n-1]
遍歷過程中持續更新紀錄hashmap與nums[i]進行AND的值, 最多不超過30種 (AND值會是個常數, hashmap.size並非n)
那這些值就相當於nums[0:i]為止的所有可能AND(subarray)的值
有了這些紀錄後, 我們就能直接從hashmap裡找出hashmap[k]的次數有多少即可, 這個hashmap[k]就是以nums[i]為結尾能貢獻的合法subarray

hashmap紀錄的就是到目前為止的所有可能{AND(subarray): frequency}