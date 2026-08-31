class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mid = math.floor(len(nums)/2)
        return sorted(nums)[mid]