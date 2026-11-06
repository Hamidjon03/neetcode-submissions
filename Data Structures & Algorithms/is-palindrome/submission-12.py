class Solution:
    def isPalindrome(self, s: str) -> bool:
        # set two pointers, one at the begining, other at the end
        # check every char for alphanumeric
        # if char is non alphanumeric move the pointers
        # compare left and righ characters
        # if they different return False
        n = len(s)
        l = 0
        r = n - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1

        return True

    
    def alphaNum(self, char):
        return (
            ord('A') <= ord(char) <= ord('Z') or
            ord('a') <= ord(char) <= ord('z') or
            ord('0') <= ord(char) <= ord('9')
        )