class Solution(object):
    def containsDuplicate(self, nums):
        return True if len(nums) > len(set(nums)) else False
