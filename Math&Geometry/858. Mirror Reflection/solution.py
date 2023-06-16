class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        firstHitHeight = p*q//gcd(p,q) # lowest common multiply
        m = firstHitHeight//p
        n = firstHitHeight//q

        if n%2 == 0:
            if m%2 == 1:
                return 2
            # else:
            #     meet original position
            #     The test cases are guaranteed so that the ray will meet a receptor eventually.
        else:
            if m%2 == 0:
                return 0
            else:
                return 1