# Iterate all the n-bit state where there are m 1-bits.
state = (1<<m)-1
while state < (1<<n):
    # do something to submask

    c = state & -state # LSB
    r = state+c
    state = (((r^state)>>2)//c) | r



# Iterate submask

state = some bitmask
submask = state
while submask > 0:
	submask = (submask-1)&state
