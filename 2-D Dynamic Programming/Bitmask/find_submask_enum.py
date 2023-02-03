# 遍歷bitmask subset的模板
# total m bits
def find_submask(m):
    for bitmask in range(1, 1<<m):
        submask = bitmask
        while submask:
            print(submask)
            submask = (submask-1)&bitmask

