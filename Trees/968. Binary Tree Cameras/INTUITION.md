# Intuition

有點像house robber, 一開始想法是tree traversal DP

如果裝在root node, 那麼left node, right node都不用裝
如果不裝, 那麼:
    - parent已cover, 但是如果沒有child node 且 parent沒cover, 那麼本身必須得裝
    - 如果left node, right node都存在, 那就是擇一安裝來cocver root node
    - 如果任一不在, 那另個就必須得裝

但由上往下進行DFS時
要不要安裝camera在node上, 除了受parent node影響外, 還跟left node跟right node的狀態也有關係
我們在要決定left node時, 這時right node狀態是平行的, 同樣也還沒決定
這樣其實就沒辦法用dp來計算, 因為dp都是根據過往的狀態來決定下個狀態

這時再想一下, 如果反過來改從leaf node出發
- 如果leaf node有裝, 那parent node就不需要
- 如果沒有, 那parent node就需要
- 兩個一比, 肯定是裝在leaf's parent比較好 => greedy algorithm.

所以為了cover所有leaf nodes, 所有leaf node's parent都必須裝camera
所以:

- 如果是leaf node, 那不用裝camera => 狀態0
- 如果是leaf node's parent, 那必須裝一台camera => `res += 1` => 狀態1
- 再來後續節點又分成
    1. 被cover, 自身沒有camera => 相當於leaf node那個狀態 => 狀態2
    2. 沒被cover => 相當於leaf node's parent, 必須裝camera => `res += 1` => 狀態1

所以我們用0/1/2三種狀態 來表示該節點是屬於狀態0, 狀態1, 狀態2, 共三種狀態其中:
1. 狀態0: leaf node
2. 狀態1: has camera, and leaf node's parent must be this state
3. 狀態2: covered node

- 所以如果任一child node是狀態0, 那代表node是leaf parent: res += 1 and return 1
- 如果任一child node是1, 代表他是狀態2: return 2
- 最後, 也就是如果兩個child node都是狀態2, 代表底下節點都被cover到了, 那麼當前節點就相當於是個狀態0的leaf node: return 0

**edge case**

如果root node本身也是leaf node的話
也就是如果`state = dfs(root) and state == 0`的話
由於root node沒有parent's node可裝camera, 所以必須裝在他自身
因此在這情況下, 最終結果必須`+1`