class Solution:
    # O(n ^ 3)
    # def checkPalindrome(self, s: str) -> bool:
    #     length = len(s)
    #     for i in range(0, length // 2):
    #         if s[i] != s[length - i - 1]:
    #             return False
    #     return True

    # def longestPalindrome(self, s: str) -> str:
    #     res = 0
    #     str_res = ""
    #     for right in range(0, len(s)):
    #         for left in range(0, right + 1):
    #             str_temp = s[left:right + 1]
    #             if self.checkPalindrome(str_temp) and res < len(str_temp):
    #                 res = len(str_temp)
    #                 str_res = str_temp    
        
    #     return str_res
    
    # O(n ^ 2)
    
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        res = ""
        for i in range(len(s)):
            odd_pal = expandAroundCenter(i, i)
            if len(odd_pal) > len(res):
                res = odd_pal

            even_pal = expandAroundCenter(i, i + 1)
            if len(even_pal) > len(res):
                res = even_pal
        
        return res
        
solution = Solution()        
result = solution.longestPalindrome("abcba")
print(result)