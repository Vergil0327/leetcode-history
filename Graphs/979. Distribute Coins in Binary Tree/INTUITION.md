# Intuition

最終目標是把硬幣全部剛好分配到每個節點各1個
從leaf開始走, 如果是left-subtree的leaf coin一路往上走都分配光了
那勢必得往右走向right-subtree

所以我們記錄每個節點有多少個1-coin需要移動出去(或是需要反向移動回來)

ex.1 3個硬幣有兩個硬幣一路往上, 兩個硬幣各走一步, 右邊則是需要一個硬幣, 往上走一步
每個節點都要分配一個硬幣所以, 左邊我們紀錄3-1=+2, 右邊我們紀錄0-1 = -1
但由於我們只需要知道他們分配需要的步數, 所以全部取abs即可, 正只是代表往外分配, 負數代表要有硬幣分配過來, 正負其實只代表方向性
所以left-subtree硬幣取abs走的步數再加上right-subtree取abs走的步數就是最終硬幣需要走的步數
而post-order dfs就記錄有多少硬幣還可以進行分配(正數), 或是還有多少硬幣需要分配(負數)即可


# English

Overview
Given the root of a binary tree storing coins, our objective is to determine the minimum number of moves required to distribute the coins so that each node has exactly one coin. A move consists of moving one coin from a node to an adjacent node.

We will need to traverse the tree to distribute the coins.

If you are not familiar with tree traversal, check out our Tree Traversal Explore Card

Approach 1: Depth-First Search
Intuition
We need to ensure each node contains one coin. Let's start with an example. How do we obtain a coin for the root node?

Input [0,0,2,4,0,1,0]

Example A

We could give the blue root node a coin from its red right child. However, this is not an optimal move, as then, a coin from the leftmost node in the tree with four coins must be passed to the red node's child that has zero coins.

From the root, it's hard to determine how to optimally distribute the coins because we don't have enough information about the subtrees.

What if we started distributing coins from the leaves?

Example B

If we represent extra coins as positive values and needed coins as negative values we can calculate the coins exchanged in the subtree rooted at the red node as follows:

current.val = current.val + leftCoins + rightCoins = 0 + 3 + -1 = 2
current is the red parent node in the subtree, and leftCoins and rightCoins are the number of coins the children need to exchange.

There are three cases for distributing coins from a leaf node:

The leaf node doesn't have any coins: Take a coin from the parent, since the parent is the only node it is connected to.
The leaf node has exactly one coin: No coins need to be exchanged.
The leaf node has more than one coin: Keep one coin and give all the extra coins to the parent.
From a leaf node, we can directly determine how to optimally distribute coins in the subtree because the only neighbor a leaf can exchange with is their parent.

How will we traverse the tree so that we handle child nodes before parent nodes? One of the primary ways to traverse a tree is a Depth-First Search (DFS). There are three main traversal types for DFS, one of which is a postorder traversal. In a postorder traversal, the left subtree is visited first, then the right, then the root.

Recursive DFS Postorder Traversal Template:

If the tree is empty, return.
Traverse the left subtree: dfs(root.left).
Traverse the right subtree: dfs(root.right).
Handle the root.
Moving up the tree, how many coins can the current node pass on to its parent?

Example C

The current node will keep one of its coins, so it will pass on one less than the number of coins it has. This means if it has only one coin, it won't pass on any coins.

The best practice is not to modify the input, so instead of manipulating the node's value, we will pass along the number of coins exchanged.

Example D

We can calculate the number of coins a parent node can pass on to its parent by subtracting one from its value to represent the coin it keeps, then adding the number of coins its left and right subtrees need to exchange.

To calculate the number of coins each subtree needs to exchange, we implement a recursive function, dfs, using the postorder traversal template.

dfs:

If the tree is empty, return 0.
Calculate the number of coins the left subtree needs to exchange: leftCoins = dfs(root.left).
Calculate the number of coins the left subtree needs to exchange: rightCoins = dfs(root.right).
Return the number of coins the current node has available to exchange with its parent: (current.val - 1) + leftCoins + rightCoins.
This function would calculate the number of coins each node needs to exchange with its parent. This is not the number of moves, but we can calculate the number of moves in the same function.

Example E

For the green highlighted subtree, it takes three moves to give each extra coin from the left child to the parent and one move to give one coin from the parent to the right child. In total, four coin exchanges occurred, requiring four moves. We calculate the number of moves by adding the absolute values of the number of coins each child needs to exchange with its parent node.

In the dfs function, we add the number of moves it takes to distribute coins within the current subtree to a globally maintained running sum before handling the root.

How do we know this process provides the minimum number of moves? Each child node either gives coins to or receives coins from its parent, but not both. Each node exchanges coins with its direct neighbors in a unidirectional flow, minimizing the total number of moves.

Algorithm:

1. Initialize a variable moves to 0.
2. Define a recursive function dfs that counts the number of moves needed to distribute the coins in the tree given the root as current.
    - Base case: If current is null, return 0 because no coins need to be exchanged.
    - Set a variable leftCoins to the number of coins the left subtree needs to exchange, the result of dfs(current.left).
    - Set a variable rightCoins to the number of coins the right subtree needs to exchange, the result of dfs(current.right).
    - Calculate the number of moves needed to distribute coins in each of the subtrees. Since the coins exchanged may be negative, we sum the absolute values of leftCoins and rightCoins and then add this sum to moves.
    - Return the number of coins the current node has available to exchange with its parent. It will keep one coin, so subtract 1 from its value and sum the result with leftCoins and rightCoins.
3. Call dfs(current).
4. Return moves.