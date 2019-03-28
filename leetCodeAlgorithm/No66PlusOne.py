# Given a non-empty array of digits representing a non-negative integer,
#  plus one to the integer.
#
# The digits are stored such that the most significant
# digit is at the head of the list, and each element in the array
# contain a single digit.
#
# You may assume the integer does not contain any
# leading zero, except the number 0 itself.
# Example 1:
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return
        index=len(digits)-1
        digits[index]+=1
        flag= digits[index] == 10
        while flag:
            digits[index] = 0
            if index >0:
                index-=1
                digits[index] +=1
            else:
                digits.insert(0, 1)
            flag=digits[index] == 10


ls=[1,2,3]
ls2=[9,9,9]
Solution().plusOne(ls)
print(ls)

