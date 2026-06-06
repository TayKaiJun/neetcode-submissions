class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        for _ in range(32):
            r = r << 1
            r += n & 1
            n = n >> 1
        
        return r
            