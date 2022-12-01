### Union-Find

2n個人要分在n個couch，首先我們找出每個couple對應分配到的couch

我們逐步來看每個couple的位置，couple從[0,1]到[n-2,n-1]
- 如果couple本身就坐在同一張couch上，那不用swap
- 如果不一樣，那必須swap一次，換完後視同兩張couch連通在一起(union step)
union的次數即為答案，我們可以看以下example

每個couple是個group，couple間的連線edge可以看到需不需要swap
一但swap，代表我們把兩個couch一起，同時兩個couch上的couple也union在一起
第一個example，swap(union)一次，同時兩個couple也都分配對的位置

如果像是第三個example, union一次後還是還沒正確swap完
但沒關係，實質上再union一次後，全部連通在一起後，就分配結束了

couchID:    0      1
coupleID: [0, 2], [1, 3]
edge:      --------- 連接couple [0,1]
edge:          --------- 連接couple[2,3]
couple_to_couch: [[0,1],[0,1]], union 一次

couchID:     0      1
coupleID: [3, 2], [0, 1]
edge:      -----   -----
couple_to_couch: [[0,0],[1,1]]

couchID:     0      1       2
coupleID: [0, 2], [1, 4], [3, 5]
edge:      ---------   --------- 連接couple [0,1], [4,5]
edge:         -------------- 連接couple [2,3]
union: couch0-couch1 (couple[0,1])
union: couch1-couch2 (couple[2,3])
couple[3,4]所做的couch已連通在一起
couple_to_couch: [[0,1],[1,2],[0,2]]