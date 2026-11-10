class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        if j == 0: return True

        while j > i:
            if not s[i].isalnum(): 
                i += 1
                continue
            if not s[j].isalnum(): 
                j -= 1
                continue
            if s[i].isalpha and s[i].isascii(): left = s[i].lower()
            else: left = int(s[i])
            if s[j].isalpha and s[j].isascii(): right = s[j].lower()
            else: right = int(s[j])

            if left == right: 
                i += 1
                j -= 1
            else: 
                return False
        
        return True
        