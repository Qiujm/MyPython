# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time
# complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        comb_array = []
        index1 = index2 = 0
        while index1<len(nums1) or index2<len(nums2):
            if index1>=len(nums1):
                comb_array.extend(nums2[index2:])
                break
            elif index2>=len(nums2):
                comb_array.extend(nums1[index1:])
                break
            else:
                if nums1[index1]<= nums2[index2]:
                    comb_array.append(nums1[index1])
                    index1 +=1
                else:
                    comb_array.append(nums2[index2])
                    index2+=1
        mid = (len(comb_array) - 1) // 2
        if  (len(comb_array)-1) % 2  :
            print(comb_array)
            return float((comb_array[mid]+comb_array[mid+1]))/2
        else:
            print(comb_array)
            return float(comb_array[mid])

    def findMedianSortedArrays2(self, nums1, nums2):
        comb_array = sorted(nums1 + nums2)
        result = 0
        if len(comb_array) % 2 == 0:
            result = (comb_array[int(len(comb_array) / 2)] + comb_array[int(len(comb_array) / 2) - 1]) / 2
        else:
            result = comb_array[len(comb_array) // 2]
        return result



nums1=[1,2]
nums2=[3,4]
median = Solution().findMedianSortedArrays(nums1,nums2)
median2 = Solution().findMedianSortedArrays2(nums1,nums2)
print(median)
print(median2)




