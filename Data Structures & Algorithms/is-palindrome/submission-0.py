class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ""
        for char in range(len(s)):
            if s[char].isalnum():
                p += s[char]
        lp = p.lower()
        rp = lp[::-1]
        if lp == rp:
            return True
        else:
            return False
        