class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        countmap = defaultdict(int)

        for num in nums:
            countmap[num] += 1

        n = len(nums) // 3

        res = []
        for key, value in countmap.items():
            if value > n:
                res.append(key)
        
        return res
        