class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        n = len(sentence)
        res = ""
        i = 0
        while i < n:
            if sentence[i] == "$":
                j = i+1
                while j < n and sentence[j] != " ":
                    j += 1

                price = sentence[i+1:j]
                if price and price.isdigit() and (i-1 < 0 or sentence[i-1] == " "):
                    res += sentence[i] + f"{int(price) * (100-discount)/100:.2f}"
                else:
                    res += sentence[i:j]
                i = j-1
            else:
                res += sentence[i]
            i += 1
        return res

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        res = ""
        words = sentence.split()
        for word in words:
            if word[0] == "$" and word[1:] and word[1:].isdigit():
                word = f"${int(word[1:]) * (100-discount)/100:.2f}"

            res += word + " "
        return res[:-1]