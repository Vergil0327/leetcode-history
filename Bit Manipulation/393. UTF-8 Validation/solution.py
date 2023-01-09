class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        nums = deque(data)
        def countLeftOne(num):
            cnt = 0
            for i in range(7, -1, -1):
                if (num >> i)&1:
                    cnt += 1
                else:
                    break
            return cnt

        while nums:
            headerByte = nums.popleft()
            ones = countLeftOne(headerByte)

            if ones == 1: return False
            if ones >= 5: return False
            if ones > 1:
                nBytes = ones-1
                while nums and nBytes > 0:
                    datum = nums.popleft()
                    if ((datum >> 6) & 0b10) != 0b10: return False
                    nBytes -= 1
                if nBytes != 0: return False
        return True  