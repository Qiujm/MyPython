# Given a 32-bit signed integer, reverse digits of an integer.
# Example 1:
# Input: 123
# Output: 321
# Example 2:
# Input: -123
# Output: -321
# Example 3:
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only
#  store integers within the 32-bit signed integer range:
#  For the purpose of this problem,assume that your function
# returns 0 when the reversed integer overflows.


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        MAX = pow(2, 31) - 1
        MIN = -pow(2, 31)
        LEN = len(str(pow(2, 31)))
        lyst = list(str(x))
        if lyst[0] != '-':
            if len(lyst) > LEN or  (len(lyst)==LEN and ''.join(lyst) > str(MAX)):
                return 0
            addlist = ['0'] * (LEN - len(lyst))
            lyst.extend(addlist)
            lyst.reverse()
            result = ''.join(lyst)
            if result > str(MAX):
                return 0
            else:
                return int(result)
        else:
            if len(lyst) > LEN + 1 or  (len(lyst) == LEN+1 and ''.join(lyst) > str(MIN)):
                return 0
            addlist = ['0'] * (LEN - len(lyst)+1)
            lyst.extend(addlist)
            lyst.reverse()
            lyst.insert(0,'-')
            lyst.pop()
            result = ''.join(lyst)
            if result > str(MIN):
                return 0
            else:
                return int(result)

        # strnum = ''
        # lyst.reverse()
        # if lyst[len(lyst) - 1] != '-':
        #     strnum = ''.join(lyst)
        # else:
        #     strnum = '-' + ''.join(lyst[:-1])
        #
        # if len(strnum) > 11 or strnum > str(max) or strnum > str(min):
        #     return 0
        # else:
        #     return int(strnum)

            # if int(strnum) in range(-pow(2,31),pow(2,31)):
            #     return int(strnum)
            # else:
            #     return 0


num = 900000
result = Solution().reverse(num)
print("2^31=%d" % pow(2, 31))
print(result)
