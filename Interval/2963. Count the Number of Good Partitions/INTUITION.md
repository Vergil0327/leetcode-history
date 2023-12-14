# Intuition

由於是將nums分成多個連續的subarray, 這代表相同nums[i]必須全部group在一起
不然勢必會有至少兩個subarray擁有相同的nums[i]

ex. [X YYYY XYY] [ZZZ] or [X YYYY XYY ZZZ]

所以每個nums[i]都會有個最左跟最右的index範圍 nums[i] = [l, r]
將每個nums[i]的interval找出來後, 如果nums[i].interval跟nums[j].interval有重疊
那我們就要nums[i].interval跟nums[j].interval合併, 因為這情況我們沒辦法拆出兩個連續subarray有不重複的nums[i], nums[j]的

最後我們會得到多個區間: nums = [...] [...] [...] [...]
這時我們就只需計算他們的所有可能的合併組合
[X]     當區間有1個時： 1種
[X][Y]  當區間有2個時： 對於Y來說, 不合併的方法數有1種, 合併的方法數也有1種, 共2種
[X][Y][Z] 當區間有2個時: 對於Z來說, 到Y為止的方法數有2種. 所以Z不跟前面合併的方法數有2種, Z可以跟Y跟XY合併, 也有兩種, 所以總共4種
...
所以res = 1, 2, 4, 8, 16, 32 ... = 2^(m-1) 其中 m為最後不重複的區間數目
