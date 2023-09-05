# Intuition

1. 最直覺方式是先O(n)時間用一個hashmap儲存每個節點的clone, 然後再一次O(n)來連接random ponter


2. 但也可以有O(1)的做法
   - 將每個節點的clone與原節點交錯(side-by-side)的連在一起: `Node1 -> Node1_Clone -> Node2 -> Node2_Clone -> ...`
   - 然後再用O(n)時間連接ramdom pointer, 此時每個節點的clone就是自身節點的`node.next`
   - 每個原節點的下個節點為`node.next.next`, 所以我們可以在用O(n)時間遍歷一遍來還原原linked-list以及將所有clone nodes連接在一起