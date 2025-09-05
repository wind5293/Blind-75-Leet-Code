class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(ch for ch in s if ch.isalnum()).lower()    
        
        reverse = string[::-1]          
        return string == reverse
                    
    # Too devil wtf
    # def isPalindrome(self, s: str) -> bool:
    #     cha = {' ',',',':','.','@','#','_','-','/','/','"','{','}','[',']',"'",'?',';','!','\\','(',')','`'}
    #     for i in cha:
    #         s = s.replace(i,'')
    #     s = s.lower()
    #     return s == s[::-1] 
                    
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))