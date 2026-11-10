class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        if j == 0: return True

        while j > i:
            if not s[i].isalnum(): 
                print("i not alpha numeric", s[i])
                i += 1
                continue
            if not s[j].isalnum(): 
                print("j not alpha numeric", s[j], j)
                j -= 1
                print(j)
                continue
            if s[i].isalpha and s[i].isascii(): left = s[i].lower()
            else: left = int(s[i])
            if s[j].isalpha and s[j].isascii(): right = s[j].lower()
            else: right = int(s[j])

            if left == right: 
                i += 1
                j -= 1
            else: 
                print(s[i], s[j])
                return False
        
        return True
        