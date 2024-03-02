#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        result = []
        left,right = 0, n -1 
        while left < n-1:
            if nums[left] + nums[right] == target:
                result.append(left)
                result.append(right)
                break
            if right > left:
                right -= 1
            if right == left:
                left += 1
                right = n-1
        return result
            
        
# @lc code=end

