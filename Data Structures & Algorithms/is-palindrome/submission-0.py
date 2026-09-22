class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ''
        for c in s :
            if c.isalnum() :
                a = c.lower()
                newstr += a      
        return newstr == newstr[ : : -1]