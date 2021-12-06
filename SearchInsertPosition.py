#@author Jie
#
#***

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left = 0
        right = len(nums)-1
        
        if target <= nums[0]: return 0
        if target > nums[right]: return (right+1)
        
        while (right-left)>1:
            mid = int(math.floor((right-left)*0.5)+left)
            targetIsSmaller = (target<=nums[mid])
            left = left if targetIsSmaller else mid
            right = mid if targetIsSmaller else right
            
        return right
