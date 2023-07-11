class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.k2v = {k:v for k, v in zip(keys, values)}

        self.count = defaultdict(int)
        for d in dictionary:
            enc = self._encrypt(d)
            self.count[enc] += 1

    def _encrypt(self, word1: str) -> str:
        s = ""
        for c in word1:
            s += self.k2v.get(c, "$")
        return s

    def encrypt(self, word1: str) -> str:
        s = self._encrypt(word1)
        return s.replace("$", "")

    def decrypt(self, word2: str) -> int:
        return self.count[word2]
