# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]
import time
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        startt=time.time()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    last_for = time.time() - startt
                    print(last_for)
                    return [i,j]



    # result:
    # Runtime: 5052 ms, faster than 11.17% of Python online submissions for Two Sum.
    # Memory Usage: 12.7 MB, less than 5.02% of Python online submissions for Two Sum.

    def twoSum2(self, nums, target):
        startt=time.time()
        d = {nums[i]: i for i in range(len(nums))}
        i = 0

        while True:
            j = target - nums[i]
            if j in d and d[j] != i:
                last_for = time.time() - startt
                print(last_for)
                return i, d[j]
                break
            else:
                i += 1


# nums = [2,7,11,15]
nums=[]
for i in range(100000):
    nums.append(i)
list = Solution().twoSum2(nums,173156)
print(list)

map()