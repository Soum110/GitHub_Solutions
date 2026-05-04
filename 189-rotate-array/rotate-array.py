class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

        ## i/p = 1 2 3 4 5 6 7, k = 3 
        ## reverse = 7 6 5 4 3 2 1
        ## spilt = 7 6 5 | 4 3 2 1
        ## reverse each part =  5 6 7 | 1 2 3 4
        ## o/p = 5 6 7 1 2 3 4


        