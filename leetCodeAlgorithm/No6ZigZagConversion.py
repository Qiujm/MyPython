# The string "PAYPALISHIRING" is written in a zigzag pattern on
# a given number of rows like this:
# (you may want to display this pattern in
# a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);

# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # row1 = 2*(numRows-1)*(n-1)
        # n,rest=divmod(len(s)-1,numRows)
        lyst = list(s)
        if numRows==1 or len(s) <= numRows:
            return s
        new_list = []
        for r in range(numRows):
            lists = []
            new_list.append(lists)

        i = index = 0
        symbol = 1
        while index < len(s):
            if i == numRows - 1:
                symbol = -1
            elif i == 0:
                symbol = 1
            new_list[i].append(s[index])
            i += symbol
            index += 1
        lists=[]
        for ls in new_list:
            lists.append(''.join(ls))
        return ''.join(lists)


s = "PAYPALISHIRING"
s2="ABC"
# result=Solution().convert(s2, 1)
# print(result)

# lis = ['zhangsan','lisi','wangwu']
# for index,name in enumerate(lis):
#     print(index)
#     print(name)

l=['']*5
print(l)
