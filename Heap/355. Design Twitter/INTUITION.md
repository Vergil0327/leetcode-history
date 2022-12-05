首先觀察題意

**確認需要的資料結構**

為了在`follow`跟`unfollow`有較好的效率，我們需要`hashset`或`hashmap`

- 我們可以把followee全加入`hashset`
- 或是利用`hashmap`, 並以Map[follower][followee]的形式紀錄關係

這邊我們使用`hashset`

另外在取得Newsfeed的時候，我們必須取得最新的10則，這邊暗示我們需要紀錄每個發文的**時間戳**, 因此我們必須維護一個單調遞增的變數來代表時間，並且每個tweet都必須附上時間戳

這邊想到一個比較好的做法是
我們可以用`doubly linked list`來儲存tweet，將最新的tweet永遠插入在最前方

那這樣在取得Newsfeed時我們可以把所有**followee**的tweets全部加入到`MaxHeap`裡，並根據時間比較，如此一來便可以確保每次取得的都是最新的tweet

並在取完的同時移動我們的ListNode到下一個不為根節點的節點，然後重新加入到`MaxHeap`裡

*ps: 自己也是自己的followee，記得把自己加入到followee中，不然會少取自己的tweet*

- 單調遞增的timestamp
- doubly linked list 紀錄tweet與timestamp
- max heap + doubly linked list用來取得最新的十則tweet ([merge k sorted lists problem](https://leetcode.com/problems/merge-k-sorted-lists/))