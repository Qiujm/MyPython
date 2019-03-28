# Implement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary until
# the first non-whitespace character is found. Then, starting from this character,
# takes an optional initial plus or minus sign followed by as many numerical digits
# as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral
# number, which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral
# number, or if no such sequence exists because either str is empty or it contains only
# whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within
# the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of
# the range of representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX=pow(2,31)-1
        INT_MIN = -pow(2,31)
        str=str.strip()
        box=['0','1','2','3','4','5','6','7','8','9','-','+']
        origin = list(str)
        if  not origin or origin[0] not in box:
            return 0
        n=1
        while n< len(origin):
            if origin[n] not in box[:10]:
                break
            else:
                n+=1
        # if origin[0] == '+':
        #     target=origin[1:n]
        # else:
        #     target=origin[:n]

        target=origin[:n]
        result=''.join(target)
        if result == '-' or result == '+':
            return 0
        result=int(result)
        if result>0:
            return min(result,INT_MAX)
        return max(result,INT_MIN)


str='4193 with words'
str2='words and 987'
str3='+912834'
result=Solution().myAtoi(str3)
print(result)

# s=['+','2','4','5','3']
# print(''.join(s))
# print(int(''.join(s)))
# # ls=[1,2,3,4,5,6]
# ls2=ls[:6]
# print(ls2)
d={'1':'a','3':'b'}
# print(type(d.keys()))
# print((d.keys()))
for key in d:
    print(key)
    print(d[key])