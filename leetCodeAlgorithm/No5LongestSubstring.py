# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"
from copy import  deepcopy
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        substr = ''
        for i in range(len(s)):
            odd = self.getPalindrome(s,i,i)
            if len(substr)<len(odd):
                substr=odd
            even= self.getPalindrome(s,i,i+1)
            if len(substr) < len(even):
                substr = even
                # substr = max(len(substr),len(odd),len(even))
        return substr

    def getPalindrome(self,s,l,r):
        while l>=0 and r<len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1:r]



s="helloollwe"
s1='babad'
s2='cb'
m=Solution().longestPalindrome(s2)
print(m)



