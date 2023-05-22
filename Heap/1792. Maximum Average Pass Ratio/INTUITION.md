# Intuition - Greedy

一開始想到說用max heap來存每個average, 然後盡可能提高avg小的那個classes[i]
但馬上就被第一個test case給擋住

這邊有個對於提高平均的數學直覺是, 我們每當對分子分母`+1`來提高平均
每次提高的平均會遞減, 所獲得的效益會變差

所以為了拉高整體平均, 我們要關注的是把**extra student**放到哪個班級裡效益才會最高
所以我們應該是把每個班級所能提升的效益放入max heap裡才對

加入extra student的平均減去當前平均, 就是加入extra student後所能拉高整體平均的效益
我們把每個extra student放入當前效益最大的的班級, 這樣最後就是我們所能獲得的最高平均