#
# @lc app=leetcode id=977 lang=python
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        left =0
        right =n-1
        for i in range(n-1,-1,-1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left +=1
            else:
                result[i] = nums[right] ** 2
                right -=1
        return result
                
        
# @lc code=end

