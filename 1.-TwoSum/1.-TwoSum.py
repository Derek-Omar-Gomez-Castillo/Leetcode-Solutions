class Solution:
    def twoSum(nums, target):
        prevMap = {}
        for index, num in enumerate(nums):
            resta = target - num
            if resta in prevMap:
                return[prevMap[resta],index]
            prevMap[num] = index

Result = Solution
result = Result.twoSum
print(result([2,7,11,15], 9) , 'Expected: [0,1]')
print(result([3,2,4], 6), 'Expected: [1,2]')
print(result([3,3], 6), 'Expected: [0,1]')
