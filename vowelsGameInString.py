class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # vowels = set("aiueo")

        # arr = [ch for ch in s if ch in vowels]
        # if len(arr) == 0:
        #     return False
        
        # elif len(arr) % 2 == 1:
        #     return True

        # else:
        #     return True
        
        return any(c in "aiueo" for c in s)
              
solution = Solution()
print(solution.doesAliceWin("leetcoder"))
print(solution.doesAliceWin("bbcd"))