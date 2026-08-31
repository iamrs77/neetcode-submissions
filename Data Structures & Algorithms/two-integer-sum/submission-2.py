class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []

        dicti = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dicti:
                return [dicti[diff], i]
            dicti[num] = i
        
        return []


        