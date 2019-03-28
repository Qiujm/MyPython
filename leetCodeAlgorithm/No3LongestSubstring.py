# Given a string, find the length of the longest substring without repeating characters.
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        slow = 0
        subdict = {}
        for fast,val in enumerate(s):
            # templen=0
            if val in subdict and subdict[val]>=slow:
                slow = subdict[val] +1
            subdict[val] = fast
            # templen +=1
            max_len = max(max_len,fast-slow+1)
        return max_len



str = 'abcbac'
count = Solution().lengthOfLongestSubstring(str)
print(count)
