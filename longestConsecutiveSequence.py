from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums) == 0:
        #     return 0
        
        # nums.sort()
        
        # res = 1
        # temp = 1
        # for i in range(1, len(nums)):
        #     if nums[i] - nums[i - 1] == 1:
        #         temp += 1
        #     elif nums[i] - nums[i - 1] == 0:
        #         continue
        #     else:
        #         res = max(res, temp)
        #         temp = 1
        #     res = max(res, temp)
        # return res   
        
        num_set = set(nums)
        longest = 0
        
        for n in nums:
            # check if its start a sequence
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                
                longest = max(longest, length)
                
        return longest
        
nums = [100, 4, 200, 1, 3, 2]
solution = Solution()
print(solution.longestConsecutive(nums))