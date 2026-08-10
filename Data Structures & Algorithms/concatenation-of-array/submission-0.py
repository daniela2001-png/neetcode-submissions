class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        i = 0
        # time complexity 2n --> ends being O(n) :D
        while i >= 0 and i < n:
            ans.append(nums[i])
            i = i + 1
        i = 0
        while i >= 0 and i < n:
            ans.append(nums[i])
            i = i + 1
        return ans
            