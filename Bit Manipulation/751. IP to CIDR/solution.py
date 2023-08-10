from typing import List
import math

class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        # ip to value: ip = 8-bit + 8-bit + 8-bit + 8-bit
        x = 0
        for v in ip.split("."):
            x = x*256 + int(v)

        def valToIP(v, step):
            ip1 = str((v>>24)&255)
            ip2 = str((v>>16)&255)
            ip3 = str((v>>8)&255)
            ip4 = str(v&255)
            return f"{ip1}.{ip2}.{ip3}.{ip4}/{32-int(math.log2(step))}"

        res = []
        while n > 0:
            cover = x & -x # LSB
            while cover > n:
                cover >>= 1
            res.append(valToIP(x, cover))
            x += cover
            n -= cover
        return res