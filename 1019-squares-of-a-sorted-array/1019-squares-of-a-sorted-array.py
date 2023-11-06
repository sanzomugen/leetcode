class Solution:
    
    def squared(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        return nums
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # when no negative nums
        length_nums = len(nums)
        if length_nums==1:
            return self.squared(nums)
        hi = length_nums-1
        lo = 0
        count = 0
        result = []
        while count<len(nums):
            if abs(nums[hi])>abs(nums[lo]):
                result.append(nums[hi]**2)
                hi-=1
            else:
                result.append(nums[lo]**2)
                lo+=1
            count+=1
        return result[::-1]
