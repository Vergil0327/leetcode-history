class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = deque(version1.split(".")), deque(version2.split("."))

        while v1 or v2:
            if not v1 and not v2: return 0
            
            if not v1:
                version = 0
                while v2:
                    version += int(v2.popleft())
                if version > 0: return -1
                else: return 0

            if not v2:
                version = 0
                while v1:
                    version += int(v1.popleft())
                if version > 0: return 1
                else: return 0

            a, b = int(v1.popleft()), int(v2.popleft())
            if a > b: return 1
            if a < b: return -1
        return 0