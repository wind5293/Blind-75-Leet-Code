from operator import __inv__


class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""
        while n != 0:
            mod = n % 2
            binary = str(mod) + binary
            n //= 2

        binary.zfill(32)
        print(binary)
        
solution = Solution()
print(solution.reverseBits(43261596))