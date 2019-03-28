# Determine whether an integer is a palindrome. An integer is
# a palindrome when it reads the same backward as forward.
#
# Example 1:
# Input: 121
# Output: true
# Example 2:
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left,
# it becomes 121-. Therefore it is not a palindrome.
# Example 3:
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:
# Coud you solve it without converting the integer to a string?

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        length=len(s)
        i=0
        while i<length//2:
            if s[i] != s[length-1-i]:
                return False
            i+=1
        return True

x=-121
result=Solution().isPalindrome(x)
print(result)

