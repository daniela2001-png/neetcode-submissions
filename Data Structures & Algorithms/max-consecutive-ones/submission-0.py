class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter_ones = 0
        counter = 0
        lenght = len(nums)
        max_number_ones = 0

        while (counter < lenght):
            if nums[counter] == 1:
                counter_ones += 1
            
                if counter_ones > max_number_ones:
                    max_number_ones = counter_ones
            else:
                counter_ones = 0
            counter += 1   
        return max_number_ones

       
