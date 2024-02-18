# Intuition

把每個點的八個方向數值全check過一遍, 看是不是prime number即可

確認是不是prime的方式也很簡單, 用O(sqrt(num))的時間即可確認
```py
def isPrime(num):
    for i in range(2, int(sqrt(num))+1):
        if num%i == 0: return False
    return True
```