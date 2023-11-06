# Intuition

每個path必須至少留有一個不能拿
如果決定不拿root node, 那底下各個子path就都可以取走
如果決定要拿root node, 那麼底下各個子path就每條路都必須至少有1個不能拿
所以我們比較不拿當前root node跟不拿底下所有子path哪個比較小, 取最小的cost不拿
那最終答案就是sum(values)減去拿走的節點的總和

define `dfs(node, prev): the minimum sum to make tree healthy`