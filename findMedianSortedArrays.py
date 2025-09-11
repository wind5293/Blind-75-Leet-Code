from typing import List

class Solution:
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     listRes = []
    #     i = 0
    #     j = 0

    #     while i < len(nums1) and j < len(nums2):
    #         if nums1[i] == nums2[j]:
    #             listRes.append(nums1[i])
    #             listRes.append(nums2[j])
    #             i += 1
    #             j += 1

    #         elif nums1[i] < nums2[j]:
    #             listRes.append(nums1[i])
    #             i += 1
            
    #         else:
    #             listRes.append(nums2[j])
    #             j += 1
                
    #     listRes.extend(nums1[i:len(nums1)] if nums1[i:len(nums1)] else nums2[j:len(nums2)])
    #     length = len(listRes)
    #     return listRes[length // 2] if length % 2 != 0 else (listRes[length // 2 - 1] + listRes[length // 2]) / 2
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        listRes = nums1 + nums2
        listRes.sort()
        
        length = len(listRes)
        return listRes[length // 2] if length % 2 != 0 else (listRes[length // 2 - 1] + listRes[length // 2]) / 2
                
nums1 = [1, 2]
nums2 = [3, 4]
solution = Solution()
res = solution.findMedianSortedArrays(nums1, nums2)
print(res)