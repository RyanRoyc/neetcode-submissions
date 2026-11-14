class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for char in s:
            if char.isalnum():
                string += char

        string = string.lower()
        reversedString = string[::-1]
        
        return string == reversedString

        