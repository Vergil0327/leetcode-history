# explanation: https://labuladong.github.io/algo/2/20/28/

# return index of matched substring
def rabinKarp(txt: str, pattern: str) -> int:
    # 位數
    L = len(pattern)

    # 進位制
    R = 256 # ascii code (256 characters)

    # 大數 質數 求餘數
    Q = 1658598167

    # R ** (L-1)
    RL = 1
    for i in range(1, L):
        RL = (RL * R) % Q # avoid overflow
    
    # construct pattern's hash
    patHash = 0
    for i in range(len(pattern)):
        patHash = (R * patHash + ord(pattern[i])) % Q

    windowHash = 0
    l, r = 0, 0
    while r < len(txt):
        # (X+Y) % Q = (X%Q + Y%Q) % Q
        # X % Q = (X+Q) % Q
        windowHash = ((R * windowHash) % Q + ord(txt[r])) % Q
        r += 1

        if r-l == L:
            if windowHash == patHash:
                # prevent hash collision
                if txt[l:r] == pattern:
                    return l
        
            # because windowHash - (ord(txt[l]) * RL)%Q can be negative, we plus Q to make sure windowHash is positive
            windowHash = (windowHash - (ord(txt[l]) * RL)%Q + Q) % Q
            l += 1
    
    return -1 # if not found
