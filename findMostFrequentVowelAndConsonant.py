from typing import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = Counter(s) # counter biến freq trở thành 1 hash map lưu ch : counter
        vowels = set("aiueo")

        maxVowels = 0
        maxConsonant = 0
        
        for ch, count in freq.items(): # lấy dữ liệu từ freq
            if ch in vowels:
                if count > maxVowels:
                    maxVowels = count
            else:
                if count > maxConsonant:
                    maxConsonant = count
            
        return maxVowels + maxConsonant        
            
solution = Solution()
print(solution.maxFreqSum("successes"))