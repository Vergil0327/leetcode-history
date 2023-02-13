# O(C(N, K))
state = (1<<m)-1
while state < (1<<n):
    # do something to submask

    c = state & -state # LSB
    r = state+c
    state = (((r^state)>>2)//c) | r
