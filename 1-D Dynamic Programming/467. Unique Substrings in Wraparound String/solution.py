class Solution:
    """
    # Intuition

    base="abcdefghijklmnopqrstuvwxyz"

    see example: s="cac", answer=2

    {c,a} are substring inbase
    {ca, ac, cac} are NOT part of base

    at the same time, same substring should view as dupliate, don't count twice.
    
    example: s="cacac", still answer=2

    that is, we only need to count every valid substring that ends with 26 base characters {a,b,c,...,x,y,z} where `valid` means substring ends with that character in s is also a substring of base string
    store number of subsring which ends with character `ch` in `count[ch]`

    see ex3: s="zab"
    z: count[z]=1 => means 1 substring ends with z: {z}
    za: count[a]=2 => means 2 substring ends with a: {za, a}
    zab: count[b]=3 => means 3 substring ends with b: {zab,ab,b}

    what if we encounter "wxyzab" afterwards ?
    since we don't want to count duplicate, we just update count[b] = max(count[b], len("wxyzab"))

    based on intuition,
    we can iterate s[i] and calculate consecutive valid substring length

    the final answer is sum(count)
    """
    def findSubstringInWraproundString(self, s: str) -> int:
        n = len(s)
        
        # count[ord(ch)-ord("a")]: the number of valid substring ends with ch
        count = [0] * 26
        size = 0

        for i in range(n):
            if i>0 and ((ord(s[i])-ord(s[i-1])+26)%26) == 1:
                size += 1
            else:
                size = 1

            key = ord(s[i])-ord("a")
            count[key] = max(count[key], size)

        return sum(count)