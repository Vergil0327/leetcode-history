@cache
def powmod(x, power, mod):
    if power == 0: return 1
    if x == 1: return 1
    if x == 0: return 0
    
    y = powmod(x, power//2, mod)%mod
    if power%2:
        return x * y * y % mod
    else:
        return y * y % mod
