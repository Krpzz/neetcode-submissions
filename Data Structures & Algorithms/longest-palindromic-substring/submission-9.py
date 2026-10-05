class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for start in range(len(s)):
            for end in range(start + 1, len(s) + 1):
                string = s[start:end]

                if string == string[::-1]:
                    if len(string) > len(longest):
                        longest = string
        
        
        return longest