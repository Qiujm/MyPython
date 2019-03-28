# Given a non-negative integer numRows, generate the
# first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of
# the two numbers directly above it.
# Example:
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]



class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        path=[1,1]
        res=[]
        self.generation(numRows, path, res)

    def generation(numRows,path,res):
        if numRows == len(res):
            return

        pass

ls=[['1'],['2']]
ls2=[['a0'],['b']]
print(ls<ls2)