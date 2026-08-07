class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Process though for this solution that I learned:

        popping rewrites the data behind the loop's back, but the loop   only ever looks forward

so that's why one of the solutions is terate backwards in order to avoid skip elements because of the shift by one to the left that the pop methods do under the hood, while terating forwards
        """
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)