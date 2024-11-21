# Intuition

since 0 <= num <= 100, we can store num's index first

if we want to calculate product, just iterate num from 0 to 100 and use binary search to know how many of them

time:
    - def add(self, num: int): O(1)
    - def getProduct(self, k: int): O(100 * log(n))


# Optimization

雖然一開始看到題目, 有想到這可以利用類似prefix sum的概念來做
但當時想不到該如何解決存在`num=0`時的情況該如何處理區間的prodcut

但其實一旦出現num=0, 那麼代表後去的乘積都會是**0**
那其實我們就整個prefix product array重新開始即可, 超出size的代表之前都為**0**

```py
def __init__(self):
    self.prefix = [1] 

def add(self, num: int) -> None:
    if num == 0:
        self.prefix = [1]
    else:
        self.prefix.append(self.prefix[-1]*num)

def getProduct(self, k: int) -> int:
    n = len(self.prefix)
    
    if k == n-1:
        return(self.prefix[-1])
    elif k > n-1:
        return 0
    else:
        return(self.prefix[-1]//self.prefix[n-k-1])
```

time:
    - def add(self, num: int): O(1)
    - def getProduct(self, k: int): O(1)