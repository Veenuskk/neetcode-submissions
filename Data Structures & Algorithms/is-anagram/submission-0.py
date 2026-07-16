class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m :
            return False
        a = sorted(s)
        b = sorted(t)
        if a == b :
            return True 
        return False
            