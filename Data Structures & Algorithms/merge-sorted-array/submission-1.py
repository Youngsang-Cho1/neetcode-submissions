class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # copy of nums1 (till idx = m)
        l1 = nums1[:m]
        # idx var for l1 and nums2
        i, j = 0, 0
        # idx for nums1 allocation
        idx = 0

        while (i + j) < (m + n):
            # if j > num2 length
            # OR l1[i] < nums2[j]
            if j >= n or (i < m and l1[i] < nums2[j]):
                nums1[idx] = l1[i]
                i += 1
            else:
                nums1[idx] = nums2[j]
                j += 1
            idx += 1








            
            



        