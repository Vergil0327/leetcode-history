class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        n = len(s)
        arr = [ord(ch) for ch in s]

        # since s has already been beautiful
        # for i position, we only need to check i-1 and i-2 position
        # i-1: AA palindrome
        # i-2: AXA palindrome
        def checkBautiful(arr, i):
            if i-1 >= 0 and arr[i-1] == arr[i]: # check AA palindrome
                return False
            if i-2 >= 0 and arr[i-2] == arr[i]: # check AXA palindrome
                return False
            return True
            
        for i in range(n-1, -1, -1):
            for ch in range(arr[i]+1, ord("a")+k):
                arr[i] = ch
                if checkBautiful(arr, i):
                    k = i+1
                    
                    while k < n:
                        mod = 0
                        arr[k] = ord("a")+mod
                        while not checkBautiful(arr, k):
                            mod = (mod+1)%3
                            arr[k] = ord("a")+mod

                        k += 1

                    return "".join(chr(rune) for rune in arr)
        return ""
