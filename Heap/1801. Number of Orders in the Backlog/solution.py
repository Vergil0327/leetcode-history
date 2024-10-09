from sortedcontainers import SortedDict
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy, sell = SortedDict(), SortedDict()

        for price, amount, orderType in orders:
            if orderType == 0: # Buy
                while price in buy and buy[price] and sell and sell.peekitem(0)[0] <= price:
                    k, v = sell.peekitem(0)
                    matched = min(buy[price], v)
                    sell[k] -= matched
                    buy[price] -= matched
                    
                    if sell[k] == 0:
                        del sell[k]
                    if buy[price] == 0:
                        del buy[price]

            else: # Sell
                sell[price] = sell.get(price, 0) + amount
                while price in sell and sell[price] and buy and buy.peekitem(-1)[0] >= price:
                    k, v = buy.peekitem(-1)
                    matched = min(sell[price], v)
                    buy[k] -= matched
                    sell[price] -= matched
                    
                    if buy[k] == 0:
                        del buy[k]
                    if sell[price] == 0:
                        del sell[price]

        return (sum(sell.values()) + sum(buy.values())) % (10**9 + 7)

# heap solution
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        sell_orders = []
        buy_orders = []

        for price, amount, isSell in orders:
            if isSell == 1:
                while amount > 0 and len(buy_orders)> 0 and -1 * buy_orders[0][0] >= price:
                    buy_price, buy_amount = heapq.heappop(buy_orders)
                    buy_price = -1 * buy_price
                    if buy_amount > amount:
                        buy_amount -= amount
                        amount = 0
                        heapq.heappush(buy_orders, (-buy_price, buy_amount)) # push as max heap
                    else:
                        amount -= buy_amount 

                if amount > 0:
                    heapq.heappush(sell_orders, (price, amount))
            else: # isBuy  
                while amount > 0 and len(sell_orders)> 0 and sell_orders[0][0] <= price:
                    sell_price, sell_amount = heapq.heappop(sell_orders)
                    
                    if sell_amount > amount:
                        sell_amount -= amount
                        amount = 0
                        heapq.heappush(sell_orders, (sell_price, sell_amount)) # push as max heap
                    else:
                        amount -= sell_amount 

                if amount > 0:
                    heapq.heappush(buy_orders, (-1* price, amount))

        res = 0
        for _, cnt in buy_orders:
            res = (res + cnt) % (10**9 + 7)
        for _, cnt in sell_orders:
            res = (res + cnt) % (10**9 + 7)
        
        return res
