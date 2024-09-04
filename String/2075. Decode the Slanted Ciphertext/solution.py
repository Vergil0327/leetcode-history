class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n//rows

        texts = []
        for i in range(rows):
            texts.append(encodedText[i*cols:i*cols+cols])

        res = ""
        for c in range(cols):
            for r in range(rows):
                if c+r < cols:
                    res += texts[r][c+r]
        
        return res.rstrip()
