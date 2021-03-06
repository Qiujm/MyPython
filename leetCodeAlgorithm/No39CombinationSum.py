# Given a set of candidate numbers (candidates) (without duplicates)
# and a target number (target), find all unique combinations in
# candidates where the candidate numbers sums to target.
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)

    # def combinationSum2(self, candidates, target):
    #     res = []
    #     tempSum=0
    #     stack=[]
    #     candidates.sort()
    #     start=0
    #     tempTarget = target
    #     while start < len(candidates):
    #         index=start
    #         while tempTarget >0:
    #             stack.append(candidates[index])
    #             tempTarget -= candidates[index]
    #             if tempTarget == 0:
    #                 res.append(stack)
    #
    #
    #
    #     return res

can = [2,3,6,7]
result=Solution().combinationSum(can,7)
print(result)
"""
def dfs(self, nums, target, index, path, res): [2,3,6,7] , 4, 1, [3] []
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)): 1
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res) [2,3,6,7] , 4, 1, [3] []


"""

