class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

        arr = [ch for ch in s if ch in vowels]
        arr.sort()
        
        result = []
        i = 0
        for ch in s:
            if ch in vowels:
                result.append(arr[i])
                i += 1
            else:
                result.append(ch)
        
        return "".join(result)
    
solution = Solution()
res = solution.sortVowels("lEetcOde")
print(res)