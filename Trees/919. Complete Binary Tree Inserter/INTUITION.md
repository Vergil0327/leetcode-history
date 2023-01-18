# Intuition

這題的目標是一層一層照順序插入每個TreeNode，這邊能聯想到的是heap也是棵樹，但是個用1-indexed array表示的樹

所以如果我們將所有TreeNode存放在array裡的話，並在0-index位置放上個dummy node，則

index = 1 為root
每個index位置的左右子節點則分別為:
- 2*index
- 2*index+1

`ex. tree = [NULL, 1,2,3,4,5,6,7,8,9,10]`

因此我們可以透過`插入位置的index//2`找出父節點
並且透過`當前插入位置index == 2 * parent_index ? 左節點 : 右節點`判斷當前節點為父節點的左節點或右節點

而每次要插入的位置為 `len(tree)`

# Complexity

- time complexity
$$O(1)$$ for both operations

- space complexity
$$O(n)$$